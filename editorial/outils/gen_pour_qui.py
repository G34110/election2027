# -*- coding: utf-8 -*-
"""Regenere site/maquettes/pour-qui.html : matrice publics x candidats.
Grille pure : age (jeunes/actifs/retraites) x classe sociale (populaires/
moyennes/aisees/tres hauts patrimoines). Les publics qui ne relevent ni de
l'age ni de la classe (entreprises, professions, collectifs, immigres,
victimes...) n'apparaissent pas dans la matrice.
Source : champ 'publics' des fiches positions."""
import json, glob, html, collections

CANDS = [
 ('dominique-de-villepin','Dominique de Villepin'),
 ('marine-le-pen','Marine Le Pen'),
 ('jean-luc-melenchon','Jean-Luc Mélenchon'),
 ('edouard-philippe','Édouard Philippe'),
 ('raphael-glucksmann','Raphaël Glucksmann'),
 ('gabriel-attal','Gabriel Attal'),
]
THEMES = {
 'pouvoir-achat':'Pouvoir d\'achat','protection-sociale':'Protection sociale',
 'dette-deficits':'Dette & déficits','delinquance':'Délinquance',
 'environnement':'Environnement','immigration':'Immigration',
 'crises-internationales':'Crises intern.','inegalites':'Inégalités',
 'education':'Éducation','emploi-chomage':'Emploi','terrorisme':'Terrorisme','institutions':'Institutions'
}

AGES = [('J','Jeunes (<30 ans)'), ('A','Actifs (30-64 ans)'), ('R','Retraités (65 ans et +)')]
CLASSES = [('pop','populaires'), ('moy','moyennes'), ('ais','aisées'), ('tha','très hauts patrimoines')]
def g(a, c):
    return f'{dict(AGES)[a]} — {dict(CLASSES)[c]}'
ROWS_GRID = [g(a,c) for a,_ in AGES for c,_ in CLASSES]

def canon(pub):
    """Retourne les lignes de la grille age x classe, ou [] si hors grille."""
    p = pub.lower()
    # les publics migratoires ne sont ni un age ni une classe -> hors grille
    if any(k in p for k in ['immigr', 'étranger', 'réfugié', 'asile', 'déplacés']):
        return []
    # ultra-riches (actifs + retraites : le patrimoine concerne les deux)
    if any(k in p for k in ['très hauts patrimoines','les plus riches','méga','finance & hauts revenus']):
        return [g('A','tha'), g('R','tha')]
    # aises / patrimoine / hauts revenus
    if any(k in p for k in ['aisé','hauts salaires','patrimoine','niches','fortunes']):
        return [g('A','ais'), g('R','ais')]
    # jeunes
    if any(k in p for k in ['jeunes','apprenti','<30','étudiant']):
        return [g('J','pop'), g('J','moy')]
    # seniors encore actifs / futurs retraites / epargnants -> actifs moyens
    if any(k in p for k in ['seniors','futurs retraités','épargnants retraite']):
        return [g('A','moy')]
    # retraites & personnes agees : classes populaires + moyennes par defaut
    if any(k in p for k in ['minimum vieillesse','retraité','personnes âgées']):
        return [g('R','pop'), g('R','moy')]
    # classes moyennes explicites
    if 'classes moyennes' in p:
        return [g('A','moy')]
    # populaires / bas revenus / précaires
    if any(k in p for k in ['modeste','bas salaires','pauvreté','chômeur','demandeurs d\'emploi','illettrisme','dépense sociale','redistribution']):
        return [g('A','pop')]
    # professions d'Etat rattachées a leur classe ordinaire
    if any(k in p for k in ['enseignant','magistrat','corps diplomatique','défenseurs']):
        return [g('A','moy')]
    if any(k in p for k in ['policier','sécurité','armée','réserviste','justice','prison','renseignement','fonctionnaire']):
        return [g('A','pop'), g('A','moy')]
    # actifs generiques : toutes classes sauf ultra-riches
    if any(k in p for k in ['actif','salarié','travailleur','cotisant','contribuable']):
        return [g('A','pop'), g('A','moy'), g('A','ais')]
    # hors grille : entreprises, immigrés, familles, victimes, délinquants,
    # malades, territoires, citoyens, partenaires, générations futures...
    return []

cells = collections.defaultdict(lambda: collections.defaultdict(list))
for path in glob.glob('editorial/data/positions/*/*.json'):
    d = json.load(open(path, encoding='utf-8'))
    pubs = d.get('publics')
    if not pubs: continue
    cid, theme = d['candidat_id'], d['theme_id']
    for p in pubs:
        for row in canon(p['public']):
            cells[row][cid].append((THEMES.get(theme, theme), p['sens'], p['fondement']))

ordered = [r for r in ROWS_GRID if r in cells]

def cell_html(entries):
    if not entries: return '<td class="vide">—</td>'
    seen, items = set(), []
    for theme, sens, fond in entries:
        key = (theme, sens)
        if key in seen: continue
        seen.add(key)
        cls = 'bene' if sens == 'beneficie' else 'cont'
        mark = '●' if sens == 'beneficie' else '◌'
        star = '<sup>†</sup>' if fond == 'analyse_externe' else ''
        items.append(f'<span class="mini {cls}">{mark} {html.escape(theme)}{star}</span>')
    return '<td>' + '<br>'.join(items) + '</td>'

rows_html = ''
for label in ordered:
    tds = ''.join(cell_html(cells[label].get(cid, [])) for cid,_ in CANDS)
    rows_html += f'      <tr><th scope="row">{html.escape(label)}</th>{tds}</tr>\n'
head = ''.join(f'<th scope="col">{n}</th>' for _,n in CANDS)

page = f'''<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Pour qui ? — Matrice des publics visés | Comparer 2027</title>
<style>
  :root {{
    --fond: #faf9f7; --surface: #ffffff; --encre: #1d2129; --encre-2: #555b66;
    --filet: #e4e1dc; --ref-fond: #f0efec; --ok: #1f7a4d; --attente: #8a5a00;
    --accent: #3a4a63;
    --serif: Georgia, 'Times New Roman', serif;
    --sans: 'Marianne', -apple-system, 'Segoe UI', Roboto, sans-serif;
  }}
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{ font-family:var(--sans); background:var(--fond); color:var(--encre); line-height:1.55; }}
  .entete {{ background:var(--surface); border-bottom:1px solid var(--filet); padding:.9rem 1rem; display:flex; justify-content:space-between; align-items:center; gap:1rem; }}
  .logo {{ font-weight:700; font-size:1.05rem; }}
  a.logo {{ color:inherit; text-decoration:none; }}
  a.logo:hover {{ text-decoration:underline; }}
  .logo span {{ color:var(--accent); }}
  .entete nav {{ display:flex; gap:.9rem; font-size:.82rem; }}
  .entete nav a {{ color:var(--encre-2); text-decoration:none; }}
  .chapo {{ padding:1.4rem 1rem 1rem; max-width:1100px; margin:0 auto; }}
  .fil-ariane {{ font-size:.75rem; color:var(--encre-2); margin-bottom:.6rem; }}
  .fil-ariane a {{ color:var(--accent); text-decoration:none; font-weight:600; }}
  .chapo h1 {{ font-size:1.6rem; margin-bottom:.3rem; }}
  .resume3 {{ font-size:.9rem; color:var(--encre-2); max-width:75ch; }}
  .bloc {{ max-width:1100px; margin:0 auto; padding:0 1rem 1.4rem; overflow-x:auto; }}
  table {{ border-collapse:collapse; width:100%; background:var(--surface); font-size:.8rem; }}
  th, td {{ border:1px solid var(--filet); padding:.55rem .6rem; text-align:left; vertical-align:top; }}
  thead th {{ background:var(--ref-fond); font-size:.78rem; }}
  thead th:first-child {{ background:var(--surface); }}
  tbody th {{ font-size:.78rem; background:var(--ref-fond); width:14rem; }}
  td.vide {{ color:#b8b4ad; text-align:center; }}
  .mini {{ font-size:.72rem; white-space:nowrap; }}
  .mini.bene {{ color:var(--ok); }}
  .mini.cont {{ color:var(--attente); }}
  .legende {{ max-width:1100px; margin:0 auto; padding:0 1rem 1.5rem; font-size:.78rem; color:var(--encre-2); }}
  .legende .mini {{ margin-right:1rem; }}
  footer {{ border-top:1px solid var(--filet); background:var(--surface); padding:1.2rem 1rem; font-size:.78rem; color:var(--encre-2); }}
  footer .wrap {{ max-width:1100px; margin:0 auto; }}
  footer a {{ color:var(--accent); }}
</style>
</head>
<body>

<header class="entete">
  <a class="logo" href="index.html">Comparer <span>2027</span></a>
  <nav>
    <a href="index.html">Thèmes</a>
    <a href="index.html">Candidats</a>
    <a href="#">Méthode</a>
    <a href="#">Sources</a>
  </nav>
</header>

<main>
  <section class="chapo">
    <div class="fil-ariane"><a href="index.html">← Accueil</a> · Analyse / Pour qui ?</div>
    <h1>Pour qui profitent les programmes ?</h1>
    <p class="resume3">Matrice des publics visés par les mesures de chaque candidat, tous thèmes confondus, croisée <strong>âge × classe sociale</strong> — jeunes / actifs / retraités × populaires / moyennes / aisées / très hauts patrimoines. <strong>Règle éditoriale</strong> : un public n'apparaît que s'il est la cible explicite d'une mesure sourcée ou d'une analyse économique externe signalée par †. Les publics qui ne relèvent ni de l'âge ni de la classe (entreprises, professions, territoires…) et les cellules <em>attendue</em> ou <em>non sourcée</em> ne figurent pas dans cette matrice.</p>
  </section>

  <section class="bloc">
    <table>
      <thead><tr><th scope="col">Public visé</th>{head}</tr></thead>
      <tbody>
{rows_html}      </tbody>
    </table>
  </section>

  <section class="legende">
    <span class="mini bene">● bénéficie (mesure visant ce public)</span>
    <span class="mini cont">◌ contribue / pénalisé (finance ou subit la mesure)</span>
    <span>† selon une analyse économique externe — voir la fiche thème pour la source</span>
  </section>
</main>

<footer>
  <div class="wrap">
    <strong>Comparaison neutre.</strong> Aucun jugement éditorial — seules des positions sourcées, datées et vérifiables.
    <br><a href="index.html">Retour à l'accueil</a> · <a href="#">Charte éditoriale</a>
    <br>Maquette v0.1 — projet en construction
  </div>
</footer>

</body>
</html>
'''
open('site/maquettes/pour-qui.html', 'w', encoding='utf-8').write(page)
print('pour-qui.html régénéré —', len(ordered), 'lignes')
for r in ordered: print(' -', r)
