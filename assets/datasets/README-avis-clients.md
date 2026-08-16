# `avis_clients.csv`

Corpus **fictif** de 300 avis clients (306 lignes avec doublons volontaires), générés par assemblage de fragments de phrases. Voir [`scripts/generate_avis_clients.py`](scripts/generate_avis_clients.py).

## Utilisé dans le module

- **06 : Texte et scraping** : nettoyage de texte, analyse de fréquence, analyse de sentiment

## Dictionnaire des variables

| Variable | Type | Description |
|---|---|---|
| `avis_id` | texte | Identifiant unique de l'avis (`A0001` à `A0300`) |
| `entreprise_id` | texte | Entreprise concernée : mêmes identifiants que [`entreprises_panel.csv`](README-entreprises-panel.md) (`E001` à `E080`), pour permettre de croiser les deux jeux de données si besoin |
| `date` | date (AAAA-MM-JJ) | Date de l'avis, sur l'année 2023 |
| `canal` | texte | Site web, Application mobile, ou Réseaux sociaux |
| `note` | entier (1-5) | Note laissée par le client |
| `texte_avis` | texte | Commentaire libre du client |

## Particularités

- **Note et tonalité du texte sont corrélées, mais pas parfaitement** : une note de 1-2 est généralement associée à un texte négatif, mais pas systématiquement pour que l'analyse de sentiment automatique du module 06 ait un vrai intérêt.
- **~5 % de valeurs manquantes** dans `texte_avis` (avis où le client a laissé une note sans commentaire).
- **6 lignes dupliquées**, pour illustrer un problème fréquent en scraping/collecte (doublons de collecte).
- **Bruit textuel volontaire** sur une partie des avis : MAJUSCULES, espaces multiples ou en début/fin, ponctuation répétée (`!!!`), pour donner un vrai objet de travail aux exercices de nettoyage de texte (normalisation, `strip()`, etc.), plutôt qu'un corpus déjà propre.
- Le texte est composé de **fragments de phrases réutilisés** (pas de génération libre) : cela crée volontairement des répétitions exactes de groupes de mots, utile pour l'exercice de fréquence de mots/expressions, mais à garder en tête. Ce n'est pas un corpus linguistiquement aussi varié qu'un vrai corpus d'avis.

## Limites

Corpus **entièrement synthétique**, construit par assemblage de phrases-types. Il convient bien pour s'exercer aux techniques (nettoyage, fréquence, sentiment).

## Régénérer les données

```bash
cd scripts/
python generate_avis_clients.py
```

Graine aléatoire fixe (`seed=42`) : exécution reproductible à l'identique.
