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
    - a (int) : Premier opérande.
    - b (int) : Second opérande.

    Retourne :
    - (float) : La somme des deux valeurs.
    """
    return a + b


def subtract(a, b):
    """
    Soustrait le premier opérande du second.

    Paramètres :
    - a (int) : Valeur à soustraire.
    - b (int) : Valeur de départ.

    Retourne :
    - (float) : Le résultat de a - b.
    """
    return a - b


def multiply(a, b):
    """
    Multiplie deux nombres.

    Paramètres :
    - a (int) : Premier opérande.
    - b (int) : Second opérande.

    Retourne :
    - (float) : Le produit de a et b.
    """
    return a * b  


def divide(a, b):
    """
    Effectue une division entière entre deux nombres.

    Paramètres :
    - a (int) : Numérateur.
    - b (int) : Dénominateur.

    Retourne :
    - (float) : Le quotient entier du calcul (a // b).
    """
    return a // b
