# Brainstorming — Site Web Présidentielle 2027
**Sessions #1 & #2 — 16-17 octobre 2026**
**Mode : Divergent | Techniques : Question Storming (principal) + pivots domaine**

---

## Sujet Central

Concevoir un site web qui présente, de façon synthétique et accessible, le programme des **5 candidats les plus probables** à l'élection présidentielle française de 2027 — toutes tendances politiques confondues.

---

## Décisions & Principes Actés

### Périmètre
- Limité aux **5 candidats** les plus crédités de passer au second tour (tous bords politiques)
- **+1 candidat de RÉFÉRENCE : Dominique de Villepin** — 6e place fixe, référentiel comparatif transversal sur chaque thème (exception éditoriale déclarée, Protocole §2.6)
- Thèmes couvrant les préoccupations **nationales ET internationales**

### Navigation
- **Point d'entrée :** Liste des thématiques → comparaison des 5 candidats sur la thématique choisie
- **Toujours accessible :** Fiche candidat complète (études, militantisme, expériences professionnelles, parcours politique)
- **Mode Face à Face :** comparaison des 5 candidats en miroir, thème par thème

### Structure des Thèmes
- **2 niveaux :** Domaines (Économie, Société, International, Environnement, Institutions…) → Sous-thèmes précis
- **Dynamique :** les thèmes évoluent avec la campagne et l'actualité
- **Gouvernance automatique** basée sur les préoccupations des Français à l'instant T

### Principes Éditoriaux
- **Neutralité absolue** dans le choix des mots et la formulation
- **Le citoyen juge** — aucun qualificatif éditorial sur les changements de position
- **Sources institutionnelles uniquement** : IFOP, BVA, OpinionWay, Harris Interactive, Elabe
- **Lien source primaire obligatoire** : toute position renvoie au site officiel du candidat ou de son parti (programme, communiqué, discours) — même règle dans la newsletter
- **Transparence sur la méthode** : comment on choisit les thèmes, comment on valide les sources

### Section "Actes Passés"
- Nom de section retenu : **"Actes passés"**
- Pour chaque thème : position actuelle vs bilan documenté si le candidat a été en poste
- Candidats sans expérience gouvernementale : actes concrets dans leur domaine d'origine
- Changements de position : **relevés avec neutralité**, date + ancienne/nouvelle position sourcées

### Design
- **Responsive mobile-first** : priorité au format dédié aux réseaux sociaux (vertical, cartes partageables, stories 9:16)
- **Neutralité chromatique** : aucune couleur structurante à connotation partisane, couleurs réservées à la donnée

### Pipeline Technique
```
Scraping RSS hebdo → Mise à jour contenu → Build auto → Git commit/push → Déploiement Cloud
```

---

## Idées Générées — Session #1 (48)

### Axe 1 — Contenu & Éditorial

**[Idée #1]** : Thèmes manquants
_Concept_ : Que faire des sujets qu'aucun candidat n'aborde mais qui préoccupent les citoyens ? Les afficher explicitement comme "angle mort du débat politique".
_Nouveauté_ : Révèle les angles morts collectifs du débat politique.

**[Idée #2]** : L'Accord Invisible
_Concept_ : Identifier et afficher les thèmes sur lesquels tous les candidats convergent sans le dire ouvertement.
_Nouveauté_ : Montre ce que la politique cache autant que ce qu'elle expose.

**[Idée #3]** : La Mémoire du Candidat
_Concept_ : Intégrer ce qu'un candidat a *déjà fait* quand il était au pouvoir vs ce qu'il promet aujourd'hui. Dimension temporelle absente des comparateurs classiques.
_Nouveauté_ : Ajoute une dimension historique vérifiable à chaque promesse.

**[Idée #17]** : Les Thèmes en Deux Niveaux
_Concept_ : Niveau 1 = grands domaines. Niveau 2 = sous-thèmes précis. L'utilisateur choisit sa profondeur de lecture.
_Nouveauté_ : Accessible aux non-initiés ET satisfaisant pour les citoyens éclairés.

**[Idée #18]** : Les Thèmes "Surprise"
_Concept_ : Catégorie *"Ce dont on ne parle pas assez"* — IA & travail, dette générationnelle, santé mentale, crise démographique — avec les positions des candidats sur ces sujets émergents.
_Nouveauté_ : Longueur d'avance éditoriale sur tous les comparateurs existants.

---

### Axe 2 — Actes Passés & Mémoire Civique

**[Idée #4]** : Le Baromètre Promesse / Réalité ⭐
_Concept_ : Pour chaque thème, afficher côte à côte : "Ce qu'il promet aujourd'hui" / "Ce qu'il a fait quand il était en poste". Indicateur visuel simple (vert/orange/rouge) montrant la cohérence historique.
_Nouveauté_ : Transforme la promesse politique en donnée vérifiable, pas en opinion.

**[Idée #5]** : La Carte Blanche Équitable
_Concept_ : Pour les candidats sans passé gouvernemental, afficher leurs actes concrets dans leur domaine d'origine comme proxy de cohérence.
_Nouveauté_ : Évite l'asymétrie entre "insiders" et "outsiders" politiques.

**[Idée #6]** : Le Fil du Temps Thématique ⭐
_Concept_ : Sur chaque thème, une frise chronologique montre l'évolution des positions du candidat depuis ses débuts — avec citations sourcées à chaque pivot.
_Nouveauté_ : Révèle si un candidat a toujours cru en sa promesse ou si c'est une adaptation électorale.

**[Idée #7]** : Le Score de Cohérence
_Concept_ : Score calculé automatiquement (via recoupement de sources) entre positions passées et programme actuel. Mesure de constance, pas un jugement.
_Nouveauté_ : Objectivise ce que les citoyens ressentent intuitivement sans pouvoir le prouver.

**[Idée #8]** : Le Pivot Documenté
_Concept_ : Carte "Évolution de position" : date du changement, ancienne position (citation sourcée), nouvelle position (citation sourcée), contexte factuel neutre. Aucun qualificatif.
_Nouveauté_ : Neutralité froide — les faits seuls, le citoyen tire ses propres conclusions.

**[Idée #9]** : Le Vide comme Information
_Concept_ : Sur un thème où un candidat n'a aucun bilan, afficher explicitement "Aucun acte passé documenté sur ce thème".
_Nouveauté_ : L'absence de données devient une donnée traitée avec la même rigueur.

**[Idée #10]** : La Promesse Datée
_Concept_ : Chaque promesse de campagne passée est horodatée. Après l'élection, un statut s'ajoute : Tenu / Partiellement tenu / Non tenu / Abandonné.
_Nouveauté_ : Le site devient un outil de mémoire civique qui vit après l'élection.

---

### Axe 3 — UX & Design de l'Information

**[Idée #13]** : La Page Thématique Structurée
_Concept_ : Chaque thème affiche les 5 candidats en colonnes : position synthétisée (2-3 phrases), mesure phare promise, bilan passé si applicable, score de cohérence. Tout visible sans scroll.
_Nouveauté_ : Comparaison immédiate, aucune recherche nécessaire.

**[Idée #14]** : La Fiche Candidat comme Carte d'Identité Politique
_Concept_ : Fiche permanente : Parcours humain → Parcours militant → Expériences pro → Mandats exercés → Positions historiques clés. Accessible depuis n'importe quelle page en un clic.
_Nouveauté_ : Le citoyen comprend *qui est* le candidat avant de juger *ce qu'il propose*.

**[Idée #15]** : L'Index des Thèmes Visuels
_Concept_ : La liste des thèmes est une grille visuelle avec icône + titre + indicateur de divergence entre candidats (fort / moyen / faible). L'utilisateur sait avant de cliquer où sont les vrais débats.
_Nouveauté_ : Guide l'attention vers les zones de friction politique réelle.

**[Idée #16]** : Le Fil Rouge Candidat
_Concept_ : Depuis la fiche candidat, accès direct à "Sa position sur chaque thème". Parcours inversé : on part du candidat et on découvre ses thèmes un par un.
_Nouveauté_ : Satisfait les visiteurs qui pensent par thème ET ceux qui ont déjà un candidat en tête.

---

### Axe 4 — Gouvernance des Thèmes

**[Idée #19]** : Le Thème Émergent Signalé
_Concept_ : Nouveau thème ajouté → badge "Nouveau" + date d'ajout. Candidats sans réponse → "Position attendue — dernière mise à jour : JJ/MM".
_Nouveauté_ : Transforme l'absence de réponse en pression transparente sur le candidat.

**[Idée #20]** : Le Journal des Mises à Jour
_Concept_ : Page dédiée listant toutes les modifications récentes : nouveau thème, position mise à jour, source ajoutée, pivot documenté. Horodatée et sourcée.
_Nouveauté_ : Garantit la traçabilité éditoriale complète.

**[Idée #21]** : La Gouvernance des Thèmes ⭐
_Concept_ : Protocole automatique basé sur critères objectifs — les thèmes entrent et sortent de la liste selon les préoccupations des Français à l'instant T, mesurées par les instituts de sondage reconnus.
_Nouveauté_ : Sélection mécanique et transparente — personne ne peut accuser un éditeur humain de favoritisme.

**[Idée #22]** : L'Alerte Position Modifiée
_Concept_ : Si un candidat change de position en cours de campagne, notification visuelle sur la page thème : "Position mise à jour le JJ/MM — voir l'évolution". Lié au Fil du Temps.
_Nouveauté_ : Le site réagit à la campagne en direct.

**[Idée #25]** : Les 3 Critères d'Entrée d'un Thème
_Concept_ : Un thème intègre la liste s'il remplit ≥2 critères sur 3 : (1) cité dans +3 grands médias nationaux cette semaine, (2) présent dans ≥1 programme officiel de candidat, (3) dans le top 10 des préoccupations des sondages institutionnels récents.
_Nouveauté_ : Critères publics et mécaniques — zéro subjectivité.

**[Idée #26]** : Le Seuil de Sortie d'un Thème
_Concept_ : Un thème peut sortir de la liste active s'il disparaît de l'agenda pendant X semaines — mais passe en "Archive", jamais supprimé.
_Nouveauté_ : La mémoire du site est préservée même quand l'actualité tourne.

**[Idée #27]** : La Page "Comment nous choisissons les thèmes"
_Concept_ : Page éditoriale publique et permanente expliquant le protocole de sélection, les critères, les sources, la fréquence de révision. En langage simple.
_Nouveauté_ : La transparence sur la *méthode* est aussi importante que la transparence sur le *contenu*.

**[Idée #28]** : La Charte Éditoriale Publique
_Concept_ : Charte écrite et publique — principes de neutralité, gestion des conflits d'intérêt, procédure en cas de sources contradictoires. Accessible depuis le footer.
_Nouveauté_ : Crédibilité institutionnelle sans nécessiter une équipe réelle.

**[Idée #29]** : La Suggestion Citoyenne Encadrée
_Concept_ : Formulaire simple pour proposer un thème avec justification. Chaque proposition évaluée publiquement selon les 3 critères. Refus ou acceptation documentés.
_Nouveauté_ : Les citoyens deviennent co-éditeurs sans perdre le contrôle éditorial.

---

### Axe 5 — Sources & Validation

**[Idée #30]** : Le Baromètre des Préoccupations en Temps Réel
_Concept_ : Module en page d'accueil affichant le Top 5 des préoccupations des Français du moment, issu du dernier sondage institutionnel disponible. Ce classement pilote l'ordre d'affichage des thèmes.
_Nouveauté_ : Le site se réorganise visuellement selon l'humeur réelle du pays.

**[Idée #31]** : La Source Unique par Institut
_Concept_ : Règle stricte : 1 source = 1 institut identifié + date de publication + lien vers l'étude originale. Aucun sondage agrégé ou anonyme. Instituts éligibles listés publiquement : IFOP, BVA, OpinionWay, Harris Interactive, Elabe.
_Nouveauté_ : Chaque chiffre est traçable à la source primaire.

**[Idée #32]** : La Fréquence de Révision Automatique
_Concept_ : Cycle de révision hebdomadaire (chaque lundi) — les critères des thèmes sont réévalués selon les derniers sondages publiés. Thèmes montants montent dans la liste, thèmes en baisse glissent vers l'archive.
_Nouveauté_ : Le site a le même souffle que la campagne (6 mois).

**[Idée #33]** : L'Indicateur de Tendance par Thème
_Concept_ : À côté de chaque thème, une flèche visuelle : ↑ montant / → stable / ↓ en baisse dans les préoccupations des Français. Basé sur la variation entre les 2 derniers sondages disponibles.
_Nouveauté_ : Le citoyen perçoit en un clin d'œil que les priorités collectives bougent.

**[Idée #34]** : Le Label "Vérifié par Sources Institutionnelles"
_Concept_ : Chaque thème actif porte un badge discret indiquant les instituts qui l'ont mesuré + la date. Info-bulle affichant le verbatim exact de la question posée dans le sondage.
_Nouveauté_ : La confiance se construit sur la transparence du *comment on sait*.

**[Idée #35]** : Le Mur des Sources
_Concept_ : Page dédiée listant toutes les sources utilisées : sondages, programmes officiels, discours, interviews vérifiées. Mise à jour en continu. Triable par date, thème, candidat.
_Nouveauté_ : Le site devient lui-même une ressource secondaire pour journalistes et citoyens curieux.

---

### Axe 6 — Pipeline Technique & Automatisation

**[Idée #36]** : Le Scraping Légal par RSS/Veille
_Concept_ : Script de veille (RSS + scraping ciblé) détectant les nouvelles publications des instituts chaque semaine. Alerte à l'éditeur pour validation avant mise en ligne.
_Nouveauté_ : Semi-automatique — la machine détecte, l'humain valide.

**[Idée #37]** : La Base de Données Sondages en JSON
_Concept_ : Chaque sondage intégré stocké dans un fichier JSON : `{ institut, date, question, résultats[], thèmes_associés[], url_source }`. Le site le lit et s'affiche automatiquement.
_Nouveauté_ : Structure légère, versionnable sur Git, auditable, sans base de données complexe.

**[Idée #38]** : Airtable/Notion comme CMS Éditorial
_Concept_ : L'éditeur gère tout depuis un tableau Airtable. Le site appelle l'API en temps réel. Mise à jour en 30 secondes sans toucher au code.
_Nouveauté_ : Sépare complètement le travail éditorial du travail technique.

**[Idée #39]** : Le Workflow de Mise à Jour Hebdomadaire
_Concept_ : Protocole fixe chaque lundi : consultation des publications des 5 instituts → saisie des nouvelles données → recalcul automatique des tendances → publication. Durée estimée : 1h/semaine.
_Nouveauté_ : Maintenance légère et prévisible.

**[Idée #40]** : L'Alerte Position Candidat via Veille Médiatique
_Concept_ : Google Alerts / Feedly configurés sur chaque candidat × chaque thème. Nouvelle déclaration détectée → notification à l'éditeur pour évaluer si mise à jour nécessaire.
_Nouveauté_ : Le site réagit aux événements de campagne en moins de 24h.

**[Idée #41]** : Stack Statique Moderne — Next.js ou Astro
_Concept_ : Site statique généré (Next.js ou Astro) — contenu dans des fichiers Markdown/JSON versionnés sur Git. Déploiement automatique à chaque commit via Vercel ou Netlify. Temps de chargement < 1s, coût quasi nul.
_Nouveauté_ : Pas de base de données, pas de serveur — robuste pendant un pic de trafic électoral.

**[Idée #42]** : Le Déploiement "One Click"
_Concept_ : Chaque mise à jour éditoriale déclenche automatiquement un rebuild via GitHub Actions. L'éditeur commit → le site est live en 2 minutes.
_Nouveauté_ : Pipeline technique invisible pour l'éditeur.

**[Idée #43]** : La Sauvegarde Historique Automatique
_Concept_ : Chaque version du site archivée via Git — on peut remonter à l'état exact du site n'importe quel jour de la campagne.
_Nouveauté_ : Le versioning Git devient un outil de transparence civique.

**[Idée #44]** : Le Pipeline CI/CD Éditorial ⭐
_Concept_ : Script Python en cron job hebdomadaire : scrape les flux RSS des 5 instituts → détecte nouveaux sondages → met à jour les fichiers JSON → commit Git horodaté automatique → déclenche rebuild Vercel/Netlify via webhook.
_Nouveauté_ : Cycle complet détection → données → site live sans intervention humaine.

**[Idée #45]** : Le Commit Sémantique Automatique
_Concept_ : Convention stricte : `[AUTO] màj-sondages 2027-W42 | +2 thèmes | 3 positions candidats modifiées`. Le changelog du site est généré automatiquement depuis l'historique Git.
_Nouveauté_ : L'historique Git devient le journal éditorial public.

**[Idée #46]** : Le Filet de Sécurité Humain
_Concept_ : Avant le push final, le script génère un rapport de diff envoyé par email/Slack à l'éditeur. Déploiement automatique si pas de réponse sous 2h.
_Nouveauté_ : L'automatisation ne court-circuite jamais le jugement humain.

**[Idée #47]** : L'Environnement Preview Automatique
_Concept_ : Chaque mise à jour génère automatiquement un lien preview (Vercel/Netlify natif) — l'éditeur vérifie visuellement avant que ce soit live publiquement.
_Nouveauté_ : Détecte les anomalies avant qu'un citoyen les voie.

**[Idée #48]** : Le Cloud Résilient
_Concept_ : Déploiement sur Vercel ou Netlify (CDN mondial, 99.99% uptime) — critique pour un site politique qui peut recevoir des pics de trafic massifs lors d'un débat ou d'une annonce majeure.
_Nouveauté_ : Aucun coût fixe serveur — scale automatiquement selon le trafic.

**[Idée #49]** : Le Dashboard de Santé du Site
_Concept_ : Page admin privée affichant : date du dernier scraping réussi, nombre de sondages intégrés, statut du dernier déploiement, alertes si une source n'a pas été mise à jour depuis +14 jours.
_Nouveauté_ : L'éditeur connaît l'état du pipeline en 10 secondes.

**[Idée #50]** : L'Alerte Anomalie Automatique
_Concept_ : Si le scraping détecte une incohérence (position d'un candidat change radicalement en une semaine), alerte spéciale avant toute mise en ligne — vérification humaine obligatoire.
_Nouveauté_ : Le pipeline est intelligent — il sait quand s'arrêter.

---

## Architecture Conceptuelle du Site

```
Page d'accueil
├── Baromètre préoccupations (Top 5 sondages temps réel)
├── Index des Thèmes (grille visuelle avec indicateur de divergence)
│   ├── Thème actif → Comparaison 5 candidats + colonne Référence (Villepin)
│   │   ├── Position actuelle (2-3 phrases, sourcée)
│   │   ├── Mesure phare promise
│   │   ├── Actes passés (Baromètre Promesse/Réalité)
│   │   ├── Fil du Temps (frise chronologique des positions)
│   │   └── Score de cohérence
│   └── Thème archivé (accessible, non actif)
├── Mode Face à Face (2 candidats en miroir)
├── Fiches Candidats
│   ├── Carte d'identité politique (parcours complet)
│   └── Toutes ses positions par thème
├── Mur des Sources
├── Journal des Mises à Jour
└── Page Gouvernance Éditoriale
```

---

## Pipeline Technique Acté

```
[Cron Job lundi matin]
        ↓
[Script Python — Scraping RSS / 5 instituts]
        ↓
[Détection nouveaux sondages + nouvelles déclarations candidats]
        ↓
[Mise à jour fichiers JSON/Markdown]
        ↓
[Rapport de diff → email/Slack éditeur (2h pour bloquer)]
        ↓
[Commit Git sémantique automatique]
[ex: AUTO màj-sondages 2027-W42 | +2 thèmes | 3 positions modifiées]
        ↓
[GitHub Actions → Build Next.js/Astro]
        ↓
[Preview URL automatique → vérification visuelle]
        ↓
[Déploiement Vercel/Netlify (CDN mondial)]
```

**Stack retenu :**
- **Framework :** Next.js ou Astro (site statique généré)
- **Données :** Fichiers JSON + Markdown versionnés sur Git
- **CMS éditorial :** Airtable (optionnel, pour éditeur non-technique)
- **CI/CD :** GitHub Actions
- **Hosting :** Vercel ou Netlify
- **Veille :** RSS instituts + sites officiels candidats/partis + Google Alerts / Feedly
- **Instituts sondages :** IFOP, BVA, OpinionWay, Harris Interactive, Elabe

---

## Idées Prioritaires (⭐)

| # | Idée | Impact | Différenciation |
|---|------|--------|-----------------|
| #4 | Baromètre Promesse / Réalité | Très élevé | Unique sur le marché |
| #6 | Fil du Temps Thématique | Très élevé | Mémoire civique long terme |
| #21 | Gouvernance Automatique des Thèmes | Élevé | Transparence et confiance |
| #44 | Pipeline CI/CD Éditorial | Élevé | Viabilité opérationnelle |
| #64 | Newsletter "Le Fil de la Campagne" | Élevé | Zéro coût éditorial (auto-générée depuis Git) |
| #74 | Veille des Sites Officiels | Élevé | Pipeline bidirectionnel instituts + candidats |

---

## Idées Générées — Session #2 (25)

### Axe 7 — Cross-Pollination (mécaniques importées)

**[Idée #51]** : L'Onglet "Historique" façon Wikipedia
_Concept_ : Chaque page candidat/thème expose publiquement son historique de révision (date, nature de la modif, source) — alimenté par l'historique Git.
_Nouveauté_ : La transparence Wikipedia appliquée à l'information électorale.

**[Idée #52]** : Le Badge "Source Requise"
_Concept_ : Équivalent du `[citation needed]` — une position non sourcée affiche un badge visible jusqu'au rattachement d'une source primaire.
_Nouveauté_ : Le site assume publiquement ses zones grises au lieu de les cacher.

**[Idée #53]** : Le Diff Politique
_Concept_ : Position modifiée affichée façon diff GitHub — ancienne formulation barrée en rouge, nouvelle en vert, horodatée.
_Nouveauté_ : Rend le pivot politique aussi lisible qu'une modification de code.

**[Idée #54]** : La Mesure Chiffrée
_Concept_ : Badge objectif par promesse : `Chiffrée` (coût/délai annoncé) vs `Orientée` (intention sans engagement mesurable). Pas de jugement vrai/faux façon PolitiFact.
_Nouveauté_ : Distingue promesse concrète et déclaration d'intention — sans noter le candidat.

**[Idée #55]** : Le Parcours Citoyen façon Duolingo
_Concept_ : Progression sauvegardée localement : "4/12 thèmes explorés", checklist de préparation au vote.
_Nouveauté_ : Gamification du devoir civique.

**[Idée #56]** : Le Paysage en Un Coup d'Œil
_Concept_ : Matrice 5 candidats × thèmes actifs, cellules colorées selon le niveau de divergence (dataviz façon Le Monde).
_Nouveauté_ : Toute la géographie du débat tenue dans un seul écran.

**[Idée #57]** : La Heatmap d'Activité Candidat
_Concept_ : Calendrier type graphe de contributions GitHub — fréquence des prises de position publiques par thème. Un candidat silencieux se voit visuellement.
_Nouveauté_ : L'intensité médiatique devient donnée objective, pas impression.

**[Idée #58]** : La Timeline Dataviz des Sondages
_Concept_ : Courbes temporelles interactives des préoccupations des Français — construites sur les JSON versionnés.
_Nouveauté_ : Le citoyen voit la campagne respirer semaine après semaine.

**[Idée #59]** : Le Bouton "Cette info est-elle à jour ?"
_Concept_ : Signalement citoyen (façon Waze) sur chaque fiche position, avec proposition de source — file de modération pour l'éditeur.
_Nouveauté_ : Vigilance distribuée contre l'obsolescence.

**[Idée #60]** : L'API Publique des Positions
_Concept_ : Les fichiers JSON du site exposés en lecture publique (repo GitHub public) — réutilisables par journalistes, chercheurs, développeurs.
_Nouveauté_ : Le site devient une infrastructure civique open data.

---

### Axe 8 — Dimension Citoyenne & Diffusion

**[Idée #61]** : Le Maillage SEO Programmatique
_Concept_ : ~60 pages statiques `candidat × thème`, chacune répondant à une requête réelle ("position de X sur la santé").
_Nouveauté_ : L'architecture du site devient machine de référencement longue traîne.

**[Idée #62]** : La Carte Partageable Open Graph
_Concept_ : Image sociale auto-générée par page thème : titre + 5 candidats + indicateur de divergence.
_Nouveauté_ : Le contenu neutre devient partageable sans devenir partisan.

**[Idée #63]** : Le Widget Embarquable
_Concept_ : Composant iframe (Baromètre des Préoccupations, comparaison thème) intégrable gratuitement par blogs, médias locaux, associations.
_Nouveauté_ : La donnée civique voyage dans l'écosystème web — le citoyen n'a pas besoin de venir.

**[Idée #64]** : La Newsletter "Le Fil de la Campagne" ⭐
_Concept_ : Résumé hebdo auto-généré depuis les commits Git : thèmes montants, pivots documentés, nouveaux sondages, positions attendues. **Retenue par l'utilisateur.**
_Nouveauté_ : La même automatisation qui met à jour le site alimente la newsletter — zéro travail éditorial.

**[Idée #65]** : Le Kit Pédagogique EMI
_Concept_ : Module clé en main pour professeurs d'EMI (lycée) : activité de comparaison, exercice "repérer un changement de position".
_Nouveauté_ : Capte les premiers votants (17-18 ans) via leurs enseignants.

**[Idée #66]** : Le Label de Méthode Validée
_Concept_ : Protocole soumis à relecture externe (ONG transparence, sociologie électorale, asso journalisme de données) — validation = badge public.
_Nouveauté_ : La crédibilité s'obtient par audit externe, pas par auto-proclamation.

**[Idée #67]** : Le Partenariat Rédactions Locales
_Concept_ : Données structurées + widgets fournis gratuitement à la presse régionale contre citation de source.
_Nouveauté_ : Mutualisation : eux gagnent une dataviz, le site gagne une distribution territoriale.

**[Idée #68]** : Le Réflexe Débat Télé
_Concept_ : Site optimisé "second écran" pendant les débats — recherche instantanée d'une position passée citée en direct.
_Nouveauté_ : Positionné sur les moments de pic d'attention civique.

**[Idée #69]** : Le Communiqué à Chaque Jalon
_Concept_ : Jalons publics automatisés pour la presse : lancement, 100e source intégrée, premier pivot documenté, mi-campagne.
_Nouveauté_ : La vie interne du projet (déjà tracée par Git) devient fil narratif médiatique.

**[Idée #70]** : Le Mode "3 Minutes avant de Voter"
_Concept_ : Parcours ultra-condensé mobile-first : top 3 préoccupations → 1 phrase par candidat par thème → lien vers le détail.
_Nouveauté_ : Capte l'électeur quand son intention de s'informer est maximale (J-1).

---

### Axe 9 — Source Primaire (construit sur #64 + retour utilisateur)

**[Idée #71]** : Le Lien Source Officielle Permanent
_Concept_ : Règle absolue — toute position affichée est adossée à un lien direct vers le site officiel du candidat ou de son parti.
_Nouveauté_ : Le site comme aiguillage vers la source primaire, jamais un substitut.

**[Idée #72]** : La Newsletter aux Liens Primaires
_Concept_ : Chaque item de "Le Fil de la Campagne" inclut le lien direct vers la page officielle du candidat/parti.
_Nouveauté_ : La newsletter est un portail vers les sources, pas un cul-de-sac.

**[Idée #73]** : L'Archive des Programmes (Wayback)
_Concept_ : Chaque page source archivée automatiquement via web.archive.org à l'intégration — double lien : site live + archive horodatée.
_Nouveauté_ : La source ne devient jamais un lien mort — la mémoire survit à la fin de campagne.

**[Idée #74]** : La Veille des Sites Officiels ⭐
_Concept_ : Le scraper hebdo surveille aussi les pages programme des 5 candidats et de leurs partis — modification détectée → alerte → Fil du Temps + Alerte Position Modifiée + newsletter.
_Nouveauté_ : Pipeline bidirectionnel — il écoute les instituts ET les candidats.

**[Idée #75]** : Le Bandeau "Programme Officiel"
_Concept_ : Encart fixe par fiche candidat : programme PDF complet + site de campagne + site du parti + date de dernière vérification du lien.
_Nouveauté_ : Ancrage institutionnel permanent — la synthèse se présente comme un résumé.

---

### Axe 10 — Modèle de Données (draft concret : `data-model-draft.jsonc`)

**[Idée #76]** : La Position Canonique
_Concept_ : Schéma strict et unique par position `candidat × thème` : `{synthèse, mesure_phare, type, statut, source{url_live, url_archive, date_vérif, verbatim}}`.
_Nouveauté_ : La rigueur éditoriale garantie par la structure — impossible de publier sans source.

**[Idée #77]** : Un Fichier = Une Cellule
_Concept_ : `positions/{candidat}/{thème}.json` — un fichier par couple. Diffs Git chirurgicaux.
_Nouveauté_ : Le versionnement granulaire tombe gratuitement de l'arborescence.

**[Idée #78]** : L'Enum de Statut, pas le Vide
_Concept_ : `statut` ∈ `{sourcee, non_sourcee, attendue, contradictoire}` — le fichier existe toujours, son statut dit la vérité.
_Nouveauté_ : Concrétise #9 (vide = information) et #52 (badge source requise) au niveau données.

**[Idée #79]** : Le Triple Ancrage Source
_Concept_ : Toute source = `url_live` + `url_archive` + `date_verification` obligatoires.
_Nouveauté_ : Implémente #71/#73 comme invariant de données, pas promesse.

**[Idée #80]** : Le Fil du Temps est une Donnée, pas une UI
_Concept_ : `fil_du_temps[]` versionné dans le fichier position — alimente Diff Politique (#53), Alerte Maj (#22), newsletter (#64).
_Nouveauté_ : Une source de vérité, trois features.

**[Idée #81]** : Les IDs Stables comme Colonne Vertébrale
_Concept_ : `candidat_id`/`theme_id` = slugs immuables pilotant URLs SEO (#61) et jointures entre fichiers.
_Nouveauté_ : Le nommage devient contrat contenu/SEO/code — jamais renommé.

**[Idée #82]** : Le Schéma Sondage Normalisé
_Concept_ : Résultats pointant vers `theme_id` → recalcul automatique tendances et ranking.
_Nouveauté_ : Le sondage est de la donnée jointe au graphe de thèmes, pas du texte.

**[Idée #83]** : Le Registre Candidat Extensible
_Concept_ : `statut` ∈ `{pressenti, declare, retire, remplace}` — anticipe retrait et remplacement dès le schéma.
_Nouveauté_ : Le cas limite traité par l'enum, pas par un hack le jour J.

**[Idée #84]** : Le Changelog Piloté par les Données
_Concept_ : `maj_le` + `commit_ref` sur chaque fichier → Journal des MàJ (#20), Historique (#51), newsletter (#64) générés sans ressaisie.
_Nouveauté_ : La traçabilité est une requête sur les données.

**[Idée #85]** : Le Contrat de Schéma Versionné
_Concept_ : JSON Schema `schema/v1/` validé en CI — donnée mal formée = build qui échoue avant publication.
_Nouveauté_ : Le pipeline #44 devient auto-protégé.

---

### Axe 11 — Cas Limites & Scénarios de Crise

**[Idée #86]** : Le Sixième Homme
_Concept_ : Entrée/sortie du top 5 gouvernée mécaniquement (moyenne intention de vote sur 3 derniers sondages institutionnels) — même protocole que les thèmes (#21). Entrée = fichiers en `attendue`, sortie = archive jamais supprimée.
_Nouveauté_ : La composition du top 5 elle-même est gouvernée par la donnée, pas par l'éditeur.

**[Idée #87]** : Le Mode Second Tour
_Concept_ : Bascule planifiée post-1er tour : 3 éliminés en archive visible, 2 finalistes en Face à Face géant comme page d'accueil.
_Nouveauté_ : Deux vies prévues dès la conception — pas de refonte paniquée le soir du 1er tour.

**[Idée #88]** : La Source Contredite Affichée
_Concept_ : Écart > X points entre instituts sur une même mesure → affichage des deux résultats côte à côte + verbatims des questions. Badge "Sources divergentes".
_Nouveauté_ : La contradiction devient pédagogie sur la mesure d'opinion.

**[Idée #89]** : Le Droit de Réponse Candidat
_Concept_ : Bouton discret par position pour que l'équipe de campagne conteste une synthèse + propose sa source. Contestation ET correction tracées au Journal (#20).
_Nouveauté_ : Risque juridique transformé en mécanisme de confiance — les campagnes relectrices.

**[Idée #90]** : Le Lien Mort Surveillé
_Concept_ : Ping hebdo des `url_live` → 404 détecté = bascule auto sur `url_archive` + badge "source archivée" + alerte éditeur.
_Nouveauté_ : Jamais de lien cassé visible — le triple ancrage (#79) absorbe ses propres défaillances.

**[Idée #91]** : L'Erreur de Scraping Auto-Réparée
_Concept_ : Donnée aberrante rejetée par la validation CI (#85) → cellule garde sa dernière version valide, statut `attendue`, alerte éditeur.
_Nouveauté_ : Fail-safe — mieux vaut "position attendue" qu'une position fausse.

**[Idée #92]** : Le Sondage Rétracté
_Concept_ : Institut qui retire une publication → `statut: retracte` + lien démenti → recalcul des thèmes + correction publique au Journal.
_Nouveauté_ : Le site corrige avec la même transparence qu'il publie.

**[Idée #93]** : Le Thème Fantôme
_Concept_ : Thème remplissant les critères mais zéro position candidat → publié avec 5 cellules `attendue` — le trou dans la matrice devient l'info.
_Nouveauté_ : L'angle mort collectif (#1) devient une page entière affichable.

**[Idée #94]** : Le Mode Après l'Élection
_Concept_ : Bascule post-2nd tour vers "mode mémoire" — Promesse Datée (#10) prend le relais (Tenu / Partiellement / Non tenu), pipeline ralenti pour suivre le mandat.
_Nouveauté_ : Le site devient outil de suivi du mandat — la mémoire civique prolongée.

**[Idée #95]** : Le Protocole Gel
_Concept_ : Crise majeure (attentat, élection reportée) → bouton gel : bandeau neutre, pipeline en pause manuelle, aucune publication auto sans dégel éditeur.
_Nouveauté_ : L'automatisation a un arrêt d'urgence — la machine s'arrête, l'humain décide.

---

### Axe 12 — Design Visuel & Format Social

**[Idée #96]** : Le Design 360px d'Abord
_Concept_ : Chaque page dessinée pour mobile en premier — le desktop est l'extension, pas l'inverse.
_Nouveauté_ : Le mobile est le format natif du site — la majorité des visites viendra de liens partagés.

**[Idée #97]** : La Colonne Éclatée
_Concept_ : La comparaison 5 colonnes devient sur mobile une pile de cartes swipeables (feuilleter les candidats ou swiper les thèmes).
_Nouveauté_ : La comparaison dense survit au format vertical — le geste remplace le tableau.

**[Idée #98]** : La Story Auto-Générée ⭐
_Concept_ : Cartes 9:16 produites chaque semaine par le pipeline depuis les JSON : "Top 5 préoccupations", "Pivot documenté de la semaine", "Thème le plus clivant".
_Nouveauté_ : Le site produit sa propre matière sociale — zéro travail de community manager.

**[Idée #99]** : La Neutralité Chromatique
_Concept_ : Palette départisane — aucune couleur structurante à connotation politique (ni rouge, bleu, jaune, vert dominant). Base neutre ardoise/crème.
_Nouveauté_ : La neutralité est physiquement visible — aucun bord déductible de la page.

**[Idée #100]** : La Couleur Réservée à la Donnée
_Concept_ : Accents uniquement pour encoder l'info (cohérence #4, tendances #33, divergence #15) — toujours doublés d'une forme/icône (daltonisme).
_Nouveauté_ : La couleur est un canal de donnée, jamais une décoration partisane.

**[Idée #101]** : La Typographie Institutionnelle
_Concept_ : Police Marianne (font open source du service public numérique français) pour l'interface + serif sobre réservé aux verbatims/citations.
_Nouveauté_ : La distinction citation/synthèse est typographique — la nature du texte est visible avant la lecture.

**[Idée #102]** : L'Accessibilité comme Socle (WCAG AA+)
_Concept_ : Contrastes AA, corps ≥16px, focus visibles, `prefers-reduced-motion`, navigation clavier — chaque dataviz doublée d'un tableau HTML pour lecteurs d'écran.
_Nouveauté_ : Critère de chaque composant, comme la source primaire — pas un audit de fin.

**[Idée #103]** : Le Dark Mode Second Écran
_Concept_ : Thème sombre via `prefers-color-scheme`, pensé pour les soirs de débat télé (#68) et la veille du scrutin.
_Nouveauté_ : Le site accompagne les rituels réels de la campagne — les débats ont lieu à 21h.

**[Idée #104]** : Les 3 Couches de Profondeur
_Concept_ : Chaque page : résumé 3 lignes (lisible en story) → synthèse comparée → sources et verbatims pliables. Le lien social atterrit sur la couche 1.
_Nouveauté_ : Le même contenu sert le scrolleur pressé et le citoyen éclairé.

**[Idée #105]** : Le Partage en Un Tap
_Concept_ : Web Share API native sur chaque carte/page — génère l'image adaptée à la plateforme cible (9:16 story, 1:1 feed, carte horizontale) + le lien.
_Nouveauté_ : Le partage est une fonction du contenu, pensé pour WhatsApp, Instagram, X.

---

## Axes Explorés — Session Complète

- [x] **Cross-Pollination** — fait (Session 2, Axe 7)
- [x] **Dimension citoyenne** — fait (Session 2, Axe 8-9)
- [x] **Modèle de données complet** — fait (Session 2, Axe 10 → `data-model-draft.jsonc`)
- [x] **Gestion des cas limites** — fait (Session 2, Axe 11)
- [x] **Design visuel** — fait (Session 2, Axe 12)

---

---

## Synthèse Convergente — Plan d'action (fin Session #2)

### Clustering — 7 familles

| Famille | Idées clés | Ce qu'elle porte |
|---|---|---|
| Données & Intégrité | #76-85, #71-75, #31, #35 | Le socle — tout le reste en dépend |
| Mémoire civique | #4, #6, #8, #10, #51, #53 | La différenciation majeure |
| Gouvernance automatique | #21, #25, #26, #33, #86 | La neutralité rendue mécanique |
| Pipeline & Ops | #36, #44, #74, #85, #90-92, #95 | Viabilité à 6 mois, ~1h/semaine |
| UX & Comparaison | #13-17, #55, #87, #94, #96-97, #104 | L'expérience citoyenne |
| Diffusion & Impact | #61-65, #67-70, #98, #105 | Le site qui se fait connaître |
| Confiance & Neutralité | #27-28, #52, #89, #99-102, #66 | L'armure anti-accusation de biais |

### Concepts de rupture
1. **Mémoire civique vérifiable** — promesse vs actes documentés
2. **Gouvernance mécanique totale** — thèmes ET candidats gouvernés par la donnée
3. **Git comme journal éditorial public** — l'historique IS la transparence
4. **Le site qui survit à l'élection** — Promesse Datée → suivi du mandat

### Priorisation
| Vague | Contenu | Idées |
|---|---|---|
| **MVP** | Socle données, stack statique, comparaison, sources primaires, gouvernance, mobile-first | #76-85, #41, #13-14, #71/79, #21/25, #27/28, #96/97 |
| **V2** | Mémoire civique, pipeline auto, newsletter, SEO | #4/6/53, #36/44/85, #64, #61/62/105 |
| **V3** | Stories, widget, API, cas limites avancés, EMI | #98, #63, #60, #86-93, #65, #67 |

### Plan d'action — 4 phases

**Phase 0 — Fondations éditoriales** (avant le premier commit)
- [ ] Charte éditoriale (#28)
- [ ] Protocole de gouvernance thèmes + candidats (#21, #25, #26, #86)
- [ ] JSON Schema v1 finalisé (`data-model-draft.jsonc` → `schema/v1/`)
- [ ] Collecte initiale : 5 candidats × ~12 thèmes × sources primaires

**Phase 1 — MVP lisible** (le site existe, statique)
- [ ] Repo + Astro/Next.js + Vercel, Git→deploy (#41-42, #48)
- [ ] Page thème 3 couches (#104) : cartes mobile (#97) / colonnes desktop (#13)
- [ ] Fiches candidats + bandeau programme officiel (#14, #75)
- [ ] Mur des sources (#35) + pages Charte & Méthode (#27-28)
- [ ] Triple ancrage sources (#79) + enum de statut (#78)

**Phase 2 — La machine** (le site se met à jour)
- [ ] Scraper RSS instituts + sites candidats (#36, #74)
- [ ] Validation JSON Schema en CI (#85) + fail-safe (#91)
- [ ] Rapport de diff → validation éditeur → commit sémantique (#45-46)
- [ ] Fil du temps + Diff politique + Baromètre (#4, #6, #53)
- [ ] Recalcul tendances (#33) + ranking thèmes (#30) + newsletter (#64)

**Phase 3 — Diffusion** (avant les débats)
- [ ] SEO programmatique candidat × thème (#61)
- [ ] Open Graph (#62) + Web Share (#105) + stories 9:16 (#98)
- [ ] Ping liens morts + bascule archive (#90), API publique (#60), widget (#63)
- [ ] Mode Second Tour testé (#87), Protocole Gel (#95), Kit EMI (#65)

---

*103 idées — exploration terminée. Prochaine étape : Phase 0 (charte, gouvernance, schéma, collecte).*
