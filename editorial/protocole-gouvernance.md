# Protocole de Gouvernance

**Projet : Site citoyen de comparaison des programmes — Élection présidentielle 2027**
**Version :** 1.0 — 17 octobre 2026
**Rôle :** Définir mécaniquement ce qui entre, sort et se classe sur le site. L'éditeur applique le protocole ; il ne décide pas.

---

## 1. Gouvernance des thèmes

### 1.1 Critères d'entrée
Un thème intègre la liste active s'il remplit **au moins 2 des 3 critères** suivants :

| # | Critère | Mesure |
|---|---------|--------|
| 1 | Couverture médiatique | Cité comme sujet de fond dans ≥3 grands médias nationaux au cours de la semaine écoulée |
| 2 | Présence programmatique | Abordé dans ≥1 programme ou déclaration officielle de candidat du top 5 |
| 3 | Préoccupation citoyenne | Présent dans le top 10 des préoccupations des Français dans ≥1 sondage institutionnel récent |

### 1.2 Cycle de révision
- **Chaque lundi**, les 3 critères sont réévalués pour chaque thème à partir des publications de la semaine écoulée.
- Le résultat de l'évaluation est consigné dans le fichier du thème (`criteres_entree`) et dans le commit Git — la décision est auditable.

### 1.3 Hiérarchie d'affichage
- L'ordre des thèmes sur la page d'accueil suit le classement du **Baromètre des Préoccupations** (dernier sondage institutionnel disponible).
- Chaque thème porte un indicateur de tendance recalculé hebdomadairement : `hausse` / `stable` / `baisse` (variation entre les 2 derniers sondages).

### 1.4 Sortie et archivage
- Un thème qui ne remplit plus qu'un seul critère (ou aucun) pendant **4 semaines consécutives** passe en statut `archive`.
- Un thème archivé reste accessible, daté, documenté — **jamais supprimé**.
- Un thème archivé qui re-remplit les critères repasse `actif` à la révision suivante.

### 1.5 Cas particuliers
- **Thème fantôme** : un thème qui remplit les critères d'entrée mais sur lequel aucun candidat n'a de position est publié quand même — ses cellules sont en statut `attendue`. Le silence collectif est une information.
- **Nouveau thème** : badge `nouveau` affiché pendant 14 jours après `date_ajout`.
- **Suggestion citoyenne** : un thème proposé par le formulaire est évalué sur les mêmes 3 critères à la révision suivante ; acceptation ou refus documentés publiquement avec la justification chiffrée.

---

## 2. Gouvernance des candidats

### 2.1 Règle du Top 5
- Le site présente les **5 candidats** les plus crédités d'intentions de vote.
- Le classement de référence est la **moyenne des intentions de vote au premier tour** mesurée sur les **3 derniers sondages institutionnels** publiés par les instituts éligibles (premier scénario présenté par l'institut, population "certains d'aller voter" si disponible).

### 2.2 Entrée — règle anti-bascule
- Un candidat hors du top 5 n'y entre que s'il est classé dans le top 5 à **2 révisions hebdomadaires consécutives**. Cette règle évite les entrées/sorties sur une fluctuation de sondage unique.

### 2.3 Sortie
- Un candidat du top 5 qui en sort à 2 révisions consécutives passe hors de l'affichage actif — sa fiche et ses positions sont **archivées**, jamais supprimées.
- Tout changement de composition est signalé au Journal des Mises à Jour avec les sondages sources.

### 2.4 Cycle de vie d'un candidat
`pressenti` → `declare` → `retire` | `remplace`

- `pressenti` : non déclaré officiellement mais dans le top 5 des sondages
- `declare` : candidature officiellement annoncée
- `retire` : retrait annoncé — fiche archivée, positions conservées et datées
- `remplace` : remplacé par un autre candidat de sa formation — la fiche du remplaçant est créée et le lien de filiation documenté sur les deux fiches

### 2.5 Équité de traitement
- Les 5 candidats reçoivent la même structure de fiche, la même profondeur de recherche, le même espace d'affichage.
- Candidat sans expérience gouvernementale : ses actes concrets dans son domaine d'origine sont documentés comme proxy (règle de la Carte Blanche Équitable).
- Candidat sans position sur un thème : cellule affichée en `attendue` avec date de dernière vérification — jamais vide.

### 2.6 Le candidat de référence (exception déclarée)
- **Dominique de Villepin** occupe une **6e place permanente**, hors du top 5 : le **candidat de référence**.
- Rôle : sur chaque thème, les positions des 5 candidats sont comparées à la sienne — il est le référentiel transversal du site. Il ne concourt pas au classement.
- **C'est la seule décision éditoriale non mécanique du site.** Elle est choisie, assumée et déclarée publiquement dans ce protocole et sur la page Gouvernance.
- Justification du choix : expérience exécutive complète (Premier ministre, Intérieur, Affaires étrangères), stature transpartisane, programme structuré.
- Ses positions sont sourcées avec la même rigueur que celles du top 5 (triple ancrage, fil du temps, actes passés).
- **Cas particuliers** : s'il entre dans le top 5 par les sondages, il devient concurrent (`role: concurrent`) et le site documente le choix d'un nouveau référentiel. S'il se retire, la place de référence est réévaluée éditorialement et la décision publiée au Journal.

---

## 3. Bascules de phase

| Événement | Effet |
|---|---|
| Annonce officielle des candidatures | Passage des candidats confirmés en `declare` |
| Soir du 1er tour | **Mode Second Tour** : les 3 éliminés en archive visible, les 2 finalistes en Face à Face page d'accueil |
| Soir du 2nd tour | **Mode Mémoire** : suivi des promesses du vainqueur (Tenu / Partiellement tenu / Non tenu / Abandonné) |
| Crise grave | **Protocole Gel** (cf. Charte §7) |

---

## 4. Journalisation

Chaque application de ce protocole produit une entrée publique :
- entrée/sortie de thème → commit `[GOV]` + ligne au Journal des Mises à Jour
- entrée/sortie de candidat → commit `[GOV]` + ligne au Journal + sondages justificatifs
- refus de suggestion citoyenne → motif chiffré publié

*Le protocole est volontairement ennuyeux : sa force est d'être prévisible, vérifiable et identique pour tous.*
