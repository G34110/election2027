# Comparer 2027

Site citoyen de comparaison des programmes des candidats à l'élection présidentielle 2027 — cinq candidats issus de la gouvernance mécanique des sondages + un candidat de référence (Dominique de Villepin, Protocole §2.6).

## Structure

```
├── editorial/          # Contenu éditorial — la matière du projet
│   ├── charte-editoriale.md      # Règles de neutralité et de sourcing
│   ├── protocole-gouvernance.md  # Gouvernance mécanique (thèmes, top 5, référence)
│   ├── brainstorming-session-01.md
│   ├── data-model-draft.jsonc
│   └── data/                     # Données versionnées (JSON Schema v1)
│       ├── schema/v1/            # position, candidat, theme, sondage
│       ├── candidats/            # 6 fiches (5 concurrents + 1 référence)
│       ├── positions/            # candidat × thème — 1 fichier par cellule
│       ├── themes/               # 12 thèmes issus des sondages de préoccupations
│       └── sondages/             # Sondages institutionnels normalisés
└── site/               # Code et maquettes
    └── maquettes/                # Maquettes HTML statiques (données réelles)
```

## Prévisualiser une maquette

```powershell
python -m http.server 8727 --directory site/maquettes
# → http://localhost:8727/theme-pouvoir-achat.html
```

## Valider les données

```powershell
python -c "import json,glob; [json.load(open(f,encoding='utf-8')) for f in glob.glob('editorial/data/**/*.json',recursive=True)]; print('JSON valides')"
```

## Déploiement (OVH mutualisé)

- **URL cible** : `https://election2027.cvbusiness.fr`
- Multisite : sous-domaine `election2027` de `cvbusiness.fr` → dossier `www/`
- Upload FTP : contenu de `site/maquettes/` → `/www/` (identifiants dans Espace client → FTP-SSH)
- Certificat SSL : Let's Encrypt gratuit à activer dans l'espace client

## Principes invariants

- Toute position citée porte une **source primaire** (site officiel candidat/parti, source gouvernementale) — `statut: sourcee | attendue | non_sourcee | contradictoire`, jamais de cellule vide.
- **Villepin est affiché comme les autres candidats** — aucun statut de « référence » visible (décision du 18/10/2026). Hors sélection mécanique des sondages, il reste affiché en suivi éditorial ; à l'automatisation, le retirer de la comparaison s'il n'est pas qualifié au second tour 2027.
- Couleurs réservées à la donnée — aucun code couleur partisan.

## Automatisation hebdomadaire (dimanche 18h)

Le pipeline  est lancé par la tâche planifiée
Windows « Comparer2027-MAJ-hebdo » (installation unique : Opration russie : la tche planifie "Comparer2027-MAJ-hebdo" a t cre.

Tache "Comparer2027-MAJ-hebdo" installee : chaque dimanche a 18h00.
Pour verifier : schtasks /query /tn "Comparer2027-MAJ-hebdo"
Pour supprimer : schtasks /delete /tn "Comparer2027-MAJ-hebdo" /f
Appuyez sur une touche pour continuer... ).
Chaque exécution :

1. **Re-vérifie les sources** — re-télécharge chaque , compare le hash
   au dernier état (). Changement détecté →
   flag « revue éditoriale » dans .
2. **Surveille les index programmes** des candidats ayant des fiches
   / → nouvelles positions possibles.
3. **Cascade thèmes** — tout thème  de  obtient
   automatiquement ses 6 fiches , sa maquette et sa tuile d'index
   (un nouveau thème se propage donc seul). Le classement du baromètre
   ( à renseigner) est surveillé : changement → signaler +
   mettre à jour , le reste suit.
4. **Règle de sélection candidats** — un candidat suivi absent du dernier
   sondage publié est signalé pour retrait (ex. Villepin hors second tour).
5. **Timbres** — « Vérifié le » / « Mis à jour le » dans le footer des pages.
6. **Journal** — entrée datée dans  si évolutions.
7. **Regénère**  et les chips ; **commit + push** GitHub.
8. **Déploie**  via FTP ( à la racine —
   gitignoré, cf. ).

Limite assumée : le pipeline **détecte et signale** les évolutions ; il ne
rédige jamais une synthèse neutre — les sources modifiées attendent une
revue éditoriale avant réécriture des cartes.
