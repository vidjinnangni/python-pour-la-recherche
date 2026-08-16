"""
Génère un export fictif de questionnaire de satisfaction au travail, au format
brut proche d'un export Qualtrics (colonnes techniques, items de Likert,
item inversé, test d'attention, réponses incomplètes).

Utilisé dans le module 07 (enquêtes et sondages).

Usage :
    python generate_enquete_satisfaction.py

Produit : ../enquete_satisfaction.csv
"""

import numpy as np
import pandas as pd

RNG = np.random.default_rng(42)

N_REPONSES = 260

SECTEURS = ["Industrie", "Commerce", "Services aux entreprises", "Technologies", "Santé"]

# Taille d'entreprise : distribution volontairement différente de la population
# de référence, pour l'exercice de pondération/redressement (module 07).
# Population de référence (fictive, à donner dans l'énoncé) :
#   Petite (<50) : 55% | Moyenne (50-250) : 30% | Grande (>250) : 15%
TAILLES = ["Petite (<50)", "Moyenne (50-250)", "Grande (>250)"]
TAILLES_PROBAS_ECHANTILLON = [0.30, 0.35, 0.35]  # sur-représentation des grandes entreprises

GENRES = ["Femme", "Homme", "Autre / ne se prononce pas"]
GENRES_PROBAS_ECHANTILLON = [0.42, 0.55, 0.03]  # légèrement différent de la population (48/50/2)

LIKERT_LABELS = {
    1: "Pas du tout d'accord",
    2: "Plutôt pas d'accord",
    3: "Neutre",
    4: "Plutôt d'accord",
    5: "Tout à fait d'accord",
}


def tirer_likert(moyenne, n=1):
    """Tire une réponse de Likert (1-5) autour d'une moyenne cible, avec arrondi et bornage."""
    valeurs = np.clip(np.round(RNG.normal(moyenne, 1.0, size=n)), 1, 5).astype(int)
    return valeurs if n > 1 else valeurs[0]


def generer():
    ids = [f"R{str(i).zfill(4)}" for i in range(1, N_REPONSES + 1)]

    dates_debut = pd.Timestamp("2024-03-01") + pd.to_timedelta(
        RNG.integers(0, 30, size=N_REPONSES), unit="D"
    )

    age = np.clip(RNG.normal(38, 10, size=N_REPONSES), 20, 65).astype(int)
    genre = RNG.choice(GENRES, size=N_REPONSES, p=GENRES_PROBAS_ECHANTILLON)
    secteur = RNG.choice(SECTEURS, size=N_REPONSES)
    taille_entreprise = RNG.choice(TAILLES, size=N_REPONSES, p=TAILLES_PROBAS_ECHANTILLON)
    anciennete = np.clip(RNG.normal(6, 5, size=N_REPONSES), 0, 35).round(1)

    # Durée de passation en secondes (questionnaire de ~12 items, ~4-6 min normalement)
    duree = np.clip(RNG.normal(280, 90, size=N_REPONSES), 20, 900).astype(int)

    # Progression : la plupart terminent (100%), certains abandonnent en cours de route
    termine = RNG.random(N_REPONSES) < 0.88
    progression = np.where(
        termine, 100, np.clip(RNG.integers(10, 90, size=N_REPONSES), 10, 90)
    )

    # Items de Likert - une légère tendance centrale par item, bruitée par répondant
    q1_ambiance = tirer_likert(3.6, N_REPONSES)
    q2_reconnaissance = tirer_likert(3.0, N_REPONSES)
    # Item inversé : "Ma charge de travail est trop importante"
    # (plus la note est haute, plus la charge perçue est problématique -> item à retourner
    #  avant de construire un score composite de satisfaction globale)
    q3_charge_travail_inv = tirer_likert(3.3, N_REPONSES)
    q4_evolution = tirer_likert(2.9, N_REPONSES)
    q5_recommandation = tirer_likert(3.5, N_REPONSES)

    # Test d'attention : "Merci de sélectionner 'Plutôt d'accord' pour cette question"
    # La grande majorité répond correctement (4) ; une minorité inattentive répond au hasard.
    attention_ok = RNG.random(N_REPONSES) < 0.92
    q_attention = np.where(attention_ok, 4, RNG.integers(1, 6, size=N_REPONSES))

    commentaire_possible = [
        "L'ambiance générale est agréable, mais les perspectives d'évolution manquent de clarté.",
        "Je me sens peu reconnu(e) dans mon travail au quotidien.",
        "Bonne équipe, charge de travail parfois difficile à gérer.",
        "Rien de particulier à signaler.",
        "Le management pourrait davantage communiquer sur les décisions.",
    ]
    a_commente = RNG.random(N_REPONSES) < 0.4
    commentaire = np.where(
        a_commente,
        RNG.choice(commentaire_possible, size=N_REPONSES),
        None,
    )

    df = pd.DataFrame({
        "repondant_id": ids,
        "date_debut": dates_debut.strftime("%Y-%m-%d"),
        "duree_secondes": duree,
        "progression_pct": progression,
        "termine": termine,
        "age": age,
        "genre": genre,
        "secteur": secteur,
        "taille_entreprise": taille_entreprise,
        "anciennete_annees": anciennete,
        "q1_ambiance": q1_ambiance,
        "q2_reconnaissance": q2_reconnaissance,
        "q3_charge_travail_inv": q3_charge_travail_inv,
        "q4_evolution": q4_evolution,
        "q_attention": q_attention,
        "q5_recommandation": q5_recommandation,
        "commentaire": commentaire,
    })

    # Réponses non terminées : les items après abandon ne sont pas renseignés
    items_fin = ["q4_evolution", "q_attention", "q5_recommandation", "commentaire"]
    non_termine = ~df["termine"]
    for col in items_fin:
        df.loc[non_termine, col] = np.nan

    # Quelques répondants "speeders" (durée anormalement courte) parmi les terminés,
    # utile pour l'exercice de détection de réponses suspectes
    idx_speeders = df[df["termine"]].sample(n=8, random_state=42).index
    df.loc[idx_speeders, "duree_secondes"] = RNG.integers(15, 40, size=len(idx_speeders))

    return df


if __name__ == "__main__":
    df = generer()
    df.to_csv("../enquete_satisfaction.csv", index=False)
    print(f"{len(df)} réponses générées -> ../enquete_satisfaction.csv")
    print(df.head())
