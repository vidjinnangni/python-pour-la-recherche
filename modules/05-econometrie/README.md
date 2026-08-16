# Module 05 : Économétrie

## Objectifs

À la fin de ce module, vous saurez :

- estimer et interpréter une régression linéaire simple et multiple avec `statsmodels` ;
- vérifier les conditions de validité d'une régression (hypothèses du modèle linéaire) ;
- diagnostiquer et traiter les problèmes courants (multicolinéarité, hétéroscédasticité) ;
- utiliser des variables catégorielles et des interactions dans un modèle ;
- estimer un modèle à variable dépendante binaire (régression logistique) ;
- estimer un modèle sur données de panel avec `linearmodels` (effets fixes, effets aléatoires).

Ce module est central pour toute recherche quantitative visant à établir des relations entre variables (ex. l'effet d'une pratique managériale sur la performance).

## Prérequis

Module 04 : statistiques descriptives et inférentielles, notamment la notion de corrélation et de test d'hypothèse.

## Durée estimée

8 à 10 heures.

## Contenu du module

1. **Régression linéaire simple**
   - Principe des moindres carrés ordinaires (MCO/OLS)
   - Estimer un modèle avec `statsmodels` (API `formula` façon R : `y ~ x`)
   - Lire une sortie de régression : coefficients, R², p-values, intervalles de confiance

2. **Régression linéaire multiple**
   - Ajouter des variables de contrôle
   - Interpréter les coefficients *toutes choses égales par ailleurs*
   - Variables catégorielles (variables indicatrices/*dummies*) et interactions

3. **Valider un modèle**
   - Hypothèses du modèle linéaire (linéarité, indépendance, homoscédasticité, normalité des résidus)
   - Diagnostiquer visuellement (graphiques de résidus)
   - Multicolinéarité (VIF) et hétéroscédasticité (test de Breusch-Pagan, écart-types robustes)

4. **Modèles à variable dépendante binaire**
   - Quand la régression linéaire n'est pas adaptée (variable expliquée 0/1, ex. churn, adoption d'une pratique)
   - Régression logistique avec `statsmodels`
   - Interpréter des coefficients en odds ratios

5. **Données de panel**
   - Spécificité des données de panel en gestion (ex. performance d'entreprises sur plusieurs années)
   - Modèle à effets fixes vs effets aléatoires, test de Hausman
   - Estimation avec `linearmodels`

## Pour commencer

Ouvrez le notebook [`05-econometrie.ipynb`](05-econometrie.ipynb) de ce module. Il s'appuie sur un jeu de données de panel fictif (performance d'entreprises sur plusieurs années) disponible dans [`assets/datasets/`](../../assets/datasets/).

## Exercices

- Exercice 1 : estimer et interpréter une régression multiple avec variables de contrôle
- Exercice 2 : diagnostiquer un modèle (résidus, multicolinéarité, hétéroscédasticité) et corriger si besoin
- Exercice 3 : estimer une régression logistique et interpréter les résultats
- Exercice 4 : estimer un modèle à effets fixes sur données de panel

Corrigés disponibles dans [`solutions/05-econometrie/`](../../solutions/05-econometrie/).

## Aller plus loin (optionnel)

- [Documentation officielle statsmodels](https://www.statsmodels.org/stable/index.html)
- [Documentation officielle linearmodels](https://bashtage.github.io/linearmodels/)
- [Wooldridge, *Introductory Econometrics: A Modern Approach*](https://faculty.cengage.com/works/9780357900161) : référence classique, transposable à Python.

## Suite

Consultez la [roadmap](../../docs/roadmap.md) pour la suite de votre parcours. Le module [09-reproductibilite](../09-reproductibilite/) est recommandé une fois que vous avez un vrai projet de recherche en cours.
