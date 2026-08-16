# Module 08 : Introduction au Machine Learning

## Objectifs

À la fin de ce module, vous saurez :

- situer le machine learning par rapport à l'économétrie (objectifs différents : prédiction vs inférence causale) ;
- préparer des données pour un modèle de ML (encodage, mise à l'échelle, split train/test) ;
- entraîner et évaluer un modèle de classification et un modèle de régression avec `scikit-learn` ;
- éviter le sur-apprentissage (*overfitting*) et valider un modèle correctement (validation croisée) ;
- réaliser une segmentation par clustering ;
- interpréter un modèle simple (importance des variables).

Ce module est une **introduction**. L'objectif est de comprendre les grands principes et de savoir quand le ML est pertinent pour une question de recherche en gestion, pas de devenir expert en ML.

## Prérequis

Module 04 (statistiques) recommandé. Le module 05 (économétrie) n'est pas indispensable, mais la comparaison avec la régression aide à mieux comprendre les spécificités du ML.

## Positionnement : ML vs économétrie

| | Économétrie | Machine learning |
|---|---|---|
| Objectif | Expliquer, tester une relation causale | Prédire, maximiser la précision |
| Priorité | Interprétabilité des coefficients | Performance prédictive |
| Exemple de question | "Le télétravail a-t-il un effet sur la performance ?" | "Quel employé risque de quitter l'entreprise ?" |

Les deux approches sont complémentaires plutôt que concurrentes pour la recherche en sciences de gestion.

## Contenu du module

1. **Préparer les données pour le ML**
   - Encoder les variables catégorielles (*one-hot encoding*)
   - Mettre à l'échelle les variables numériques (standardisation, normalisation)
   - Séparer en jeu d'entraînement et jeu de test (`train_test_split`)

2. **Classification supervisée**
   - Principe : prédire une catégorie
   - Un modèle simple : régression logistique, arbre de décision
   - Évaluer : matrice de confusion, précision, rappel, F1-score

3. **Régression supervisée**
   - Principe : prédire une valeur continue
   - Un modèle simple : régression linéaire régularisée (Ridge/Lasso), forêt aléatoire
   - Évaluer : RMSE, MAE, R²

4. **Éviter le sur-apprentissage**
   - Qu'est-ce que l'*overfitting* ? Pourquoi c'est un problème ?
   - Validation croisée (*cross-validation*)
   - Compromis biais-variance (intuition, sans les détails mathématiques)

5. **Apprentissage non supervisé : clustering**
   - Principe : regrouper des observations similaires sans variable cible
   - K-means, choisir le nombre de clusters
   - Cas d'usage en gestion : segmentation client, typologie d'entreprises

6. **Interprétation d'un modèle simple**
   - Importance des variables (*feature importance*)
   - Limites de l'interprétabilité des modèles complexes

## Pour commencer

Ouvrez le notebook [`08-intro-machine-learning.ipynb`](08-intro-machine-learning.ipynb) de ce module.

## Exercices

- Exercice 1 : préparer un jeu de données pour un modèle (encodage, split train/test)
- Exercice 2 : entraîner et évaluer un modèle de classification (ex. prédire le churn client)
- Exercice 3 : entraîner et évaluer un modèle de régression
- Exercice 4 : segmentation par K-means et interprétation des clusters obtenus

Corrigés disponibles dans [`solutions/08-intro-machine-learning/`](../../solutions/08-intro-machine-learning/).

## Aller plus loin (optionnel)

- [Documentation officielle scikit-learn](https://scikit-learn.org/stable/)
- [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course) (en anglais)

## Suite

Consultez la [roadmap](../../docs/roadmap.md). Le module [09-reproductibilite](../09-reproductibilite/) est recommandé pour structurer proprement un projet mobilisant ML ou économétrie.
