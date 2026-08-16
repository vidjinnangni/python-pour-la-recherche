# Module 02  : Manipulation de données avec Pandas

## Objectifs

À la fin de ce module, vous saurez :

- charger des données depuis différents formats (CSV, Excel) dans un `DataFrame` pandas ;
- explorer et diagnostiquer un jeu de données (types, valeurs manquantes, doublons) ;
- sélectionner, filtrer et trier des données ;
- nettoyer des données (valeurs manquantes, formats incohérents, doublons) ;
- créer de nouvelles variables (colonnes calculées) ;
- grouper et agréger des données (`groupby`) ;
- croiser plusieurs jeux de données (jointures) ;
- gérer des dates.  

C'est le module central du tronc commun : `pandas` est l'outil que vous utiliserez pour la quasi-totalité de vos traitements de données de recherche.

## Prérequis

Module 01. Vous devez être à l'aise avec les listes, dictionnaires, boucles et fonctions Python.

## Durée estimée

6 à 8 heures

## Contenu du module

1. **Découverte du DataFrame**
    - `Series` vs `DataFrame`
    - Charger un CSV (`read_csv`) et un Excel (`read_excel`)
    - Premiers réflexes d'exploration : `.head()`, `.info()`, `.describe()`, `.shape`

2. **Sélectionner et filtrer**
    - Sélectionner des colonnes, des lignes (`loc`, `iloc`)
    - Filtrer selon une ou plusieurs conditions
    - Trier (`sort_values`)

3. **Nettoyer les données**
    - Repérer et traiter les valeurs manquantes (`isna`, `dropna`, `fillna`)
    - Repérer et traiter les doublons (`duplicated`, `drop_duplicates`)
    - Corriger des types et formats incohérents (ex. texte au lieu de nombre)

4. **Créer et transformer des variables**
    - Créer une colonne calculée à partir d'autres colonnes
    - `apply` et fonctions personnalisées
    - Recoder des catégories (ex. regrouper des modalités d'une variable qualitative)

5. **Grouper et agréger (`groupby`)**
    - Statistiques par groupe (ex. chiffre d'affaires moyen par secteur)
    - Tableaux croisés (`pivot_table`)

6. **Croiser plusieurs jeux de données**
    - `merge` (jointures façon SQL : inner, left, right, outer)
    - `concat` (empiler des données)
    - Cas fréquent en gestion : croiser des données financières et des données RH sur un identifiant d'entreprise commun

7. **Gérer les dates**
    - Convertir en `datetime`
    - Extraire année/mois/jour, calculer des durées
    - Utile pour les séries temporelles (ex. évolution du cours d'une action, données de panel).

## Pour commencer

Ouvrez le notebook [`02-pandas-donnees.ipynb`](02-pandas-donnees.ipynb) de ce module. Il s'appuie sur un jeu de données fictif disponible dans [`assets/datasets/`](../../assets/datasets/).

## Exercices

- Exercice 1 : chargement et exploration d'un jeu de données réel
- Exercice 2 : nettoyage (valeurs manquantes, doublons, types)
- Exercice 3 : `groupby` et statistiques par groupe (ex. performance moyenne par secteur d'activité)
- Exercice 4 : croiser deux jeux de données avec `merge`

Corrigés disponibles dans [`solutions/02-pandas-donnees/`](../../solutions/02-pandas-donnees/).

## Aller plus loin (optionnel)

- [Documentation officielle pandas](https://pandas.pydata.org/docs/)
- [Pandas Cheat Sheet (PDF)](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)

## Suite

Une fois à l'aise avec `pandas`, passez au module [03-visualisation](../03-visualisation/) pour apprendre à représenter graphiquement vos données, ou consultez la [roadmap](../../docs/roadmap.md) pour choisir votre parcours selon votre objectif de recherche.
