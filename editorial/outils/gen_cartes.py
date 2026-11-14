# -*- coding: utf-8 -*-
"""Regenere le corps + bloc source d'une carte candidat dans les pages theme,
depuis editorial/data/positions/<cid>/<theme>.json.
Usage : python gen_cartes.py <candidat_id> [theme ...]
Seules les cartes 'sourcee' sont reconstruites (attendue/non_sourcee conservees)."""
import json, re, sys, glob, html

STATUT_BADGE = {'sourcee': ('b-sourcee', 'Sourcée'),
                'attendue': ('b-attendue', 'Attendue'),
                'non_sourcee': ('b-nonsourcee', 'Non sourcée')}
TYPE_BADGE = {'chiffree': ('b-chiffree', 'Chiffrée'),
              'orientee': ('b-orientee', 'Orientée')}

def short_url(u):
    m = re.sub(r'^https?://', '', u)
    parts = m.split('/')
    host, path = parts[0], '/'.join(parts[1:])
    return host + ('/' + path if len(path) <= 38 else '/' + path[:35] + '…')

def esc(t):
    return html.escape(t, quote=False)

def corps_html(pos):
    b1 = '<span class="badge %s">%s</span>' % STATUT_BADGE['sourcee']
    b2 = ''
    if pos.get('type_mesure') in TYPE_BADGE:
        b2 = '<span class="badge %s">%s</span>' % TYPE_BADGE[pos['type_mesure']]
    lines = ['<div class="corps">',
             '<div class="badges">%s%s</div>' % (b1, b2),
             '<p class="synthese">%s</p>' % esc(pos['synthese']),
             '<div class="mesure">%s</div>' % esc(pos['mesure_phare'])]
    verb = pos.get('sources', [pos['source']])[0].get('verbatim', '')
    if verb:
        lines.append('<div class="verbatim">« %s »</div>' % esc(verb))
    lines.append('</div>')
    return '\n          '.join(lines)

def source_html(d):
    pos = d['position_actuelle']
    srcs = pos.get('sources') or [pos['source']]
    out = ['<div class="source">']
    for s in srcs:
        out.append('  <a href="%s">%s</a>' % (s['url_live'], html.escape(short_url(s['url_live']))))
        if s.get('url_archive'):
            out.append('  <a href="%s">↳ archive web.archive.org</a>' % s['url_archive'])
        out.append('  <span class="verif">Vérifié le %s</span>' %
                   '/'.join(reversed(s.get('date_verification', '').split('-'))))
    out.append('</div>')
    return '\n          '.join(out)

def rebuild(theme_file, cid):
    try:
        d = json.load(open('editorial/data/positions/%s/%s.json' % (cid, theme_file), encoding='utf-8'))
    except FileNotFoundError:
        return False
    if d.get('statut') != 'sourcee' or not d.get('position_actuelle'):
        return False
    f = 'site/maquettes/theme-%s.html' % theme_file
    s = open(f, encoding='utf-8').read()
    # localise l'article du candidat : balise article contenant "carte" dont le .corps suit
    arts = list(re.finditer(r'<article class="carte[^"]*">([\s\S]*?)</article>', s))
    ORDER = ['dominique-de-villepin', 'marine-le-pen', 'jean-luc-melenchon',
             'edouard-philippe', 'raphael-glucksmann', 'gabriel-attal']
    idx = ORDER.index(cid)
    if idx >= len(arts):
        print('  !! pas de carte', cid, 'dans', f)
        return False
    seg = arts[idx].group(0)
    new_seg = re.sub(r'<div class="corps">[\s\S]*?</div>\s*(?=<div class="source">)',
                     corps_html(d['position_actuelle']) + '\n          ', seg, count=1)
    new_seg = re.sub(r'<div class="source">[\s\S]*?</div>\s*</article>',
                     source_html(d) + '\n      </article>', new_seg, count=1)
    open(f, 'w', encoding='utf-8').write(s[:arts[idx].start()] + new_seg + s[arts[idx].end():])
    return True

cid = sys.argv[1]
themes = sys.argv[2:] or [re.search(r'theme-([a-z-]+)\.html', f).group(1)
                          for f in sorted(glob.glob('site/maquettes/theme-*.html'))]
for t in themes:
    print(t, 'MAJ' if rebuild(t, cid) else 'inchangé')
