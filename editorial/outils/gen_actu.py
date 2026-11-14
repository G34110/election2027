# -*- coding: utf-8 -*-
"""Genere site/maquettes/actualites.html depuis editorial/data/actualites.json :
1) l'actualite datee des six candidats suivis,
2) les personnalites « non encore declarees » que les sondages mesurent,
3) les candidats declares hors de la selection de six (regle §2)."""
import json, html

D = json.load(open('editorial/data/actualites.json', encoding='utf-8'))
E = html.escape
MAJ = '/'.join(reversed(D['maj_le'].split('-')))

def actu_card(c):
    items = ''.join(
        f'<div class="actu-item"><span class="actu-date">{E(i["date"])}</span>'
        f'<p>{E(i["texte"])}</p>'
        f'<a class="actu-src" href="{i["url"]}">{E(i["source"])} ↗</a></div>'
        for i in c['items'])
    return (f'<article class="actu-carte"><div class="actu-tete">'
            f'<div class="n">{E(c["candidat"])}</div><div class="p">{E(c["parti"])}</div></div>{items}</article>')

def nd_card(p):
    return (f'<article class="actu-carte"><div class="actu-tete">'
            f'<div class="n">{E(p["nom"])}</div><div class="p">{E(p["etiquette"])}</div></div>'
            f'<div class="actu-item"><p class="mesures">{E(p["mesures"])}</p>'
            f'<p class="nd-note">{E(p["note"])}</p></div></article>')

H = D['declares_hors_selection']
rows = ''.join(
    f'<tr><td><strong>{E(c["nom"])}</strong></td><td>{E(c["parti"])}</td>'
    f'<td>{E(c["statut"])}</td><td>{str(c["pct"]) + " %" if c["pct"] else "—"}</td></tr>'
    for c in H['candidats'])

page = f'''<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Actualités et candidatures | Comparer 2027</title>
<style>
  :root {{
    --fond: #faf9f7; --surface: #ffffff; --encre: #1d2129; --encre-2: #555b66;
    --filet: #e4e1dc; --ref-fond: #f0efec;
    --ok: #1f7a4d; --attente: #8a5a00; --accent: #3a4a63;
    --sans: 'Marianne', -apple-system, 'Segoe UI', Roboto, sans-serif;
  }}
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{ font-family:var(--sans); background:var(--fond); color:var(--encre); line-height:1.6; }}
  .entete {{ background:var(--surface); border-bottom:1px solid var(--filet); padding:.9rem 1rem; display:flex; justify-content:space-between; align-items:center; }}
  .logo {{ font-weight:700; font-size:1.05rem; }}
  a.logo {{ color:inherit; text-decoration:none; }}
  .logo span {{ color:var(--accent); }}
  .entete nav {{ display:flex; gap:.9rem; font-size:.82rem; flex-wrap:wrap; }}
  .entete nav a {{ color:var(--encre-2); text-decoration:none; }}
  .entete nav a:hover {{ text-decoration:underline; }}
  .wrap {{ max-width:1100px; margin:0 auto; padding:1.6rem 1rem 2.5rem; }}
  .fil-ariane {{ font-size:.75rem; color:var(--encre-2); margin-bottom:.6rem; }}
  .fil-ariane a {{ color:var(--accent); text-decoration:none; font-weight:600; }}
  h1 {{ font-size:1.6rem; margin-bottom:.4rem; }}
  .intro {{ color:var(--encre-2); font-size:.92rem; max-width:100ch; margin-bottom:1.6rem; }}
  h2 {{ font-size:1.15rem; margin:1.8rem 0 .7rem; padding-top:1.2rem; border-top:1px solid var(--filet); }}
  h2:first-of-type {{ border-top:none; padding-top:0; }}
  .h2-note {{ font-size:.78rem; color:var(--encre-2); font-weight:400; margin:-.4rem 0 .8rem; }}
  .grid {{ display:grid; grid-template-columns:repeat(auto-fill,minmax(320px,1fr)); gap:.9rem; }}
  .actu-carte {{ background:var(--surface); border:1px solid var(--filet); border-radius:10px; padding:.9rem 1rem; }}
  .actu-tete {{ border-bottom:1px solid var(--filet); padding-bottom:.5rem; margin-bottom:.6rem; }}
  .actu-tete .n {{ font-weight:700; font-size:.98rem; }}
  .actu-tete .p {{ font-size:.72rem; color:var(--encre-2); }}
  .actu-item {{ margin-bottom:.7rem; }}
  .actu-item:last-child {{ margin-bottom:0; }}
  .actu-date {{ display:inline-block; font-size:.68rem; font-weight:700; color:var(--accent); background:#e9edf3; border-radius:4px; padding:.08rem .45rem; margin-bottom:.25rem; }}
  .actu-item p {{ font-size:.83rem; margin-bottom:.3rem; }}
  .actu-src {{ font-size:.72rem; color:var(--accent); }}
  .mesures {{ font-weight:600; }}
  .nd-note {{ color:var(--encre-2); font-size:.8rem; }}
  table {{ border-collapse:collapse; width:100%; font-size:.82rem; margin:.6rem 0 1rem; background:var(--surface); }}
  th, td {{ border:1px solid var(--filet); padding:.45rem .6rem; text-align:left; vertical-align:top; }}
  thead th {{ background:var(--ref-fond); font-size:.75rem; }}
  .encadre {{ background:var(--surface); border:1px solid var(--filet); border-left:3px solid var(--accent); border-radius:6px; padding:.8rem 1rem; font-size:.85rem; margin:.8rem 0 1.2rem; }}
  footer {{ border-top:1px solid var(--filet); background:var(--surface); margin-top:2rem; }}
  .wrapf {{ max-width:1100px; margin:0 auto; padding:1.4rem 1rem 2rem; font-size:.78rem; color:var(--encre-2); }}
  .wrapf a {{ color:var(--accent); }}
  .maj {{ font-size:.72rem; color:var(--encre-2); }}
</style>
</head>
<body>

<header class="entete">
  <a class="logo" href="index.html">Comparer <span>2027</span></a>
  <nav>
    <a href="index.html#themes">Thèmes</a>
    <a href="index.html#candidats">Candidats</a>
    <a href="pour-qui.html">Pour qui&nbsp;?</a>
    <a href="charte.html">Charte</a>
    <a href="actualites.html">Actualités</a>
  </nav>
</header>

<main class="wrap">
  <div class="fil-ariane"><a href="index.html">Accueil</a> › Actualités et candidatures</div>
  <h1>Actualités et candidatures</h1>
  <p class="intro">Ce qui bouge dans les six campagnes suivies, les personnalités que les Français voient
  encore se déclarer, et les candidats déjà en lice hors de notre sélection. <span class="maj">Dernière mise à jour : {MAJ}.</span></p>

  <h2>L'actualité des six candidats suivis</h2>
  <p class="h2-note">Événements datés et sourcés qui modifient ou éclairent leur programme.</p>
  <div class="grid">
    {''.join(actu_card(c) for c in D['actus_candidats'])}
  </div>

  <h2>Non encore déclarés… mais les Français y pensent</h2>
  <p class="h2-note">Personnalités <strong>sans candidature officiellement déclarée</strong> (au {MAJ}) mais présentes
  dans les baromètres d'intentions de vote ou de « satisfaits si élu(e) » — mesures Ipsos (baromètre des personnalités,
  automne 2026), Cluster17 (sept. 2026) et Odoxa (question ouverte, mai 2025).</p>
  <div class="grid">
    {''.join(nd_card(p) for p in D['non_declares'])}
  </div>

  <h2>Déclarés, hors de la sélection suivie</h2>
  <div class="encadre">{E(H['note'])} La règle mécanique est la même pour tous :
  une candidature qui s'installe durablement dans les sondages intègre la comparaison.</div>
  <table>
    <thead><tr><th>Candidat(e)</th><th>Parti</th><th>Statut</th><th>Intentions (oct. 2026)</th></tr></thead>
    <tbody>{rows}</tbody>
  </table>
  <p class="h2-note">Source des scores : <a href="{H['url_source']}">OpinionWay — baromètre Presitrack 2027, vague 3 (PDF) ↗</a></p>
</main>

<footer>
  <div class="wrapf">
    <strong>Comparaison neutre.</strong> Aucun jugement éditorial — seules des positions sourcées, datées et vérifiables.
    <br><a href="index.html">Retour à l'accueil</a> · <a href="pour-qui.html">Matrice « Pour qui »</a> · <a href="charte.html">Charte éditoriale</a>
    <br>Maquette v0.1 — projet en construction
  </div>
</footer>

</body>
</html>
'''
open('site/maquettes/actualites.html', 'w', encoding='utf-8').write(page)
print('actualites.html genere —', len(D['actus_candidats']), 'candidats,', len(D['non_declares']), 'non declares')
