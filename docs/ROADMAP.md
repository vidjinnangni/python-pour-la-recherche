# ROADMAP

Ce repo de ressources pour apprendre à utiliser Python comme outil de recherche en sciences de gestion n'impose pas d'ordre strict au-delà du **tronc commun**. Vous pourrez ensuite choisir le parcours qui correspond le mieux à votre objectif.

## Tronc commun (obligatoire)

Il s'agit des 4 premiers modules à partir desquels vous allez pouvoir acquérir les bases nécessaires.

| Module                   | Contenu                                                                            | Durée estimée |
| ------------------------ | ---------------------------------------------------------------------------------- | ------------- |
| `00-prise-en-main`       | Installer Python, Jupyter/Colab, Git, se repérer dans le repo                      | 1 - 2h        |
| `01-fondamentaux-python` | Variables, types de données, boucles, conditions, fonctions, structures de données | 4 - 6h        |
| `02-pandas-donnees`      | Charger, nettoyer, croiser, transformer des données                                | 6 - 8h        |
| `03-visualisation`       | Graphiques avec matplotlib, seaborn, plotly                                        | 3 - 4h        |

> Les modules `00` à `03` permettent déjà d'avoir les bases  pour être autonome sur 80 % des tâches courantes de traitement de données.

## Parcours par objectif

### Économétrie / Tests statistiques

`00` → `01` → `02` → `03` → **`04-stats-descriptives-inferentielles`** → **`05-econometrie`** → `09-reproductibilite`

Études quantitatives, tests d'hypothèses, régressions, données de panel.

### Données d'enquêtes / de sondage

`00` → `01` → `02` → `03` → **`07-enquetes-sondages`** → `04-stats-descriptives-inferentielles` → `09-reproductibilite`

Études de satisfaction, enquêtes, panels consommateurs, pondération d'échantillons.

### Données textuelles

`00` → `01` → `02` → `03` → **`06-texte-scraping`** → `08-machine-learning-intro` (pour aller plus loin) → `09-reproductibilite`

Analyse de contenu, Revues de littérature assistées, sentiment analysis.

### Explorer le machine learning appliquée à la gestion

`00` → `01` → `02` → `03` → `04-stats-descriptives-inferentielles` → **`08-machine-learning-intro`** → `09-reproductibilite`

Segmentation client, prédiction, scoring, détection de patterns dans de larges jeux de données.

---

> Si vous découvrez Python et n'avez pas encore de projet précis, vous pouvez suivre l'ordre `00` à `09`. Au module `03-visualisation`, vous pouvez faire un bilan pour évaluer si vous souhaitez aller plus loin ou pas.

Le module `09-reproductibilite` (structurer un projet de recherche) est à suivre si vous avez un vrai projet entre les mains.

---

## Résumé

```
                        00 → 01 → 02 → 03  (tronc commun)
                                      │
              ┌───────────┬──────────┼───────────┐
              │           │          │           │
              04+05       07         06          04+08
           (économétrie) (enquêtes) (texte)      (ML)
              │           │          │           │
              └───────────┴──────────┴───────────┘
                              │
                              09 (reproductibilité)
```
