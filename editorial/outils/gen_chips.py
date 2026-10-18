# -*- coding: utf-8 -*-
"""Regenere les chips 'Pour qui' des 12 pages theme depuis les JSON 'publics',
alignes sur le vocabulaire de la matrice : age x classe sociale.
- les publics age/classe deviennent des labels compacts (ex. 'Actifs — pop. a aisees')
- les publics hors grille (entreprises, immigres, professions, victimes,
  collectifs) restent affiches tels quels
- fondement 'analyse_externe' -> chip .ext avec † + lien vers l'analyse."""
import json, re, glob, html

AGES = ['Jeunes', 'Actifs', 'Retraités']
CLS = ['populaires', 'moyennes', 'aisées', 'très hauts patrimoines']
CLS_SHORT = {'populaires': 'populaires', 'moyennes': 'moyennes',
             'aisées': 'aisées', 'très hauts patrimoines': 'très hauts patrimoines'}

def canon_cells(pub):
    """Retourne (cells, transversal) : cells = set de (age_idx, cls_idx) ou None."""
    p = pub.lower()
    def g(a, c): return (AGES.index(a), CLS.index(c))
    # les publics migratoires ne sont ni un age ni une classe -> hors grille
    if any(k in p for k in ['immigr', 'étranger', 'réfugié', 'asile', 'déplacés']):
        return None
    if any(k in p for k in ['très hauts patrimoines', 'les plus riches', 'méga', 'finance & hauts revenus']):
        return {g('Actifs','très hauts patrimoines'), g('Retraités','très hauts patrimoines')}
    if any(k in p for k in ['aisé','hauts salaires','patrimoine','niches','fortunes']):
        return {g('Actifs','aisées'), g('Retraités','aisées')}
    if any(k in p for k in ['jeunes','apprenti','<30','étudiant']):
        return {g('Jeunes','populaires'), g('Jeunes','moyennes')}
    if any(k in p for k in ['seniors','futurs retraités','épargnants retraite']):
        return {g('Actifs','moyennes')}
    if any(k in p for k in ['minimum vieillesse','retraité','personnes âgées']):
        return {g('Retraités','populaires'), g('Retraités','moyennes')}
    if 'classes moyennes' in p:
        return {g('Actifs','moyennes')}
    if any(k in p for k in ['modeste','bas salaires','pauvreté','chômeur','demandeurs d\'emploi','illettrisme','dépense sociale','redistribution']):
        return {g('Actifs','populaires')}
    if any(k in p for k in ['enseignant','magistrat','corps diplomatique','défenseurs']):
        return {g('Actifs','moyennes')}
    if any(k in p for k in ['policier','sécurité','armée','réserviste','justice','prison','renseignement','fonctionnaire']):
        return {g('Actifs','populaires'), g('Actifs','moyennes')}
    if any(k in p for k in ['actif','salarié','travailleur','cotisant','contribuable']):
        return {g('Actifs','populaires'), g('Actifs','moyennes'), g('Actifs','aisées')}
    return None  # hors grille : label conserve

def merge_labels(cells):
    """Fusionne un set de (age,cls) : classes contigues d'un meme age -> un run,
    meme run sur plusieurs ages -> ages groupes."""
    by_age = {}
    for a, c in cells:
        by_age.setdefault(a, set()).add(c)
    runs = {}
    for a, cset in by_age.items():
        cs = sorted(cset)
        i = 0
        while i < len(cs):
            j = i
            while j + 1 < len(cs) and cs[j+1] == cs[j] + 1:
                j += 1
            run = cs[i:j+1]
            key = tuple(run)
            runs.setdefault(key, set()).add(a)
            i = j + 1
    out = []
    for run, aset in sorted(runs.items(), key=lambda kv: (min(kv[1]), kv[0][0])):
        ages = ' & '.join(AGES[a] for a in sorted(aset))
        if len(run) == 1:
            cls_lbl = CLS_SHORT[CLS[run[0]]]
        elif len(run) == 2:
            cls_lbl = CLS_SHORT[CLS[run[0]]].replace('populaires','pop.').replace('moyennes','moy.') + ' & ' + CLS_SHORT[CLS[run[1]]].replace('moyennes','moy.').replace('aisées','aisées').replace('très hauts patrimoines','très hauts patr.')
        else:
            cls_lbl = CLS_SHORT[CLS[run[0]]].replace('populaires','pop.').replace('moyennes','moy.') + ' à ' + CLS_SHORT[CLS[run[-1]]].replace('moyennes','moy.').replace('aisées','aisées')
        out.append(f'{ages} — {cls_lbl}')
    return out

def chips_block(pubs):
    """Construit le div .publics pour une carte."""
    parts = ['<div class="publics"><span class="lbl">Pour qui</span>']
    links = []
    for sens in ('beneficie', 'contribue'):
        cells, ext_cells, transv = set(), set(), []
        for p in pubs:
            if p['sens'] != sens:
                continue
            c = canon_cells(p['public'])
            if c is None:
                lbl = p['public']
                if p['fondement'] == 'analyse_externe':
                    lbl += ' †'
                    if p.get('source_url'):
                        links.append((p['source_url'], p.get('detail', 'analyse externe')))
                    transv.append((lbl, True))
                else:
                    transv.append((lbl, False))
            else:
                (ext_cells if p['fondement'] == 'analyse_externe' else cells).update(c)
                if p['fondement'] == 'analyse_externe' and p.get('source_url'):
                    links.append((p['source_url'], p.get('detail', 'analyse externe')))
        cls = 'chip' if sens == 'beneficie' else 'chip contrib'
        prefix = '' if sens == 'beneficie' else 'pénalisés : '
        for lbl in merge_labels(cells):
            parts.append(f'<span class="{cls}">{prefix}{html.escape(lbl)}</span>')
        for lbl in merge_labels(ext_cells):
            parts.append(f'<span class="{cls} ext">{prefix}{html.escape(lbl)} †</span>')
        for lbl, is_ext in transv:
            tag = f'{cls} ext' if is_ext else cls
            parts.append(f'<span class="{tag}">{prefix}{html.escape(lbl)}</span>')
    seen = set()
    for url, title in links:
        if url in seen:
            continue
        seen.add(url)
        parts.append(f'<a class="src-analyse" href="{url}" title="{html.escape(title)}">analyse ↗</a>')
    parts.append('</div>')
    return ''.join(parts)

ORDER = ['dominique-de-villepin','marine-le-pen','jean-luc-melenchon','edouard-philippe','raphael-glucksmann','gabriel-attal']

def page_theme(fname):
    return re.search(r'theme-([a-z-]+)\.html', fname).group(1)

PUBS_RE = re.compile(r'<div class="publics">.*?</div>', re.S)
n_files, n_chips = 0, 0
for f in sorted(glob.glob('site/maquettes/theme-*.html')):
    theme = page_theme(f)
    s = open(f, encoding='utf-8').read()
    arts = s.split('<article class="carte')
    out = [arts[0]]
    idx = 0
    for part in arts[1:]:
        seg = '<article class="carte' + part
        cid = ORDER[idx] if idx < len(ORDER) else None
        idx += 1
        try:
            d = json.load(open(f'editorial/data/positions/{cid}/{theme}.json', encoding='utf-8'))
        except FileNotFoundError:
            d = {}
        pubs = d.get('publics')
        if pubs:
            block = chips_block(pubs)
            if PUBS_RE.search(seg):
                seg = PUBS_RE.sub(lambda m: block, seg, count=1)
            else:
                seg = re.sub(r'(\n\s*</div>\s*\n\s*<div class="source">)', '\n          ' + block + r'\1', seg, count=1)
            n_chips += 1
        out.append(seg)
    open(f, 'w', encoding='utf-8').write(''.join(out))
    n_files += 1
    print('MAJ', f)
print('pages:', n_files, '| cartes avec chips:', n_chips)
