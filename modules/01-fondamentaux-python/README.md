# Module 01 : Fondmentaux Python

## Objectifs

À la fin de ce module, vous saurez :

- manipuler les types de base (nombres, texte, booléens) et les structures de données (listes, dictionnaires, tuples) en Python ;
- écrire des conditions et des boucles ;
- écrire et utiliser des fonctions ;
- lire et comprendre les messages d'erreur Python les plus courants ;
- importer et utiliser une bibliothèque externe.

Ce module donne **les bases générales de programmation en Python**. Il n'est pas spécifique à la recherche en gestion.

## Prérequis

Module 00 : avoir un environnement Python fonctionnel (Colab ou local).

## Durée estimée

4 à 6 heures.

## Contenu du module

1. **Qu'est-ce que Python ?**

2. **Variables et types de base**
    - Nombres (`int`, `float`), texte (`str`), booléens (`bool`)
    - Conversion de types

3. **Structures de données**
    - Les listes (`list`)
    - Les dictionnaires (`dict`) : paires clé/valeur, très utile pour représenter des données structurées
    - Les tuples (`tuple`)
    - Aperçu des ensembles (`set`)

4. **Conditions**
    - `if` / `elif` / `else`
    - Opérateurs de comparaison et logiques (`==`, `!=`, `and`, `or`, `not`)

5. **Boucles**
    - `for` : parcourir une liste, un dictionnaire
    - `while`
    - Compréhensions de liste (`[x for x in ...]`) : un raccourci très utilisé en Python

6. **Fonctions**
    - Définir une fonction (`def`), paramètres, valeur de retour
    - Pourquoi découper son code en fonctions (réutilisabilité, lisibilité)

7. **Erreurs et débogage**
    - Lire un message d'erreur (traceback)
    - Erreurs courantes : `NameError`, `TypeError`, `IndexError`, `KeyError`

8. **Bibliothèques**
    - `import`
    - Différence entre bibliothèque standard et bibliothèque externe (celles de `requirements.txt`)

## Pour commencer

Ouvrez le notebook [`01-fondamentaux-python.ipynb`](01-fondamentaux-python.ipynb) de ce module.

## Exercices

Voir le dossier [`exercices/`](exercices/) :

- Exercice 1 : manipulation de listes et dictionnaires (ex. structurer une petite liste de répondants à une enquête fictive)
- Exercice 2 : boucles et conditions (ex. filtrer des données selon un critère)
- Exercice 3 : écrire une fonction réutilisable (ex. calculer une moyenne pondérée)

Corrigés disponibles dans [`solutions/01-fondamentaux-python/`](../../solutions/01-fondamentaux-python/).

> *Essayez de résoudre les exercices avant de les consulter*.

## Aller plus loin (optionnel)

- [Le tutoriel Python officiel](https://docs.python.org/fr/3/tutorial/)
- [Python Basics](https://realpython.com/tutorials/basics/)

## Suite

Une fois les bases acquises, passez au module [02-pandas-donnees](../02-pandas-donnees/), où l'on commence à travailler avec de vraies données de recherche.
