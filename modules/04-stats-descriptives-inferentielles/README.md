# Module 04 : Statistiques descriptives et inférentielles

## Objectifs

À la fin de ce module, vous saurez :

- calculer et interpréter les statistiques descriptives usuelles (tendance centrale, dispersion, distribution) ;
- comprendre et vérifier les conditions d'application des tests statistiques courants ;
- réaliser des tests d'hypothèses avec `scipy.stats` (comparaison de moyennes, corrélation, indépendance) ;
- interpréter une p-value correctement, et éviter les pièges d'interprétation les plus fréquents ;
- calculer et interpréter des intervalles de confiance.

Ce module est le socle statistique nécessaire avant d'aborder l'économétrie (module 05).

## Prérequis

Modules 00 à 03 (tronc commun). Des notions de statistiques de niveau licence/master sont utiles, mais pas indispensables. Les rappels théoriques nécessaires sont inclus.

## Durée estimée

5 à 7 heures.

## Contenu du module

1. **Statistiques descriptives**
   - Tendance centrale : moyenne, médiane, mode
   - Dispersion : écart-type, variance, quartiles, étendue
   - Forme de la distribution : asymétrie (*skewness*), aplatissement (*kurtosis*)
   - Statistiques descriptives avec `pandas` (`.describe()`) et `scipy.stats`

2. **Rappels sur les distributions**
   - Loi normale et son importance
   - Vérifier visuellement la normalité (histogramme, QQ-plot)
   - Tester la normalité (test de Shapiro-Wilk)

3. **Tests de comparaison de moyennes**
   - Test t de Student (deux échantillons indépendants, échantillons appariés)
   - ANOVA (comparaison de plus de deux groupes)
   - Alternatives non paramétriques (Mann-Whitney, Kruskal-Wallis) quand les conditions d'application ne sont pas remplies

4. **Tests de corrélation et d'indépendance**
   - Corrélation de Pearson (linéaire) vs Spearman (monotone, non paramétrique)
   - Test du Chi² d'indépendance (variables catégorielles), utile pour croiser deux variables qualitatives d'une enquête

5. **Interpréter une p-value correctement**
   - Ce qu'une p-value dit et ne dit pas
   - Seuil de significativité (5 %, 1 %) : convention, pas vérité absolue
   - Erreurs de type I et II
   - Le problème des comparaisons multiples

6. **Intervalles de confiance**
   - Construire et interpréter un intervalle de confiance
   - Lien avec les tests d'hypothèses

## Pour commencer

Ouvrez le notebook [`04-stats-descriptives-inferentielles.ipynb`](04-stats-descriptives-inferentielles.ipynb) de ce module.

## Exercices

- Exercice 1 : statistiques descriptives et détection d'anomalies dans un jeu de données
- Exercice 2 : tester si deux groupes diffèrent significativement (ex. satisfaction moyenne entre deux segments de clients)
- Exercice 3 : tester une corrélation et un lien d'indépendance entre deux variables catégorielles
- Exercice 4 : construire et interpréter un intervalle de confiance

Corrigés disponibles dans [`solutions/04-stats-descriptives-inferentielles/`](../../solutions/04-stats-descriptives-inferentielles/).

## Aller plus loin (optionnel)

- [Documentation officielle scipy.stats](https://docs.scipy.org/doc/scipy/reference/stats.html)
- [Introduction aux statistiques](https://www.datacamp.com/fr/courses/introduction-to-statistics)

## Suite

Selon votre objectif (voir la [roadmap](../../docs/roadmap.md)) :

- aller vers l'[économétrie](../05-econometrie/), pour la modélisation (régressions, panels) ;
- aller vers le [machine learning](../08-intro-machine-learning/), pour des approches prédictives.
