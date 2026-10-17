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

## Principes invariants

- Toute position citée porte une **source primaire** (site officiel candidat/parti, source gouvernementale) — `statut: sourcee | attendue | non_sourcee | contradictoire`, jamais de cellule vide.
- La colonne **Référence** (Villepin) apparaît en premier : première carte sur mobile, colonne de gauche sur desktop.
- Couleurs réservées à la donnée — aucun code couleur partisan.
