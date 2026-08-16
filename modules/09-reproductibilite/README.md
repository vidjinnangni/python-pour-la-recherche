# Module 09 : Reproductibilité

## Objectifs

À la fin de ce module, vous saurez :

- bien structurer un projet de recherche Python ;
- séparer données brutes, données transformées, code et résultats ;
- documenter votre code et vos choix méthodologiques ;
- geler vos dépendances pour garantir que votre analyse reste exécutable dans le temps ;
- utiliser Git pour versionner votre projet de recherche ;
- comprendre les attentes actuelles des revues et institutions en matière de reproductibilité.

Ce module est transversal. Il s'applique quel que soit votre parcours (économétrie, texte, enquêtes, ML). Il est recommandé une fois que vous avez un vrai projet de recherche entre les mains, pas nécessairement à la fin du cours.

## Prérequis

Tronc commun (modules 00 à 03). L'idéal serait d'avoir déjà un projet de recherche en cours pour appliquer directement les principes.

## Durée estimée

3 à 5 heures.

## Contenu du module

1. **L'importance de la reproductibilité**
   - Attentes des revues (données et code disponibles, *open science*)
   - Se relire soi-même six mois plus tard
   - Faciliter la relecture par des coauteurs ou des relecteurs

2. **Structurer un projet de recherche**
   - Séparer `data/raw/` (jamais modifié), `data/processed/`, `notebooks/`, `scripts/`, `outputs/`
   - Nommer ses fichiers et dossiers de façon cohérente
   - Un exemple de structure de projet type, transposable à votre propre recherche

3. **Documenter**
   - Un bon README de projet : objectif, comment reproduire l'analyse
   - Bien documenter son code
   - Documenter les choix méthodologiques directement dans les notebooks (cellules Markdown)

4. **Geler son environnement**
   - Pourquoi figer les versions des bibliothèques (`requirements.txt` avec versions, comme dans ce repo)
   - Durabilité : un notebook qui tourne aujourd'hui doit encore tourner dans 3 ans

5. **Git pour son propre projet**
   - Rappel : `clone`/`pull` (vu au module 00) suffisent pour suivre ce cours, mais pas pour gérer votre propre recherche
   - `git add`, `git commit`, `git push` : sauvegarder l'historique de son travail
   - Un `.gitignore` adapté à un projet de recherche (données sensibles, gros fichiers)
   - *Aperçu* : partager son code via un repo GitHub public au moment de la publication

6. **Reproductibilité des résultats numériques**
   - Fixer les graines aléatoires (*random seed*) pour les analyses impliquant du tirage aléatoire (ML, bootstrap)
   - Consigner précisément les versions de Python et des bibliothèques utilisées dans l'article/le rapport

## Pour commencer

Ouvrez le notebook [`09-reproductibilite.ipynb`](09-reproductibilite.ipynb) de ce module.

## Exercices

Voir le dossier [`exercices/`](exercices/) :

- Exercice 1 : réorganiser un projet "en vrac" fourni selon une structure claire
- Exercice 2 : écrire un README de projet complet pour une analyse fictive
- Exercice 3 : figer un environnement (`requirements.txt`) pour un projet donné
- Exercice 4 : initialiser un repo Git pour un projet et faire ses premiers commits

Corrigés disponibles dans [`solutions/09-reproductibilite/`](../../solutions/09-reproductibilite/).

## Aller plus loin (optionnel)

- [The Turing Way](https://the-turing-way.netlify.app/), guide complet sur la recherche reproductible (en anglais)
- [Documentation officielle Git](https://git-scm.com/doc)
- [Cookiecutter Data Science](https://cookiecutter-data-science.drivendata.org/), modèle de structure de projet

## Suite

Ce module clôt le tronc commun de compétences transversales. Retournez à la [roadmap](../../docs/roadmap.md) si vous souhaitez explorer un autre parcours thématique.
