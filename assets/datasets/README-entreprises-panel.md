# `entreprises_panel.csv`

Jeu de données **fictif** représentant un panel de 80 entreprises suivies sur 5 ans (2019-2023). Généré synthétiquement. Voir [`scripts/generate_entreprises_panel.py`](scripts/generate_entreprises_panel.py).

## Utilisé dans les modules

- **02 : Pandas et données** : exploration, nettoyage, `groupby`
- **03 : Visualisation** : graphiques (évolution, comparaison par secteur)
- **05 : Économétrie** : régression multiple, modèle à effets fixes sur données de panel

## Dictionnaire des variables

| Variable | Type | Description |
|---|---|---|
| `entreprise_id` | texte | Identifiant unique de l'entreprise (`E001` à `E080`) |
| `annee` | entier | Année d'observation (2019 à 2023) |
| `secteur` | texte | Secteur d'activité (Industrie, Commerce, Services aux entreprises, Technologies, Santé) |
| `region` | texte | Région du siège social |
| `annee_creation` | entier | Année de création de l'entreprise |
| `teletravail` | 0/1 | L'entreprise pratique-t-elle le télétravail (variable fixe dans le temps) |
| `effectifs` | entier | Nombre de salariés cette année-là |
| `chiffre_affaires_keur` | décimal | Chiffre d'affaires annuel, en milliers d'euros |
| `rentabilite` | décimal | Taux de rentabilité (ex. 0.08 = 8 %) |
| `satisfaction_rh` | décimal (1-10) | Score de satisfaction des salariés, contient des valeurs manquantes |

## Particularités

- **8 valeurs manquantes** sur `satisfaction_rh` (~2 %), pour les exercices de nettoyage du module 02.
- **4 lignes dupliquées**, pour les exercices de détection de doublons du module 02.
- **Effet `teletravail` intégré mais bruité** : les entreprises avec `teletravail = 1` ont en moyenne une croissance, une rentabilité et une satisfaction RH légèrement supérieures, mais avec suffisamment de bruit pour que ce ne soit pas trivialement significatif. Cela permet d'illustrer un vrai test d'hypothèse ou une régression (modules 04 et 05).

## Limites

Ces données sont **entièrement synthétiques**. Les corrélations qu'on y observe (ex. lien télétravail/performance) sont construites pour l'exercice et ne doivent pas être interprétées comme un résultat de recherche réel.

## Régénérer les données

```bash
cd scripts/
python generate_entreprises_panel.py
```

Le script utilise une graine aléatoire fixe (`seed=42`), donc l'exécution est reproductible à l'identique.
