"""
Génère un corpus fictif d'avis clients pour le module 06 (texte et scraping).

Les avis sont construits par assemblage de fragments de phrases (positifs,
négatifs, neutres), avec du bruit volontaire (fautes, espaces, casse) pour
alimenter les exercices de nettoyage de texte.

Usage :
    python generate_avis_clients.py

Produit : ../avis_clients.csv
"""

import numpy as np
import pandas as pd

RNG = np.random.default_rng(42)

N_AVIS = 300
CANAUX = ["Site web", "Application mobile", "Réseaux sociaux"]

# Fragments de phrases par tonalité, pour composer des avis réalistes et variés
FRAGMENTS_POSITIFS = [
    "Le service client a été très réactif.",
    "Livraison rapide, je suis très satisfait.",
    "Le rapport qualité-prix est excellent.",
    "L'équipe a été à l'écoute de mes besoins.",
    "Je recommande vivement cette entreprise.",
    "Un accompagnement personnalisé et efficace.",
    "Très bonne expérience du début à la fin.",
    "Le produit correspond parfaitement à mes attentes.",
]

FRAGMENTS_NEGATIFS = [
    "Le délai de livraison a été beaucoup trop long.",
    "Le service après-vente n'a jamais répondu.",
    "Je suis déçu par la qualité du produit.",
    "Le prix ne correspond pas du tout à la qualité.",
    "Personne n'a pris en charge ma réclamation.",
    "Une expérience décevante, je ne recommande pas.",
    "Le site est peu clair et difficile à utiliser.",
    "Trop d'erreurs dans le traitement de ma commande.",
]

FRAGMENTS_NEUTRES = [
    "Rien à signaler de particulier.",
    "Le produit correspond à la description.",
    "Livraison dans les délais annoncés.",
    "Une expérience correcte, sans plus.",
    "Le service est standard, comme ailleurs.",
]


def composer_avis(tonalite):
    """Compose un avis en assemblant 1 à 3 fragments selon la tonalité."""
    if tonalite == "positif":
        fragments = RNG.choice(FRAGMENTS_POSITIFS, size=RNG.integers(1, 3), replace=False)
    elif tonalite == "negatif":
        fragments = RNG.choice(FRAGMENTS_NEGATIFS, size=RNG.integers(1, 3), replace=False)
    else:
        fragments = RNG.choice(FRAGMENTS_NEUTRES, size=RNG.integers(1, 2), replace=False)
    return " ".join(fragments)


def ajouter_bruit(texte):
    """Introduit du bruit réaliste (espaces multiples, casse, ponctuation) pour ~25% des avis."""
    if RNG.random() < 0.10:
        texte = texte.upper()
    if RNG.random() < 0.15:
        texte = texte.replace(". ", ".  ")  # double espace
    if RNG.random() < 0.10:
        texte = "  " + texte + "   "  # espaces en début/fin
    if RNG.random() < 0.08:
        texte = texte + "!!!"
    return texte


def generer():
    entreprise_ids = [f"E{str(i).zfill(3)}" for i in range(1, 81)]  # cohérent avec entreprises_panel.csv

    lignes = []
    for i in range(1, N_AVIS + 1):
        # Note et tonalité corrélées (une note basse va avec un avis plutôt négatif, pas toujours)
        note = RNG.integers(1, 6)
        if note <= 2:
            tonalite = RNG.choice(["negatif", "neutre"], p=[0.85, 0.15])
        elif note == 3:
            tonalite = RNG.choice(["negatif", "neutre", "positif"], p=[0.3, 0.4, 0.3])
        else:
            tonalite = RNG.choice(["positif", "neutre"], p=[0.85, 0.15])

        texte = composer_avis(tonalite)
        texte = ajouter_bruit(texte)

        lignes.append({
            "avis_id": f"A{str(i).zfill(4)}",
            "entreprise_id": RNG.choice(entreprise_ids),
            "date": pd.Timestamp("2023-01-01") + pd.Timedelta(days=int(RNG.integers(0, 365))),
            "canal": RNG.choice(CANAUX),
            "note": note,
            "texte_avis": texte,
        })

    avis = pd.DataFrame(lignes)

    # Quelques valeurs manquantes réalistes dans le texte (avis avec juste une note, sans commentaire)
    mask_vide = RNG.random(len(avis)) < 0.05
    avis.loc[mask_vide, "texte_avis"] = np.nan

    # Quelques doublons volontaires (copier-coller d'avis, cas fréquent en vrai)
    doublons = avis.sample(n=6, random_state=42)
    avis = pd.concat([avis, doublons], ignore_index=True)

    avis["date"] = avis["date"].dt.strftime("%Y-%m-%d")
    return avis.sort_values("date").reset_index(drop=True)


if __name__ == "__main__":
    avis = generer()
    avis.to_csv("../avis_clients.csv", index=False)
    print(f"{len(avis)} avis générés -> ../avis_clients.csv")
    print(avis.head())
