# -*- coding: utf-8 -*-
"""Pipeline hebdomadaire Comparer 2027 — a executer chaque dimanche 18h
(installation : scripts/install_tache_hebdo.bat).

Etapes :
 1. Re-telecharge chaque url_live des fiches 'sourcee' et compare le hash
    de contenu au hash connu (editorial/data/etat_verif.json).
    -> hash different = source modifiee : flag pour revue editoriale.
 2. Fiches 'attendue'/'non_sourcee' : surveille l'index programme du
    candidat -> changement = position peut-etre parue.
 3. Timbre 'Verifie le / Mis a jour le' dans le footer des pages theme.
 4. Entree dans le journal de charte.html si changements detectes.
 5. Regenere pour-qui.html et les chips (gen_pour_qui.py, gen_chips.py).
 6. git add/commit/push s'il y a des modifications.
 7. Deploiement FTP vers OVH (deploy_ovh.py) si identifiants disponibles.

Le pipeline DETECTE et SIGNALE les evolutions ; il ne reecrit jamais une
synthese neutre — les sources modifiees sont listees pour revue humaine
dans editorial/verif/verif-<date>.md.
"""
import json, glob, hashlib, re, subprocess, sys, urllib.request, gzip, datetime, os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)
TODAY = datetime.date.today()
TODAY_ISO = TODAY.isoformat()
TODAY_FR = TODAY.strftime('%d/%m/%Y')
TODAY_FR_LONG = TODAY.strftime('%d %B %Y').replace('October', 'octobre')

UA = {'User-Agent': 'Mozilla/5.0 (compatible; Comparer2027-verif/1.0)', 'Accept-Encoding': 'gzip'}

# index programme surveille pour les fiches non sourcees
PROG_INDEX = {
    'dominique-de-villepin': 'https://lafrancehumaniste.fr/projet-france-2027.html',
    'marine-le-pen': 'https://rassemblementnational.fr/22-mesures',
    'jean-luc-melenchon': 'https://melenchon2027.fr/programme2025/livre/',
    'edouard-philippe': 'https://www.edouardphilippe.fr/priorites',
    'raphael-glucksmann': 'https://raphaelglucksmann.eu/programme.html',
    'gabriel-attal': 'https://attalpresident.fr/programme',
}

ETAT_PATH = 'editorial/data/etat_verif.json'

def fetch(url):
    """Retourne (code_http, hash_contenu, taille). None si echec."""
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=20) as r:
            raw = r.read()
            if r.headers.get('Content-Encoding') == 'gzip':
                raw = gzip.decompress(raw)
            # normalise les blancs pour limiter les faux positifs
            norm = re.sub(rb'\s+', b' ', raw)
            return r.status, hashlib.sha256(norm).hexdigest(), len(raw)
    except urllib.error.HTTPError as e:
        return e.code, None, 0
    except Exception as e:
        return 0, None, 0

def main():
    etat = json.load(open(ETAT_PATH, encoding='utf-8')) if os.path.exists(ETAT_PATH) else {'sources': {}, 'index': {}}
    rapport = [f'# Vérification hebdomadaire — {TODAY_FR_LONG}\n']
    changes, errors, checked = [], [], 0
    themes_impacts = set()

    # ── 1. fiches sourcee : re-verification des url_live ──
    for path in sorted(glob.glob('editorial/data/positions/*/*.json')):
        d = json.load(open(path, encoding='utf-8'))
        src = (d.get('position_actuelle') or {}).get('source') or {}
        url = src.get('url_live')
        if not url:
            continue
        checked += 1
        code, h, taille = fetch(url)
        prev = etat['sources'].get(path, {})
        cid, theme = d['candidat_id'], d['theme_id']
        if h is None:
            errors.append((f'{cid}/{theme}', url, f'HTTP {code}'))
            continue
        if prev.get('hash') and prev['hash'] != h:
            changes.append((f'{cid}/{theme}', url, 'contenu modifié'))
            themes_impacts.add(theme)
            rapport.append(f'- **{cid} / {theme}** : source modifiée → revue éditoriale requise ({url})')
        etat['sources'][path] = {'hash': h, 'url': url, 'http': code, 'verif_le': TODAY_ISO, 'taille': taille}

    # ── 2. fiches attendue/non_sourcee : surveillance des index ──
    watch = set()
    for path in sorted(glob.glob('editorial/data/positions/*/*.json')):
        d = json.load(open(path, encoding='utf-8'))
        if d.get('statut') in ('attendue', 'non_sourcee'):
            watch.add(d['candidat_id'])
    for cid in sorted(watch):
        url = PROG_INDEX.get(cid)
        if not url:
            continue
        code, h, _ = fetch(url)
        prev = etat['index'].get(cid, {})
        if h is None:
            errors.append((f'{cid} (index)', url, f'HTTP {code}'))
            continue
        if prev.get('hash') and prev['hash'] != h:
            changes.append((f'{cid} (index programme)', url, 'index modifié — nouvelles positions possibles'))
            rapport.append(f'- **{cid}** : index programme modifié → vérifier si les positions attendues sont parues ({url})')
        etat['index'][cid] = {'hash': h, 'url': url, 'http': code, 'verif_le': TODAY_ISO}

    # ── 3. erreurs reseau dans le rapport ──
    if errors:
        rapport.append('\n### Sources injoignables (blocage anti-robot ou panne)')
        for c, u, e in errors:
            rapport.append(f'- {c} : {u} ({e})')

    os.makedirs('editorial/verif', exist_ok=True)
    rpath = f'editorial/verif/verif-{TODAY_ISO}.md'
    rapport.insert(1, f'{checked} sources re-vérifiées, {len(watch)} index candidats surveillés, '
                      f'{len(changes)} changement(s) détecté(s), {len(errors)} erreur(s) réseau.\n')
    open(rpath, 'w', encoding='utf-8').write('\n'.join(rapport) + '\n')
    json.dump(etat, open(ETAT_PATH, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print(f'[pipeline] {checked} sources, {len(changes)} changement(s), {len(errors)} erreur(s) -> {rpath}')

    # ── 4. timbres dans les pages theme ──
    for f in glob.glob('site/maquettes/theme-*.html'):
        theme = re.search(r'theme-([a-z-]+)\.html', f).group(1)
        s = open(f, encoding='utf-8').read()
        if theme in themes_impacts:
            txt = (f'Dernière mise à jour : {TODAY_FR} — une source a évolué, '
                   'revue éditoriale en cours.')
        else:
            txt = f'Verifié le {TODAY_FR} — aucune évolution détectée.'
        stamp = f'<p class="maj-auto">{txt}</p>'
        if '<p class="maj-auto">' in s:
            s = re.sub(r'<p class="maj-auto">.*?</p>', stamp, s, count=1, flags=re.S)
        else:
            s = s.replace('<br>Maquette v0.1 — projet en construction',
                          stamp + '\n    <br>Maquette v0.1 — projet en construction', 1)
        open(f, 'w', encoding='utf-8').write(s)

    # ── 5. journal dans charte.html si changements ──
    if changes:
        f = 'site/maquettes/charte.html'
        s = open(f, encoding='utf-8').read()
        detail = ' ; '.join(f'{c} ({w})' for c, _u, w in changes)
        entry = (f'    <li><span class="d">{TODAY_FR_LONG}</span> — Vérification hebdomadaire : '
                 f'{checked} sources contrôlées, {len(changes)} évolution(s) détectée(s) '
                 f'({detail}). Rapport : editorial/verif/verif-{TODAY_ISO}.md.</li>\n')
        s = s.replace('<ul class="journal">\n', '<ul class="journal">\n' + entry, 1)
        open(f, 'w', encoding='utf-8').write(s)
        print('[pipeline] journal mis à jour')

    # ── 6. regen des fichiers derives ──
    for gen in ('gen_pour_qui.py', 'gen_chips.py'):
        subprocess.run([sys.executable, '-X', 'utf8', f'editorial/outils/{gen}'],
                       check=True, capture_output=True)

    # ── 7. git ──
    if subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True).stdout.strip():
        subprocess.run(['git', 'add', '-A'], check=True)
        msg = (f'Verif hebdo {TODAY_FR} : {checked} sources, '
               f'{len(changes)} changement(s) detecte(s)'
               + (' (revue editoriale requise)' if changes else ''))
        subprocess.run(['git', 'commit', '-m', msg], check=True)
        subprocess.run(['git', 'push'], check=True)
        print('[pipeline] commit + push effectues')
    else:
        print('[pipeline] aucune modification -> pas de commit')

    # ── 8. deploiement ──
    if os.path.exists('deploy.secrets.json'):
        subprocess.run([sys.executable, '-X', 'utf8', 'editorial/outils/deploy_ovh.py'], check=False)
    else:
        print('[pipeline] deploy.secrets.json absent -> deploiement FTP ignore '
              '(renseignez les identifiants OVH pour activer)')

if __name__ == '__main__':
    main()
