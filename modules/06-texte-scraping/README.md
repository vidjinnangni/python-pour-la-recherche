# Module 06 : Texte et scraping

## Objectifs

À la fin de ce module, vous saurez :

- collecter des données depuis le web de façon éthique (requêtes HTTP, API, scraping) ;
- nettoyer et préparer un corpus de texte pour l'analyse ;
- réaliser une analyse de fréquence et une analyse de sentiment simples ;
- comprendre les enjeux légaux et éthiques de la collecte de données web pour la recherche.

Ce module est utile pour toute recherche qui mobilise des données textuelles : avis, rapports annuels, articles de presse, entretiens retranscrits.

## Prérequis

Modules 00 à 03 (tronc commun). Le module 04 (stats) est utile, mais pas indispensable pour la première partie du module.

## Durée estimée

6 à 8 heures.

## Contenu du module

1. **Enjeux légaux et éthiques (à lire en premier)**
   - Conditions d'utilisation des sites, RGPD, droit d'auteur
   - Préférer une API officielle au scraping quand elle existe
   - Respecter le fichier `robots.txt` et ne pas surcharger un serveur
   - Anonymisation des données personnelles collectées

2. **Collecter des données**
   - Requêtes HTTP avec `requests`
   - Utiliser une API (structure JSON, authentification simple par clé)
   - Scraping HTML avec `BeautifulSoup` : sélectionner des éléments, extraire du texte

   *Ce module ne couvre pas les sites qui nécessitant du JavaScript dynamique*

3. **Nettoyer un corpus de texte**
   - Normalisation (minuscules, ponctuation, espaces)
   - Suppression des mots vides (*stop words*)
   - Tokenisation avec `nltk`
   - Lemmatisation / racinisation (*stemming*)

4. **Analyses de base sur le texte**
   - Fréquence des mots, nuages de mots
   - Analyse de sentiment simple (approche par lexique)
   - *Aperçu* de la vectorisation de texte (TF-IDF) ; prérequis du module ML

## Pour commencer

Ouvrez le notebook [`06-texte-scraping.ipynb`](06-texte-scraping.ipynb) de ce module. **Lisez la section sur les enjeux légaux et éthiques avant de scraper quoi que ce soit**, même pour vos projets personnels.

## Exercices

Voir le dossier [`exercices/`](exercices/) :

- Exercice 1 : collecter des données via une API publique (JSON)
- Exercice 2 : scraper une page HTML simple avec BeautifulSoup
- Exercice 3 : nettoyer un corpus de texte fourni (avis clients fictifs)
- Exercice 4 : analyse de fréquence et de sentiment sur ce corpus

Corrigés disponibles dans [`solutions/06-texte-scraping/`](../../solutions/06-texte-scraping/).

## Aller plus loin (optionnel)

- [Documentation officielle requests](https://requests.readthedocs.io/)
- [Documentation officielle BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Documentation officielle nltk](https://www.nltk.org/)
- CNIL, [Le web scraping](https://www.cnil.fr/) : cadre légal en France/UE

## Suite

Pour aller plus loin dans l'analyse de texte avec des méthodes prédictives, direction le module [08-intro-machine-learning](../08-intro-machine-learning/). Sinon, consultez la [roadmap](../../docs/roadmap.md) pour la suite de votre parcours.
