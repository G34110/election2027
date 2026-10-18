# -*- coding: utf-8 -*-
"""Transforme les 'Ce qu'il faut retenir' des pages theme en listes a puces
(une ligne par candidat) + ajoute le CSS. Corrige au passage les resumes
devenus obsoletes (terrorisme/Melenchon et institutions/Philippe resourcedes)
et les mentions 'ref.' residuelles."""
import re, glob

NEW = {
'pouvoir-achat': '''Tous les candidats promettent des salaires plus élevés, par des voies opposées :
        <ul>
          <li><strong>Villepin</strong> — +200&nbsp;€ nets/mois via une CSG universelle <em>(chiffré)</em></li>
          <li><strong>Le Pen</strong> — hausse de 10&nbsp;% sans cotisations patronales <em>(chiffré, programme 2022)</em></li>
          <li><strong>Mélenchon</strong> — SMIC à 1&nbsp;600&nbsp;€ et indexation sur l'inflation <em>(chiffré)</em></li>
          <li><strong>Philippe</strong> — heures supplémentaires exonérées <em>(chiffré)</em></li>
          <li><strong>Glucksmann</strong> — rémunération des actifs financée par la taxe « méga-héritages » <em>(montant annoncé)</em></li>
          <li><strong>Attal</strong> — « choc » par la productivité et les charges allégées <em>(non chiffré)</em></li>
        </ul>''',
'protection-sociale': '''Retraites : le clivage est frontal.
        <ul>
          <li><strong>Villepin</strong> — abrogation de la réforme 2023 via convention citoyenne <em>(orienté)</em></li>
          <li><strong>Le Pen</strong> — 60 ans réservé aux carrières précoces <em>(chiffré)</em></li>
          <li><strong>Mélenchon</strong> — retour à 60 ans / 40 annuités <em>(chiffré)</em></li>
          <li><strong>Philippe</strong> — 65 ans progressif <em>(chiffré)</em></li>
          <li><strong>Attal</strong> — durée de cotisation plutôt que l'âge <em>(non chiffré)</em></li>
        </ul>
        Santé : « 100&nbsp;% Sécu » (Mélenchon), plan d'urgence de 20&nbsp;Md€ (Le Pen), services publics renforcés (Glucksmann — non chiffré).''',
'dette-deficits': '''Diagnostic partagé (dette jugée insoutenable) mais remèdes opposés :
        <ul>
          <li><strong>Villepin</strong> — extinction des niches fiscales <em>(chiffré, ~12&nbsp;Md€/an pour les déficits)</em></li>
          <li><strong>Le Pen</strong> — coupes UE/immigration/agences + impôt sur les fortunes financières <em>(chiffré, ~36&nbsp;Md€)</em></li>
          <li><strong>Mélenchon</strong> — hausse des impôts sur les plus riches <em>(chiffré, +100&nbsp;Md€ de recettes)</em></li>
          <li><strong>Philippe</strong> — règle d'or constitutionnelle + fonctionnaires réduits <em>(chiffré, −250&nbsp;000)</em></li>
          <li><strong>Glucksmann</strong> — justice fiscale <em>(non chiffré)</em></li>
          <li><strong>Attal</strong> — « zéro déficit en 10 ans » <em>(chiffré)</em></li>
        </ul>''',
'delinquance': '''Durcissement des sanctions chez quatre candidats, intensités différentes :
        <ul>
          <li><strong>Villepin</strong> — alourdissement pour les crimes les plus violents <em>(non sourcé)</em></li>
          <li><strong>Le Pen</strong> — peines planchers + 85&nbsp;000 places de prison + doublement des magistrats <em>(chiffré)</em></li>
          <li><strong>Mélenchon</strong> — approche opposée : police de proximité + régulation carcérale <em>(orienté)</em></li>
          <li><strong>Philippe</strong> — peines planchers + suppression du JAP + « pouvoir aux maires » <em>(chiffré)</em></li>
          <li><strong>Glucksmann</strong> — documenté mais non sourcé</li>
          <li><strong>Attal</strong> — pas de chantier sécurité publié</li>
        </ul>''',
'environnement': '''Fracture nette sur l'énergie et la stratégie climatique :
        <ul>
          <li><strong>Villepin</strong> — bifurcation écologique érigée en condition de la prospérité <em>(chiffré, 700-800&nbsp;000 emplois)</em></li>
          <li><strong>Le Pen</strong> — nucléaire relancé + sortie du marché européen de l'électricité <em>(non chiffré)</em></li>
          <li><strong>Mélenchon</strong> — planification écologique et « règle verte » <em>(chiffré, −65&nbsp;% en 2030)</em></li>
          <li><strong>Philippe</strong> — nucléaire relancé + adaptation financée <em>(chiffré, 8 EPR, 2&nbsp;Md€/an)</em></li>
          <li><strong>Glucksmann</strong> — justice climatique <em>(non chiffré)</em></li>
          <li><strong>Attal</strong> — réduction accélérée des émissions <em>(chiffré, −5&nbsp;%/an)</em></li>
        </ul>''',
'immigration': '''Six postures distinctes :
        <ul>
          <li><strong>Villepin</strong> — refus du « piège identitaire », pas de mesures de politique migratoire publiées</li>
          <li><strong>Le Pen</strong> — référendum et « priorité nationale » <em>(chiffré)</em></li>
          <li><strong>Mélenchon</strong> — politique « humaniste et réaliste », régularisations et carte de séjour 10 ans</li>
          <li><strong>Philippe</strong> — division par deux et quotas <em>(chiffré)</em></li>
          <li><strong>Glucksmann</strong> — convention citoyenne</li>
          <li><strong>Attal</strong> — frontières comme enjeu de puissance, préférence travail à points</li>
        </ul>''',
'crises-internationales': '''L'OTAN et la puissance européenne cristallisent les désaccords :
        <ul>
          <li><strong>Villepin</strong> — « le chemin gaulliste » de l'indépendance, Europe souveraine</li>
          <li><strong>Le Pen</strong> — sortie du commandement intégré de l'OTAN</li>
          <li><strong>Mélenchon</strong> — sortie du commandement intégré puis de l'organisation, non-alignement</li>
          <li><strong>Philippe</strong> — massification des forces <em>(chiffré, 250&nbsp;000 réservistes)</em></li>
          <li><strong>Glucksmann</strong> — « l'Europe puissance » comme doctrine</li>
          <li><strong>Attal</strong> — soutien à l'Ukraine « sans relâche », doctrine de puissance</li>
        </ul>''',
'inegalites': '''Le sujet est décliné différemment selon les candidats :
        <ul>
          <li><strong>Villepin</strong> — lutte contre la pauvreté érigée en priorité politique</li>
          <li><strong>Le Pen</strong> — soutien aux familles : part fiscale, héritage désimposé <em>(chiffré)</em></li>
          <li><strong>Mélenchon</strong> — « révolution fiscale » et mise au pas de la finance <em>(chiffré)</em></li>
          <li><strong>Philippe</strong> — nouvelle politique familiale chiffrée</li>
          <li><strong>Glucksmann</strong> — réduction des inégalités « entre territoires et générations »</li>
          <li><strong>Attal</strong> — pas de volet dédié publié</li>
        </ul>''',
'education': '''Six approches sourcées :
        <ul>
          <li><strong>Villepin</strong> — « refonder l'école pour refaire société » <em>(chiffré, +20&nbsp;% de dépenses/élève sur 10 ans)</em></li>
          <li><strong>Le Pen</strong> — restauration de la « transmission des savoirs »</li>
          <li><strong>Mélenchon</strong> — éradication de l'illettrisme et « école globale »</li>
          <li><strong>Philippe</strong> — « école de la liberté et de l'exigence », enseignants +20&nbsp;% <em>(chiffré)</em></li>
          <li><strong>Glucksmann</strong> — plan de sauvetage de l'école publique</li>
          <li><strong>Attal</strong> — objectif PISA chiffré, école « mère des batailles »</li>
        </ul>''',
'emploi-chomage': '''Conceptions opposées de l'assurance-chômage et de l'emploi :
        <ul>
          <li><strong>Villepin</strong> — « droit au travail » réhabilité, fusion allocations/formation</li>
          <li><strong>Le Pen</strong> — ciblage jeunes : IR à 0, chèque-formation <em>(chiffré)</em></li>
          <li><strong>Mélenchon</strong> — garantie d'emploi pour tout chômeur de longue durée <em>(chiffré)</em></li>
          <li><strong>Philippe</strong> — indemnisation limitée à 12 mois <em>(chiffré)</em></li>
          <li><strong>Glucksmann</strong> — pas de volet chômage publié</li>
          <li><strong>Attal</strong> — nouvelle réforme affichant +100&nbsp;000 emplois <em>(annoncé)</em></li>
        </ul>''',
'terrorisme': '''Quatre positions publiées, deux absentes :
        <ul>
          <li><strong>Villepin</strong> — antiterrorisme « dans l'État de droit », prévention renforcée</li>
          <li><strong>Le Pen</strong> — éradication des « réseaux islamistes »</li>
          <li><strong>Mélenchon</strong> — nouvelle stratégie antiterroriste, sortie de « l'état d'urgence permanent »</li>
          <li><strong>Philippe</strong> — lutte adossée à la guerre contre le narcotrafic</li>
          <li><strong>Glucksmann, Attal</strong> — pas de volet antiterroriste publié à ce jour</li>
        </ul>''',
'institutions': '''Deux changements de République et quatre réformes démocratiques :
        <ul>
          <li><strong>Villepin</strong> — « le chemin gaulliste », Big Bang de la règle républicaine</li>
          <li><strong>Le Pen</strong> — RIC et proportionnelle</li>
          <li><strong>Mélenchon</strong> — 6e République par Assemblée constituante</li>
          <li><strong>Philippe</strong> — méthode par dissolution et référendums adossés <em>(source secondaire)</em></li>
          <li><strong>Glucksmann</strong> — rénovation pour la lisibilité et les contre-pouvoirs</li>
          <li><strong>Attal</strong> — pas de volet institutionnel publié</li>
        </ul>''',
}

RE = re.compile(r'<p class="resume3"><strong>Ce qu\'il faut retenir\.</strong>.*?</p>', re.S)
CSS_ANCHOR = '.resume3 strong { color:var(--encre); font-weight:600; }'
CSS_ADD = CSS_ANCHOR + '\n  .resume3 ul { margin:.4rem 0 .5rem 1.15rem; }\n  .resume3 li { margin-bottom:.3rem; }\n  .resume3 li strong { color:var(--encre); font-weight:600; }'

for f in sorted(glob.glob('site/maquettes/theme-*.html')):
    theme = re.search(r'theme-([a-z-]+)\.html', f).group(1)
    s = open(f, encoding='utf-8').read()
    if CSS_ADD not in s:
        s = s.replace(CSS_ANCHOR, CSS_ADD, 1)
    block = NEW.get(theme)
    if block:
        repl = '<div class="resume3"><p><strong>Ce qu\'il faut retenir.</strong> ' + block + '</p></div>'
        s2, n = RE.subn(repl, s, count=1)
        s = s2
        print(f'{theme}: {"OK" if n else "!! non trouvé"}')
    open(f, 'w', encoding='utf-8').write(s)
