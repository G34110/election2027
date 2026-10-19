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

# barometre des preoccupations (Ipsos/BVA « La Tribune Dimanche »).
# Renseigner l'URL de la derniere publication pour detecter un nouveau
# classement -> le pipeline signale, la mise a jour des themes/* reste
# editoriale puis la cascade est mecanique (voir gouvernance_themes).
BAROMETRE_URL = None

CANDS_ORDER = [
    ('dominique-de-villepin', 'Dominique de Villepin', 'La France humaniste'),
    ('marine-le-pen', 'Marine Le Pen', 'Rassemblement National'),
    ('jean-luc-melenchon', 'Jean-Luc Mélenchon', 'La France Insoumise'),
    ('edouard-philippe', 'Édouard Philippe', 'Horizons'),
    ('raphael-glucksmann', 'Raphaël Glucksmann', 'Place Publique / PS'),
    ('gabriel-attal', 'Gabriel Attal', 'Renaissance'),
]

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

def gouvernance_themes(rapport):
    """Cascade mecanique : pour chaque theme actif dans editorial/data/themes/,
    garantit (a) les 6 fiches positions 'attendue', (b) la maquette
    theme-<id>.html, (c) la tuile d'index. Retourne les themes crees."""
    crees = []
    themes = []
    for f in sorted(glob.glob('editorial/data/themes/*.json')):
        if '_template' in f:
            continue
        t = json.load(open(f, encoding='utf-8'))
        themes.append(t)
    for t in themes:
        tid, titre = t['id'], t.get('titre', t['id'])
        if t.get('statut') == 'retire':
            rapport.append(f'- **thème {tid}** : statut « retire » — nettoyage manuel requis '
                           '(fiches JSON + maquette + tuile index)')
            continue
        # (a) stubs JSON par candidat
        for cid, _n, _p in CANDS_ORDER:
            p = f'editorial/data/positions/{cid}/{tid}.json'
            if not os.path.exists(p):
                stub = {
                    'candidat_id': cid, 'theme_id': tid, 'statut': 'attendue',
                    'maj_le': TODAY_ISO, 'commit_ref': '', 'alerte_maj': False,
                    'position_actuelle': None, 'fil_du_temps': [], 'actes_passes': [],
                    '_note': 'Fiche creee mecaniquement par le pipeline hebdomadaire '
                             '(nouveau theme) — position a documenter des publication.'}
                json.dump(stub, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
                open(p, 'a', encoding='utf-8').write('\n')
                rapport.append(f'- **{cid}/{tid}** : fiche « attendue » créée (nouveau thème)')
        # (b) maquette
        page = f'site/maquettes/theme-{tid}.html'
        if not os.path.exists(page):
            open(page, 'w', encoding='utf-8').write(skeleton_theme(tid, titre))
            crees.append(tid)
            rapport.append(f'- **thème {tid}** : maquette créée avec 6 cellules « attendue »')
        # (c) tuile index
        idx = 'site/maquettes/index.html'
        s = open(idx, encoding='utf-8').read()
        if f'theme-{tid}.html' not in s:
            tile = (f'      <a class="theme live" href="theme-{tid}.html">\n'
                    f'        <div class="top"><span class="titre">{titre}</span><span class="pct">—</span></div>\n'
                    f'        <div class="meta">Nouveau thème — positions attendues</div>\n'
                    f'        <span class="badge-live">Thème ajouté</span>\n'
                    f'      </a>\n')
            pos = s.find('<div class="grille-themes">')
            end = s.find('</div>\n  </section>', pos)
            s = s[:end] + tile + '    ' + s[end:]
            s = re.sub(r'Les \d+ thèmes', f'Les {len([t for t in themes if t.get("statut") != "retire"])} thèmes', s, count=1)
            open(idx, 'w', encoding='utf-8').write(s)
            rapport.append(f'- **index** : tuile « {titre} » ajoutée')
    return crees


def skeleton_theme(tid, titre):
    """Genere une maquette theme squelette : 6 cartes 'attendue', meme design."""
    ref = open('site/maquettes/theme-pouvoir-achat.html', encoding='utf-8').read()
    css = re.search(r'<style>.*?</style>', ref, re.S).group(0)
    cards = ''
    for cid, nom, parti in CANDS_ORDER:
        url = PROG_INDEX.get(cid, '')
        cards += f'''      <article class="carte">
        <div class="carte-tete">
          <div class="nom">{nom}</div>
          <div class="parti">{parti}</div>
        </div>
        <div class="corps">
          <div class="badges"><span class="badge b-attendue">Attendue</span></div>
          <div class="cellule-vide">
            Aucune position officielle publiée à ce jour.
            <span class="cellule-note">Thème ajouté mécaniquement — position à documenter dès publication.</span>
          </div>
        </div>
        <div class="source">
          <a href="{url}">{url.replace('https://', '')}</a>
          <span class="verif">Vérifié le {TODAY_FR} — position attendue</span>
        </div>
      </article>
'''
    return f'''<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{titre} — comparatif | Comparer 2027</title>
{css}
</head>
<body>

<header class="entete">
  <a class="logo" href="index.html">Comparer <span>2027</span></a>
  <nav>
    <a href="index.html#themes">Thèmes</a>
    <a href="index.html#candidats">Candidats</a>
    <a href="charte.html">Méthode</a>
    <a href="charte.html#sources">Sources</a>
  </nav>
</header>

<main>
  <section class="chapo">
    <div class="fil-ariane"><a href="index.html">← Accueil</a> · Thèmes / {titre}</div>
    <h1>{titre}</h1>
    <div class="resume3"><p><strong>Ce qu'il faut retenir.</strong> Thème ajouté mécaniquement par le pipeline hebdomadaire — les six positions sont attendues, à documenter dès publication des programmes.</p></div>
  </section>

  <section class="grille-cartes">
{cards}  </section>
</main>

<footer>
  <div class="wrap">
    <strong>Comparaison neutre.</strong> Aucun jugement éditorial — seules des positions sourcées, datées et vérifiables.
    <p class="maj-auto">Créé le {TODAY_FR} — positions attendues.</p>
    <br><a href="charte.html#sources">Mur des sources</a> · <a href="charte.html#journal">Journal des mises à jour</a> · <a href="charte.html">Charte éditoriale</a>
    <br>Maquette v0.1 — projet en construction
  </div>
</footer>

</body>
</html>
'''


def gouvernance_candidats(rapport):
    """Regle de selection : si le dernier sondage publie ne contient plus un
    candidat suivi, le signaler (retrait mecanique a confirmer)."""
    sonds = sorted(glob.glob('editorial/data/sondages/sond-*.json'))
    if not sonds:
        return
    d = json.load(open(sonds[-1], encoding='utf-8'))
    ids = {r.get('candidat_id') for r in d.get('resultats', []) if r.get('candidat_id')}
    for cid, nom, _p in CANDS_ORDER:
        if cid not in ids:
            rapport.append(f'- **{nom}** : absent du dernier sondage '
                           f'({d["id"]}) — règle §2 : retrait de la comparaison à appliquer si confirmé')


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

    # ── 2b. gouvernance : themes (cascade) + candidats (regle de selection) ──
    if BAROMETRE_URL:
        code, h, _ = fetch(BAROMETRE_URL)
        prev = etat['index'].get('barometre', {})
        if h and prev.get('hash') and prev['hash'] != h:
            changes.append(('baromètre des préoccupations', BAROMETRE_URL, 'nouveau classement possible'))
            rapport.append(f'- **baromètre** : classement des préoccupations probablement modifié '
                           f'→ mettre à jour editorial/data/themes/ (la cascade thème suit automatiquement)')
        if h:
            etat['index']['barometre'] = {'hash': h, 'url': BAROMETRE_URL, 'http': code, 'verif_le': TODAY_ISO}
    gouvernance_themes(rapport)
    gouvernance_candidats(rapport)

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
