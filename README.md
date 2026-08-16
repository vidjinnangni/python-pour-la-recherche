# Python pour la recherche en sciences de gestion

![Python pour la recherche](/docs/images/banner_image.png)

**Ressources pour apprendre à utiliser Python comme outil de recherche en sciences de gestion**. Elles couvrent : le traitement de données, les statistiques, l'économétrie, le texte, les enquêtes, avec une introduction au machine learning.

## Pourquoi Python ?

En sciences de gestion, la recherche quantitative repose historiquement sur des outils comme Excel, IBM SPSS Statistics, Stata ou R. Mais Python s'est imposé comme une alternative, voire un complément, grâce à sa **syntaxe simple et lisible**.

**Autres avantages :**

- **Un seul outil pour tout le pipeline de recherche :** collecte de données (scraping, API), nettoyage, statistiques, économétrie, machine learning et visualisation, sans changer de logiciel à chaque étape.
- **Reproductibilité :** un notebook Python documente et exécute chaque étape de l'analyse. Cela facilite la relecture par les pairs et la réplication.
- **Passage à l'échelle :** contrairement à Excel, Python gère sans effort des jeux de données volumineux (grandes enquêtes, données de panel, données textuelles massives).
- **Un écosystème riche et gratuit :** `pandas`, `statsmodels`, `scikit-learn`, etc. couvrent l'essentiel des besoins d'un chercheur en gestion, sans licence payante (contrairement à Stata ou SPSS).
- **Une compétence transférable :** au-delà de la recherche, Python est largement utilisé en entreprise (data analyse, reporting). Il s'agit donc d'une compétence valorisable au-delà du seul cadre académique.

> Bien évidemment, Python ne remplace pas R ou Stata en toutes circonstances. L'objectif est de vous donner les moyens de choisir l'outil adapté à chaque situation, en connaissant bien celui-ci.

## À qui s'adresse ce cours ?

- Doctorant.e.s, chercheur.se.s et étudiant.e.s en sciences de gestion.
- **Niveau :** de débutant à intermédiaire. Aucune expérience en programmation n'est requise pour commencer.

> [!NOTE]
> Chaque module est autonome et peut être suivi dans l'ordre ou en fonction de vos besoins.

## Objectifs

Ces ressources vous permettront de savoir :

- manipuler, nettoyer et croiser des jeux données avec la bibliothèque Python `Pandas` ;
- produire des visualisations claires pour vos articles et présentations ;
- réaliser des statistiques descriptives et des tests d'hypothèses ;
- estimer des modèles économétriques (régressions, données de panel) ;
- collecter et analyser des données textuelles (scrapping, text mining) ;
- traiter des données d'enquêtes/sondages ;
- structurer un projet de recherche reproductible.

## Structure

```text
python-pour-la-recherche/
├── README.md                     # ce fichier
├── requirements.txt              # dépendances pip
├── environment.yaml              # dépendances conda (optionnel)
├── docs/
│   └── roadmap.md                # parcours conseillés selon votre profil/objectif
├── assets/
│   └── datasets/                 # jeux de données utilisés dans les modules
├── modules/
│   ├── 00-prise-en-main/
│   ├── 01-fondamentaux-python/
│   ├── 02-pandas-donnees/
│   ├── 03-visualisation/
│   ├── 04-stats-descriptives-inferentielles/
│   ├── 05-econometrie/
│   ├── 06-texte-scraping/
│   ├── 07-enquetes-sondages/
│   ├── 08-machine-learning-intro/
│   └── 09-reproductibilite/
└── solutions/                    # corrigés des exercices, par module
```

Chaque module est composé :

- d'un fichier `README.md` avec les objectifs, les prérequis et la durée estimée ;
- d'un notebook de cours (`.ipynb`) ;
- d'un dossier `exercices/` ;
- du corrigé des exercices dans le dossier `solutions/<numero-module>/`.

## Comment naviguer dans le cours ?

Pour commencer, consultez [`docs/ROADMAP.md`](/docs/ROADMAP.md) pour des parcours conseillés selon votre objectif. Si vous n'avez pas d'objectif spécifique, vous pouvez suivre les modules dans l'ordre (`00` → `09`) pour une progression cohérente.

## Installation

Vous avez deux (02) options pour suivre ce cours. **Si vous débutez, commencez par l'option A**. Elle ne nécessite aucune installation.

### Option A : Google Colab (recommandé pour débuter)

[Google Colab](https://colab.research.google.com/) est un service gratuit de Google qui exécute des notebooks Jupyter directement dans votre navigateur, sans rien installer sur votre ordinateur. Tout ce dont vous avez besoin, c'est un compte Google.

![Google Colab](/docs/images/interface-google-colab.png)

### Option B : Installation locale sur votre ordinateur

Cette option est plus confortable sur la durée (pas besoin de réimporter les fichiers à chaque fois), mais demande un peu plus de mise en place. Elle suppose que vous savez ouvrir un terminal (l'application « Terminal » sur Mac, « Invite de commandes » ou « PowerShell » sur Windows ou le terminal intégré si vous utilisez déjà VS Code).

**Prérequis : avoir Python installé.** Vérifiez si c'est déjà le cas en tapant dans votre terminal :

```bash
python3 --version
```

Si vous obtenez un numéro de version (ex. `Python 3.11.4`), c'est bon, passez à l'étape suivante. Sinon, installez Python depuis [python.org/downloads](https://www.python.org/downloads/) (choisissez une version 3.10 ou plus récente), puis relancez la vérification.

#### 1. Cloner le repo

Le plus simple si vous découvrez Git : téléchargez le repo en `.zip` depuis GitHub (Cliquez sur le bouton bleu **"Code"** puis sur le lien **"Download ZIP"** en haut de la page du repo), puis décompressez-le où vous voulez sur votre ordinateur.

![Télécharger le repo](/docs/images/download-zip.png)

Si vous êtes à l'aise avec Git (voir le module [00-prise-en-main](modules/00-prise-en-main/) pour l'essentiel à connaître) :

```bash
git clone https://github.com/vidjinnangni/python-pour-la-recherche.git
```

Ensuite, dans votre terminal, déplacez-vous dans le dossier du repo :

```bash
cd chemin/vers/python-pour-la-recherche
```

#### 2. Créer un environnement virtuel et installer les dépendances

Un **environnement virtuel** est un espace isolé où seront installées les bibliothèques de ce cours, sans interférer avec d'autres projets Python sur votre machine. C'est une bonne pratique !

```bash
# Créer l'environnement (une seule fois)
python3 -m venv venv
 
# Activer l'environnement (à refaire à chaque nouvelle session de travail)
source venv/bin/activate        # sur Mac / Linux
venv\Scripts\activate           # sur Windows
 
# Installer les bibliothèques du cours (une seule fois, une fois l'environnement activé)
pip install -r requirements.txt
```

Vous saurez que l'environnement est activé si son nom (`venv`) apparaît entre parenthèses au début de la ligne de commande dans votre terminal.

*Vous utilisez déjà conda plutôt que pip ? Remplacez cette étape par :*

```bash
conda env create -f environment.yml
conda activate python-recherche-gestion
```

#### 3. Lancer Jupyter

Une fois l'environnement activé (étape précédente) :

```bash
jupyter lab
```

Cette commande ouvre automatiquement un onglet dans votre navigateur avec l'interface JupyterLab. Dans le panneau de gauche, naviguez jusqu'au module voulu (ex. `modules/00-prise-en-main/`) et double-cliquez sur le fichier `.ipynb` pour l'ouvrir.

Pour arrêter Jupyter, retournez dans le terminal et faites `Ctrl + C`.

**La prochaine fois** que vous voulez travailler sur le cours, vous n'aurez plus qu'à refaire les étapes 2 (activer l'environnement, sans le recréer) et 3 (lancer `jupyter lab`). Il n'est plus nécessaire" de tout réinstaller.

## Jeux de données

Les jeux de données utilisées dans les modules se trouvent dans `assets/datasets/`. Ils sont soit fictifs (créés pour l'exercice), soit issus de sources ouvertes citées dans le README de chaque module.

## Contribuer

Ces ressources sont amenées à évoluer. Les suggestions, corrections et retours sont les bienvenus.

## Licence

Les ressources de ce repo sont distribuées sous double licence :

- Licence [CC-BY-4.0](LICENCE), pour le contenu pédagogique ;
- Licence [MIT](LICENSE-CODE), pour le code (notebooks, scripts, snippets).

---

Le logo Python est une marque déposée de la *Python Software Foundation*.
