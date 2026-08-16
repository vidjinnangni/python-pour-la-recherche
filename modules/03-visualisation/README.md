# Module 03 : Visualisation

## Objectifs

À la fin de ce module, vous saurez :

- choisir le bon type de graphique selon votre message et vos données ;
- produire des graphiques avec `matplotlib` et `seaborn` ;
- personnaliser un graphique pour qu'il soit lisible et présentable (titres, légendes, échelles) ;
- créer des graphiques interactifs avec `plotly` ;
- exporter vos graphiques pour un article, un rapport ou une présentation.

C'est le dernier module du tronc commun. À la fin de ce module, vous êtes autonome sur l'essentiel des tâches courantes de traitement et de représentation de données.

## Prérequis

Module 02. Vous devez savoir manipuler un `DataFrame` pandas.

## Durée estimée

3 à 4 heures.

## Contenu du module

1. **Choisir le bon graphique**
   - Comparer des catégories → barres
   - Montrer une évolution → ligne
   - Montrer une distribution → histogramme, boxplot
   - Montrer une relation entre deux variables → nuage de points (scatter)
   - Erreurs fréquentes (échelles trompeuses, trop d'informations sur un même graphique)

2. **Matplotlib : les bases**
   - Anatomie d'une figure (`Figure`, `Axes`)
   - Graphiques de base : ligne, barres, histogramme, nuage de points
   - Personnalisation : titres, labels, légendes, couleurs, taille

3. **Seaborn : aller plus vite et plus loin**
   - Graphiques statistiques prêts à l'emploi (`boxplot`, `violinplot`, `heatmap`)
   - Visualiser des corrélations (matrice de corrélation)
   - Graphiques par groupe/catégorie en une ligne de code

4. **Plotly : l'interactivité**
   - Quand l'interactivité apporte de la valeur (exploration, présentation web)
   - Graphiques interactifs de base (ligne, barres, scatter)

5. **Produire un graphique présentable**
   - Bonnes pratiques pour un graphique destiné à un article académique (résolution, noir et blanc/couleur, taille de police)
   - Exporter en `.png`, `.pdf`, `.svg`

## Pour commencer

Ouvrez le notebook [`03-visualisation.ipynb`](03-visualisation.ipynb) de ce module. Il réutilise le jeu de données d'entreprises du module 02.

## Exercices

Voir le dossier [`exercices/`](exercices/) :

- Exercice 1 : reproduire un graphique donné (choix du bon type de graphique)
- Exercice 2 : personnaliser un graphique pour le rendre présentable (titres, légendes, échelle)
- Exercice 3 : visualiser une corrélation entre deux variables avec seaborn
- Exercice 4 : créer un graphique interactif simple avec plotly

Corrigés disponibles dans [`solutions/03-visualisation/`](../../solutions/03-visualisation/).

## Aller plus loin (optionnel)

- [Documentation officielle matplotlib](https://matplotlib.org/stable/index.html)
- [Documentation officielle seaborn](https://seaborn.pydata.org/)
- [Documentation officielle plotly (Python)](https://plotly.com/python/)
- [From Data to Viz](https://www.data-to-viz.com/), pour choisir le bon type de graphique

## Suite

Le tronc commun est terminé. Consultez la [roadmap](../../docs/roadmap.md) pour choisir votre parcours selon votre objectif de recherche : économétrie, enquêtes, texte, ou machine learning.
