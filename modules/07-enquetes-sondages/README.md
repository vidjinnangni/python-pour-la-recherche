# Module 07 : Enquêtes et sondages

## Objectifs

À la fin de ce module, vous saurez :

- importer et structurer des données d'enquête (export Qualtrics, LimeSurvey, Google Forms) ;
- nettoyer des données de questionnaire (réponses incomplètes, tests de qualité, données à l'envers) ;
- recoder des variables (échelles de Likert, variables composites) ;
- calculer et vérifier la fiabilité d'une échelle (alpha de Cronbach) ;
- pondérer un échantillon pour le redresser par rapport à une population de référence ;
- produire les tableaux et graphiques usuels d'un rapport d'enquête.

Ce module s'adresse à toute recherche qui mobilise des données de questionnaire : satisfaction, enquêtes, panels...

## Prérequis

Modules 00 à 04 (tronc commun + statistiques descriptives/inférentielles).

## Durée estimée

6 à 8 heures.

## Contenu du module

1. **Importer des données d'enquête**
   - Formats d'export courants (Qualtrics, LimeSurvey, Google Forms, SurveyMonkey) et les erreurs fréquentes (lignes d'en-tête multiples, métadonnées)
   - Repérer les questions, sous-questions et variables techniques (durée, date, IP)

2. **Nettoyer les données de questionnaire**
   - Réponses incomplètes ou abandonnées en cours de route
   - Tests d'attention / questions pièges (*attention checks*)
   - Détecter les patterns suspects
   - Items inversés (*reverse-coded*) à recoder

3. **Recoder et construire des variables**
   - Échelles de Likert
   - Construire une variable composite à partir de plusieurs items (ex. score moyen de satisfaction)
   - Variables catégorielles issues de questions à choix multiples

4. **Fiabilité d'une échelle**
   - Principe de l'alpha de Cronbach
   - Calcul avec Python, seuils d'interprétation usuels
   - Que faire si l'alpha est trop faible (retirer un item, etc.)

5. **Pondération et redressement**
   - Pourquoi pondérer (échantillon non représentatif de la population cible)
   - Principe du redressement (ex. calage sur marges : âge, secteur, taille d'entreprise)
   - Appliquer des poids dans les statistiques descriptives

6. **Produire un rapport d'enquête**
   - Tableaux de fréquence, tris croisés
   - Graphiques usuels (barres empilées pour Likert, etc.)

## Pour commencer

Ouvrez le notebook [`07-enquetes-sondages.ipynb`](07-enquetes-sondages.ipynb) de ce module. Il s'appuie sur un export fictif de questionnaire de satisfaction, disponible dans [`assets/datasets/`](../../assets/datasets/).

## Exercices

- Exercice 1 : importer et nettoyer un export de questionnaire fictif
- Exercice 2 : recoder des items de Likert et construire une variable composite
- Exercice 3 : calculer l'alpha de Cronbach d'une échelle
- Exercice 4 : pondérer un échantillon et comparer les résultats pondérés/non pondérés

Corrigés disponibles dans [`solutions/07-enquetes-sondages/`](../../solutions/07-enquetes-sondages/).

## Aller plus loin (optionnel)

- [Documentation officielle pandas](https://pandas.pydata.org/docs/) (rappel, très utilisé dans ce module)
- [pyreadstat](https://github.com/Roche/pyreadstat), pour importer des fichiers SPSS (`.sav`) si besoin
- [Documentation Qualtrics : export de données](https://www.qualtrics.com/support/)

## Suite

Consultez la [roadmap](../../docs/roadmap.md) pour la suite de votre parcours. Le module [04-stats-descriptives-inferentielles](../04-stats-descriptives-inferentielles/) est un bon complément si ce n'est pas déjà fait, pour aller plus loin dans l'analyse de vos résultats d'enquête.
