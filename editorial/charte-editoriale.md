# Charte Éditoriale

**Projet : Site citoyen de comparaison des programmes — Élection présidentielle 2027**
**Version :** 1.0 — 17 octobre 2026
**Statut :** Publique — affichée en permanence sur le site (footer)

---

## 1. Mission

Permettre à tout citoyen de comparer les positions des candidats les plus probables à l'élection présidentielle 2027, thème par thème, à partir de sources primaires vérifiables, sans intermédiation partisane.

Le site est un **aiguillage vers les sources**, jamais un substitut. Toute synthèse renvoie au document officiel dont elle est issue.

---

## 2. Principes non négociables

### 2.1 Neutralité absolue
- Aucun qualificatif éditorial sur les candidats, les positions, les changements de position.
- Les formulations sont descriptives et factuelles : "Le candidat propose X" — jamais "le candidat promet enfin / ose / prétend X".
- Le citoyen juge. Le site documente.
- Aucune couleur, typographie ou mise en page ne favorise ou défavorise un candidat (cf. neutralité chromatique).

### 2.2 Source primaire obligatoire
- Toute position affichée est adossée à un lien vers le **site officiel du candidat ou de son parti** (programme, communiqué, discours publié).
- Chaque source porte un **triple ancrage** : `url_live` (site officiel) + `url_archive` (web.archive.org) + `date_verification`.
- Une position sans source primaire est affichée avec le statut `non_sourcee` ou `attendue` — jamais masquée, jamais inventée.

### 2.3 Instituts de sondage éligibles
- Seules les publications de ces instituts alimentent les données d'opinion : **IFOP, BVA, OpinionWay, Harris Interactive, Elabe**.
- 1 donnée = 1 institut identifié + 1 date + 1 question verbatim + 1 lien vers l'étude originale. Aucun sondage agrégé ou anonyme.

### 2.4 Traçabilité totale
- Toute modification du contenu est versionnée dans Git (historique public).
- Chaque changement de position d'un candidat est documenté : date, ancienne position sourcée, nouvelle position sourcée, contexte factuel neutre.
- Le Journal des Mises à Jour est public et permanent.

### 2.5 Gouvernance mécanique
- Ni les thèmes ni les candidats du top 5 ne sont choisis par décision humaine : ils entrent et sortent selon les critères objectifs du Protocole de Gouvernance (document séparé, public).
- **Exception déclarée** : le candidat de référence (Protocole §2.6) est un choix éditorial unique — il est assumé, justifié et publié. Cacher une exception serait une violation de cette charte ; la déclarer n'en est pas une.

---

## 3. Ce que le site ne fait jamais

- Aucun pronostic sur le résultat de l'élection.
- Aucune notation, classement ou recommandation de candidat.
- Aucun commentaire sur la cohérence d'un candidat (le score de cohérence, s'il existe, est une mesure documentée, pas un jugement).
- Aucune publicité, aucun contenu sponsorisé, aucune donnée de tracking partagée à des tiers à fins commerciales.
- Aucune suppression de contenu : ce qui sort de l'affichage actif est **archivé**, jamais effacé.

---

## 4. Gestion des erreurs

- Une erreur constatée est corrigée **publiquement** : la correction apparaît au Journal des Mises à Jour avec la même visibilité que la donnée erronée.
- Une donnée dont la vérification échoue repasse en statut `attendue` — le site préfère afficher une absence qu'une information fausse.
- Si un institut retire ou corrige une publication, la rétractation est documentée et les calculs dépendants sont recalculés.

## 5. Droit de réponse

- Chaque position affichée offre à l'équipe de campagne concernée un canal de contestation avec possibilité de fournir la source correcte.
- Toute contestation et sa résolution sont tracées publiquement au Journal des Mises à Jour.

## 6. Conflits d'intérêt

- L'identité de l'éditeur est publique sur le site.
- Tout lien professionnel, militant ou financier avec un parti, une campagne ou un institut couvert doit être déclaré publiquement sur la page de gouvernance.
- En l'absence de déclaration, ce principe vaut engagement que l'éditeur n'entretient aucun tel lien.

## 7. Protocole de crise

- En cas d'événement grave affectant la campagne (attentat, report de l'élection, crise nationale), l'éditeur active le **protocole gel** : bandeau neutre d'information, suspension de toute publication automatisée jusqu'à décision humaine explicite de reprise.

## 8. Modification de la charte

- Toute modification de la présente charte est elle-même versionnée dans Git et signalée au Journal des Mises à Jour. La charte ne peut être modifiée rétroactivement.

---

*Cette charte est la règle du jeu. Si le site la viole, la violation est documentable — c'est voulu.*
