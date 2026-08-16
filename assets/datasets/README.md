# Jeux de données du cours

Tous les jeux de données de ce dossier sont **fictifs/synthétiques**, générés spécifiquement pour ce cours (voir `scripts/`). Aucun ne provient de vraies entreprises ou de vrais répondants.

## Jeux de données disponibles

| Fichier | Modules concernés | Description |
|---|---|---|
| [`entreprises_panel.csv`](README-entreprises-panel.md) | 02, 03, 05 | Panel de 80 entreprises sur 5 ans (effectifs, CA, rentabilité, télétravail) |
| [`avis_clients.csv`](README-avis-clients.md) | 06 | Corpus de 300 avis clients fictifs pour l'analyse de texte |
| [`enquete_satisfaction.csv`](README-enquete-satisfaction.md) | 07 | Export fictif de questionnaire de satisfaction (260 réponses, échelles de Likert) |

## Principe

Chaque jeu de données est accompagné :

- d'un README dédié avec dictionnaire des variables
- d'un script de génération reproductible dans `scripts/`, avec graine aléatoire (*random seed*) fixée
