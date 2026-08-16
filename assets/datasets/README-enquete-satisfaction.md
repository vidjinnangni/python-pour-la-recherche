# `enquete_satisfaction.csv`

Export **fictif** d'un questionnaire de satisfaction au travail (260 réponses), au format brut proche d'un export Qualtrics/LimeSurvey réel, avec des colonnes techniques, réponses incomplètes et suspectes. Voir [`scripts/generate_enquete_satisfaction.py`](scripts/generate_enquete_satisfaction.py).

## Utilisé dans le module

- **07 : Enquêtes et sondages** : import, nettoyage, recodage, fiabilité d'échelle, pondération

## Dictionnaire des variables

| Variable | Type | Description |
|---|---|---|
| `repondant_id` | texte | Identifiant unique du répondant |
| `date_debut` | date | Date de passation du questionnaire |
| `duree_secondes` | entier | Durée de passation, en secondes |
| `progression_pct` | entier (10-100) | Pourcentage de progression dans le questionnaire |
| `termine` | booléen | Le répondant a-t-il terminé le questionnaire |
| `age` | entier | Âge du répondant |
| `genre` | texte | Femme / Homme / Autre / ne se prononce pas |
| `secteur` | texte | Secteur d'activité de l'entreprise du répondant |
| `taille_entreprise` | texte | Petite (<50), Moyenne (50-250), Grande (>250) salariés |
| `anciennete_annees` | décimal | Ancienneté dans l'entreprise, en années |
| `q1_ambiance` | Likert 1-5 | "L'ambiance de travail dans mon équipe est bonne" |
| `q2_reconnaissance` | Likert 1-5 | "Mon travail est reconnu à sa juste valeur" |
| `q3_charge_travail_inv` | Likert 1-5 | **Item inversé** : "Ma charge de travail est trop importante" |
| `q4_evolution` | Likert 1-5 | "J'ai de bonnes perspectives d'évolution dans cette entreprise" |
| `q_attention` | Likert 1-5 | **Test d'attention**. Consigne : "Merci de sélectionner 'Plutôt d'accord' pour cette question" (réponse attendue = 4) |
| `q5_recommandation` | Likert 1-5 | "Je recommanderais cette entreprise comme employeur" |
| `commentaire` | texte libre | Commentaire optionnel, souvent manquant |

Échelle de Likert : 1 = Pas du tout d'accord … 5 = Tout à fait d'accord.

## Population de référence (pour l'exercice de pondération)

L'échantillon **sur-représente volontairement** les grandes entreprises et sous-représente légèrement les femmes par rapport à une population de référence fictive donnée pour l'exercice de redressement :

| Variable | Population de référence | Échantillon observé |
|---|---|---|
| Petite entreprise (<50) | 55 % | ~30 % |
| Moyenne entreprise (50-250) | 30 % | ~34 % |
| Grande entreprise (>250) | 15 % | ~36 % |
| Femme | 48 % | ~40 % |
| Homme | 50 % | ~56 % |
| Autre / ne se prononce pas | 2 % | ~4 % |

C'est cet écart qui doit être corrigé par pondération dans l'exercice.

## Particularités

- **~13 % de réponses incomplètes** (`termine = False`) : les items après abandon (`q4_evolution`, `q_attention`, `q5_recommandation`, `commentaire`) sont vides. Cela représente les cas réaliste d'abandon en cours de questionnaire.
- **Item inversé** (`q3_charge_travail_inv`) : à retourner (`6 - valeur`) avant de construire un score composite de satisfaction globale avec `q1`, `q2` et `q4`.
- **Test d'attention** (`q_attention`) : environ 20 % des répondants n'y répondent pas correctement ; à utiliser pour discuter du filtrage (faut-il exclure ces répondants ? tous ? au cas par cas ?).
- **Réponses "speeders"** : quelques répondants ont une durée de passation anormalement courte (moins de 40 secondes pour un questionnaire qui en prend ~280 en moyenne) ; à repérer via `duree_secondes`.
- **Commentaire libre manquant** (~68 % de valeurs manquantes). Cela correspond au taux de réponse habituellement faible aux questions ouvertes.

## Limites

Données **entièrement synthétiques**. Les échelles ne sont pas issues d'un instrument validé et la population de référence utilisée pour la pondération est fictive, construite uniquement pour illustrer la mécanique du redressement.

## Régénérer les données

```bash
cd scripts/
python generate_enquete_satisfaction.py
```

Graine aléatoire fixe (`seed=42`) : exécution reproductible à l'identique.
