# -*- coding: utf-8 -*-
"""Injecte le champ 'publics' dans les fiches positions et les chips dans les maquettes thème."""
import json, glob, re, collections

# (candidat, theme) -> [(public, sens, detail)]
D = {
('dominique-de-villepin','crises-internationales'): [
 ("Armées & défense","beneficie","capacités de défense européenne (conseil de sécurité européen)"),
 ("Citoyens européens","beneficie","autonomie stratégique face aux pressions extérieures")],
('dominique-de-villepin','dette-deficits'): [
 ("Générations futures","beneficie","retour à l'équilibre des comptes publics"),
 ("Bénéficiaires de niches fiscales","contribue","extinction des ~400 niches (~175 Md€/an)")],
('dominique-de-villepin','education'): [
 ("Élèves","beneficie","démocratisation des savoirs, +20 % de dépenses réelles par élève sur 10 ans"),
 ("Enseignants","beneficie","budget sanctuarisé, revalorisé de l'inflation")],
('dominique-de-villepin','emploi-chomage'): [
 ("Chômeurs","beneficie","droit au travail, fusion allocations-chômage et crédits de formation"),
 ("Actifs","beneficie","sens du travail remis au centre du pacte républicain")],
('dominique-de-villepin','environnement'): [
 ("Générations futures","beneficie","seuils écologiques et prospérité durable"),
 ("Ménages modestes","beneficie","redistribution sociale de la transition"),
 ("Pollueurs","contribue","incitations fiscales au coût réel de la pollution")],
('dominique-de-villepin','immigration'): [
 ("Immigrés & étrangers","beneficie","défense de l'universalisme républicain contre le « piège identitaire »")],
('dominique-de-villepin','inegalites'): [
 ("Personnes en pauvreté","beneficie","9,5 M sous le seuil — pauvreté des travailleurs traitée structurellement")],
('dominique-de-villepin','institutions'): [
 ("Citoyens","beneficie","président arbitre, refus des contournements de la Constitution")],
('dominique-de-villepin','protection-sociale'): [
 ("Malades & usagers","beneficie","logique de prévention, refus de la privatisation de la santé"),
 ("Personnes âgées dépendantes","beneficie","caisse de Sécurité sociale de l'autonomie")],
('dominique-de-villepin','terrorisme'): [
 ("Forces de sécurité & renseignement","beneficie","consolidation PNAT/DGSI, prévention renforcée"),
 ("Libertés publiques","beneficie","stabilité juridique, pas d'inflation des lois d'exception")],
('edouard-philippe','crises-internationales'): [
 ("Réservistes & armées","beneficie","250 000 réservistes, service volontaire 50 000/an, munitions")],
('edouard-philippe','delinquance'): [
 ("Victimes","beneficie","courtes peines dès la 1re infraction, arsenal pénal renforcé"),
 ("Délinquants","contribue","peines planchers, suppression du juge d'application des peines")],
('edouard-philippe','dette-deficits'): [
 ("Générations futures","beneficie","déficit ramené à 2 % du PIB en fin de quinquennat"),
 ("Fonctionnaires","contribue","suppression d'un tiers des départs à la retraite (−250 000 postes)")],
('edouard-philippe','education'): [
 ("Enseignants","beneficie","+20 % de rémunération moyenne sur le quinquennat"),
 ("Élèves","beneficie","primaire concentrée sur les fondamentaux"),
 ("Chefs d'établissement","beneficie","autonomie : méthodes, horaires, recrutement")],
('edouard-philippe','emploi-chomage'): [
 ("Chômeurs <50 ans","contribue","indemnisation ramenée à 12 mois max (vs 18)"),
 ("Salariés en arrêt maladie","contribue","3 jours de carence, privé comme public"),
 ("Entreprises","beneficie","période incompressible arrêt/rupture conventionnelle")],
('edouard-philippe','environnement'): [
 ("Filière nucléaire","beneficie","8 EPR supplémentaires"),
 ("Ménages des territoires","beneficie","adaptation : DATAR 2.0, fonds 2 Md€/an"),
 ("Importateurs carbonés","contribue","prix du carbone aux frontières européennes")],
('edouard-philippe','immigration'): [
 ("Immigrés & demandeurs d'asile","contribue","division par deux : regroupement familial suspendu, quotas, fin de l'asile à vie"),
 ("Nationaux","beneficie","priorité affichée sur les flux")],
('edouard-philippe','inegalites'): [
 ("Familles","beneficie","allocation unique dès le 1er enfant, PTZ par naissance, temps partiel"),
 ("Classes moyennes","beneficie","IR supprimé les 3 premières années de l'enfant")],
('edouard-philippe','institutions'): [
 ("Citoyens","beneficie","référendums adossés aux législatives")],
('edouard-philippe','protection-sociale'): [
 ("Futurs retraités","contribue","65 ans progressif, 45 annuités en moins de 10 ans"),
 ("Épargnants retraite","beneficie","capitalisation collective, plan d'épargne abondé 500 €")],
('edouard-philippe','terrorisme'): [
 ("Forces de renseignement","beneficie","DGSI mobilisée sur le narcotrafic"),
 ("Narcotrafiquants","contribue","régime des peines aligné sur celui des terroristes")],
('gabriel-attal','crises-internationales'): [
 ("Armées & réserve","beneficie","amplification du réarmement, réserves opérationnelles"),
 ("Ukraine & partenaires","beneficie","soutien « sans relâche »")],
('gabriel-attal','dette-deficits'): [
 ("Générations futures","beneficie","« zéro déficit en 10 ans maximum »"),
 ("Bénéficiaires de la dépense sociale","contribue","effort porté d'abord sur la dépense sociale")],
('gabriel-attal','education'): [
 ("Élèves","beneficie","<20 élèves par classe en primaire, Choc des savoirs rétabli"),
 ("Enseignants","beneficie","reconnaissance du métier (objectif PISA 10 ans)")],
('gabriel-attal','emploi-chomage'): [
 ("Seniors","beneficie","« droit au travail » : durée de cotisation plutôt qu'âge"),
 ("Chômeurs","contribue","réforme pour que « travailler rapporte toujours plus »"),
 ("Demandeurs d'emploi","beneficie","+100 000 emplois affichés")],
('gabriel-attal','environnement'): [
 ("Ménages","beneficie","rénovation thermique, véhicule électrique accessible"),
 ("Filières industrielles vertes","beneficie","décarbonation industrielle"),
 ("Générations futures","beneficie","« dette écologique » : −5 %/an d'émissions jusqu'en 2030")],
('gabriel-attal','immigration'): [
 ("Immigrés de travail","beneficie","préférence travail, système à points (modèle canadien)"),
 ("Familles d'immigrés","contribue","regroupement familial « qui doit diminuer »")],
('gabriel-attal','protection-sociale'): [
 ("Seniors actifs","beneficie","droit au travail, durée de cotisation plutôt qu'âge"),
 ("Bénéficiaires de la dépense sociale","contribue","cadre budgétaire de réduction de la dépense")],
('jean-luc-melenchon','crises-internationales'): [
 ("Corps diplomatique","beneficie","réseau diplomatique rétabli"),
 ("Alliés atlantiques","contribue","retrait du commandement intégré de l'OTAN puis de l'organisation")],
('jean-luc-melenchon','delinquance'): [
 ("Victimes & quartiers","beneficie","police de proximité au service de la sûreté"),
 ("Policiers & justice","beneficie","doublement des effectifs, moyens humains"),
 ("Détenus","beneficie","régulation carcérale contraignante contre la surpopulation")],
('jean-luc-melenchon','dette-deficits'): [
 ("Services publics & ménages","beneficie","~80 Md€ de dépenses d'urgence financées"),
 ("Les plus riches","contribue","+100 Md€ de recettes « uniquement en faisant contribuer les plus riches »")],
('jean-luc-melenchon','education'): [
 ("Élèves & étudiants","beneficie","école globale, refondation du supérieur"),
 ("Parents de jeunes enfants","beneficie","service public de la petite enfance"),
 ("Adultes en illettrisme","beneficie","éradication à l'horizon 2027")],
('jean-luc-melenchon','emploi-chomage'): [
 ("Chômeurs de longue durée","beneficie","garantie d'emploi rémunéré au SMIC revalorisé (volontariat)"),
 ("Chômeurs","beneficie","assurance-chômage « protectrice » rétablie")],
('jean-luc-melenchon','environnement'): [
 ("Générations futures","beneficie","règle verte constitutionnelle, −65 % CO₂ en 2030"),
 ("Secteurs carbonés","contribue","planification écologique contraignante")],
('jean-luc-melenchon','immigration'): [
 ("Travailleurs & étudiants étrangers","beneficie","visas facilités, régularisations, carte de séjour 10 ans"),
 ("Réfugiés & déplacés climatiques","beneficie","statut de « détresse environnementale », AME rétablie")],
('jean-luc-melenchon','inegalites'): [
 ("Ménages modestes","beneficie","révolution fiscale au profit des plus modestes"),
 ("Finance & hauts revenus","contribue","taxe sur les transactions, contrôle des capitaux")],
('jean-luc-melenchon','institutions'): [
 ("Citoyens","beneficie","Assemblée constituante, 6e République")],
('jean-luc-melenchon','protection-sociale'): [
 ("Retraités","beneficie","retour à 60 ans/40 annuités, pensions ≥ SMIC, minimum vieillesse au seuil de pauvreté"),
 ("Malades","beneficie","« 100 % Sécu »"),
 ("Cotisants & employeurs","contribue","financement de la couverture intégrale")],
('jean-luc-melenchon','terrorisme'): [
 ("Forces de sécurité","beneficie","moyens humains plutôt que surveillance technologique"),
 ("Libertés publiques","beneficie","sortie de « l'état d'urgence permanent »")],
('marine-le-pen','crises-internationales'): [
 ("Armées","beneficie","budget défense porté à 55 Md€ en 2027"),
 ("Alliés (Allemagne, OTAN)","contribue","retrait du commandement intégré, coopérations rediscutées")],
('marine-le-pen','delinquance'): [
 ("Victimes","beneficie","peines planchers, présomption de légitime défense pour les forces de l'ordre"),
 ("Magistrats & prisons","beneficie","doublement des magistrats, 85 000 places"),
 ("Délinquants","contribue","suppression des réductions et aménagements de peine")],
('marine-le-pen','dette-deficits'): [
 ("Contribuables","beneficie","baisses de recettes ciblées (TVA, énergie)"),
 ("Agences & organismes publics","contribue","subventions réduites de 20 % (−7,7 Md€)"),
 ("Étrangers bénéficiaires de prestations","contribue","−6,1 Md€ sur les prestations sociales aux étrangers"),
 ("Patrimoines financiers","contribue","impôt sur les fortunes financières (~4 Md€)")],
('marine-le-pen','education'): [
 ("Élèves","beneficie","mission de transmission des savoirs restaurée")],
('marine-le-pen','emploi-chomage'): [
 ("Jeunes actifs (<30 ans)","beneficie","IR à 0, chèque-formation 200-300 € pour apprentis"),
 ("Apprentis & leurs employeurs","beneficie","chèque-formation mensuel"),
 ("Jeunes entrepreneurs","beneficie","IS exonéré 5 ans")],
('marine-le-pen','environnement'): [
 ("Filières nucléaire, hydro & hydrogène","beneficie","indépendance énergétique"),
 ("Filière éolienne","contribue","arrêt des nouveaux parcs, démantèlement progressif"),
 ("Consommateurs d'énergie","beneficie","sortie du marché européen de l'électricité (prix visés)")],
('marine-le-pen','immigration'): [
 ("Nationaux","beneficie","« priorité nationale » : prestations, logement, emploi réservés"),
 ("Immigrés & étrangers","contribue","accès restreint aux prestations sociales")],
('marine-le-pen','inegalites'): [
 ("Familles","beneficie","part fiscale dès le 2e enfant, prêt 0 % devenu subvention au 3e"),
 ("Mères isolées","beneficie","soutien doublé"),
 ("Familles modestes & classes moyennes","beneficie","héritage direct désimposé")],
('marine-le-pen','institutions'): [
 ("Citoyens","beneficie","RIC et proportionnelle")],
('marine-le-pen','protection-sociale'): [
 ("Retraités","beneficie","réindexation inflation, minimum vieillesse 1 000 €, 60 ans carrières précoces"),
 ("Malades & soignants","beneficie","plan d'urgence santé de 20 Md€")],
('marine-le-pen','terrorisme'): [
 ("Réseaux islamistes","contribue","éradication des idéologies et de leurs réseaux"),
 ("Citoyens","beneficie","priorité sécuritaire affichée")],
('raphael-glucksmann','crises-internationales'): [
 ("Défense européenne","beneficie","souveraineté industrielle, énergétique et militaire"),
 ("Défenseurs des droits humains","beneficie","lutte contre les ingérences, « puissance de paix »")],
('raphael-glucksmann','dette-deficits'): [
 ("Très hauts patrimoines","contribue","taxe « méga-héritages » (~15 Md€ annoncés)"),
 ("Bénéficiaires de la redistribution","beneficie","fiscalité au service de la solidarité")],
('raphael-glucksmann','education'): [
 ("Enseignants","beneficie","revalorisation des rémunérations"),
 ("Élèves","beneficie","moins d'élèves par classe en primaire, rénovation du bâti")],
('raphael-glucksmann','environnement'): [
 ("Ménages modestes","beneficie","transition protégeant d'abord les plus modestes"),
 ("Industries de demain","beneficie","investissements dans les filières vertes"),
 ("Générations futures","beneficie","justice climatique, biodiversité")],
('raphael-glucksmann','immigration'): [
 ("Citoyens","beneficie","convention citoyenne tirée au sort")],
('raphael-glucksmann','inegalites'): [
 ("Ménages modestes & territoires","beneficie","réduction des inégalités « entre territoires et générations »"),
 ("Femmes","beneficie","égalité femmes-hommes"),
 ("Hauts revenus & patrimoines","contribue","justice fiscale redistributive")],
('raphael-glucksmann','institutions'): [
 ("Citoyens & contre-pouvoirs","beneficie","participation démocratique, indépendance de la justice")],
('raphael-glucksmann','protection-sociale'): [
 ("Usagers des services publics","beneficie","santé, école, transports renforcés au plus près des territoires"),
 ("Territoires ruraux & éloignés","beneficie","accès équitable partout")],
}

def chips_html(pubs):
    chips = []
    for p, s, _det in pubs:
        if s == 'beneficie':
            chips.append(f'<span class="chip">{p}</span>')
        else:
            chips.append(f'<span class="chip contrib">pénalisés : {p.lower() if p[0].isupper() and not p.split()[0].endswith("s") and len(p.split())==1 else p}</span>')
    return '<div class="publics"><span class="lbl">Pour qui</span>' + ''.join(chips) + '</div>'

def fix_contrib_label(p):
    low = p[0].lower() + p[1:] if not p.isupper() else p
    return 'pénalisés : ' + low

# ── 1. JSON ──
n = 0
for (cid, theme), pubs in D.items():
    path = f'editorial/data/positions/{cid}/{theme}.json'
    d = json.load(open(path, encoding='utf-8'), object_pairs_hook=collections.OrderedDict)
    d['publics'] = [{"public": p, "sens": s, "fondement": "mesure", "detail": det} for p, s, det in pubs]
    json.dump(d, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    open(path, 'a', encoding='utf-8').write('\n')
    n += 1
print('JSON publics écrits :', n)

# ── 2. CSS sur les 11 pages ──
CSS = '''  /* ── Pour qui : publics impactés ── */
  .publics { display:flex; flex-wrap:wrap; gap:.3rem; align-items:center; font-size:.72rem; }
  .publics .lbl { font-size:.62rem; font-weight:700; letter-spacing:.06em; text-transform:uppercase; color:var(--encre-2); }
  .chip { background:var(--ref-fond); border:1px solid var(--filet); border-radius:999px; padding:.1rem .55rem; }
  .chip.contrib { background:transparent; border-style:dashed; color:var(--encre-2); }
  .chip.ext { border-color:var(--accent); }
  .publics a.src-analyse { color:var(--accent); font-size:.68rem; text-decoration:none; }
  .publics a.src-analyse:hover { text-decoration:underline; }
'''
ORDER = ['dominique-de-villepin','marine-le-pen','jean-luc-melenchon','edouard-philippe','raphael-glucksmann','gabriel-attal']

for f in glob.glob('site/maquettes/theme-*.html'):
    if 'pouvoir-achat' in f:
        continue
    theme = re.search(r'theme-([a-z-]+)\.html', f).group(1)
    s = open(f, encoding='utf-8').read()
    if '.publics {' not in s:
        s = s.replace('</style>', CSS + '</style>', 1)
    # insère les chips : pour chaque carte dans l'ordre, avant </div> qui ferme .corps
    arts = s.split('<article class="carte')
    out = [arts[0]]
    idx = 0
    for part in arts[1:]:
        seg = '<article class="carte' + part
        cid = ORDER[idx] if idx < len(ORDER) else None
        idx += 1
        pubs = D.get((cid, theme))
        if pubs:
            chips = []
            for p, se, _d in pubs:
                if se == 'beneficie':
                    chips.append(f'<span class="chip">{p}</span>')
                else:
                    chips.append(f'<span class="chip contrib">{fix_contrib_label(p)}</span>')
            block = '<div class="publics"><span class="lbl">Pour qui</span>' + ''.join(chips) + '</div>'
            # insère avant le </div> qui précède <div class="source">
            seg = re.sub(r'(\n\s*</div>\s*\n\s*<div class="source">)', '\n          ' + block + r'\1', seg, count=1)
        out.append(seg)
    s = ''.join(out)
    open(f, 'w', encoding='utf-8').write(s)
    print('MAJ', f)
