"""
Génère un jeu de données fictif d'entreprises en panel (2019-2023).

Utilisé dans les modules 02 (pandas), 03 (visualisation) et 05 (économétrie).

Usage :
    python generate_entreprises_panel.py

Produit : ../entreprises_panel.csv
"""

import numpy as np
import pandas as pd

# Graine fixée pour la reproductibilité (voir module 09)
RNG = np.random.default_rng(42)

N_ENTREPRISES = 80
ANNEES = list(range(2019, 2024))  # 2019 à 2023 inclus

SECTEURS = [
    "Industrie",
    "Commerce",
    "Services aux entreprises",
    "Technologies",
    "Santé",
]
REGIONS = [
    "Île-de-France",
    "Auvergne-Rhône-Alpes",
    "Nouvelle-Aquitaine",
    "Hauts-de-France",
    "Occitanie",
]

def generer_entreprises():
    """Caractéristiques fixes de chaque entreprise (niveau entreprise)."""
    entreprises = pd.DataFrame({
        "entreprise_id": [f"E{str(i).zfill(3)}" for i in range(1, N_ENTREPRISES + 1)],
        "secteur": RNG.choice(SECTEURS, size=N_ENTREPRISES),
        "region": RNG.choice(REGIONS, size=N_ENTREPRISES),
        "annee_creation": RNG.integers(1990, 2019, size=N_ENTREPRISES),
        "teletravail": RNG.choice([0, 1], size=N_ENTREPRISES, p=[0.4, 0.6]),
    })
    # Taille de référence en 2019, servira de point de départ à la trajectoire
    entreprises["effectifs_base"] = RNG.integers(15, 500, size=N_ENTREPRISES)
    entreprises["ca_base"] = entreprises["effectifs_base"] * RNG.uniform(80, 220, size=N_ENTREPRISES)
    return entreprises


def generer_panel(entreprises):
    """Étend chaque entreprise sur plusieurs années avec une trajectoire simulée."""
    lignes = []
    for _, e in entreprises.iterrows():
        effectifs = e["effectifs_base"]
        ca = e["ca_base"]
        for annee in ANNEES:
            # Croissance annuelle bruitée, légèrement plus forte si télétravail=1
            croissance_effectifs = RNG.normal(0.02 + 0.01 * e["teletravail"], 0.05)
            croissance_ca = RNG.normal(0.03 + 0.015 * e["teletravail"], 0.08)

            effectifs = max(3, effectifs * (1 + croissance_effectifs))
            ca = max(50, ca * (1 + croissance_ca))

            rentabilite = RNG.normal(0.08 + 0.02 * e["teletravail"], 0.06)
            satisfaction_rh = np.clip(
                RNG.normal(6.5 + 0.6 * e["teletravail"], 1.4), 1, 10
            )

            lignes.append({
                "entreprise_id": e["entreprise_id"],
                "annee": annee,
                "secteur": e["secteur"],
                "region": e["region"],
                "annee_creation": e["annee_creation"],
                "teletravail": e["teletravail"],
                "effectifs": round(effectifs),
                "chiffre_affaires_keur": round(ca, 1),
                "rentabilite": round(rentabilite, 4),
                "satisfaction_rh": round(satisfaction_rh, 1),
            })

    panel = pd.DataFrame(lignes)

    # Introduire quelques valeurs manquantes réalistes (pour les exercices de nettoyage)
    mask = RNG.random(len(panel)) < 0.03
    panel.loc[mask, "satisfaction_rh"] = np.nan

    # Introduire quelques doublons volontaires (pour les exercices de nettoyage)
    doublons = panel.sample(n=4, random_state=42)
    panel = pd.concat([panel, doublons], ignore_index=True)

    return panel


if __name__ == "__main__":
    entreprises = generer_entreprises()
    panel = generer_panel(entreprises)
    panel = panel.sort_values(["entreprise_id", "annee"]).reset_index(drop=True)
    panel.to_csv("../entreprises_panel.csv", index=False)
    print(f"{len(panel)} lignes générées -> ../entreprises_panel.csv")
    print(panel.head())
