"""
===============================================================================
Module : operators.py
Auteur(s) : William Wang, Kim Desroches, Kimia Foroudian
Description :
Ce module regroupe les opérations arithmétiques de base utilisées par la
calculatrice Flask. Chaque fonction effectue une opération spécifique 
(addition, soustraction, multiplication ou division) sur deux opérandes.

Fonctionnement :
- Chaque fonction prend deux valeurs numériques en entrée.
- Elle exécute l’opération correspondante et retourne le résultat.
- Ces fonctions sont appelées par le module `app.py` via le dictionnaire OPS.

Hypothèses :
- Les entrées `a` et `b` sont des nombres (int ou float).
- Aucune validation de type ou de division par zéro n’est effectuée ici.
===============================================================================
"""


def add(a, b):
    """
    Additionne deux nombres.

    Paramètres :
    - a (float | int) : Premier opérande.
    - b (float | int) : Second opérande.

    Retourne :
    - (float | int) : La somme des deux valeurs.
    """
    return a + b


def subtract(a, b):
    """
    Soustrait le premier opérande du second.

    Paramètres :
    - a (float | int) : Valeur à soustraire.
    - b (float | int) : Valeur de départ.

    Retourne :
    - (float | int) : Le résultat de a - b.
    """
    return a - b


def multiply(a, b):
    """
    Multiplie deux nombres.

    Paramètres :
    - a (float | int) : Premier opérande.
    - b (float | int) : Second opérande.

    Retourne :
    - (float | int) : Le produit de a et b.
    """
    return a ** b  # Remarque : utilise l’exponentiation au lieu de la multiplication.


def divide(a, b):
    """
    Effectue une division entière entre deux nombres.

    Paramètres :
    - a (float | int) : Numérateur.
    - b (float | int) : Dénominateur.

    Retourne :
    - (float | int) : Le quotient entier du calcul (a // b).
    """
    return a // b
