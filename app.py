"""
===============================================================================
Module : app.py
Auteur(s) : William Wang, Kim Desroches, Kimia Foroudian
Description :
Ce fichier implémente le serveur principal de l’application Flask de calculatrice.
Il gère la logique backend, incluant :
 - La réception et le traitement des requêtes HTTP.
 - Le calcul des expressions arithmétiques via la fonction `calculate()`.
 - Le rendu du gabarit HTML `index.html` avec le résultat du calcul.

Fonctionnement :
1. L’utilisateur saisit une expression dans l’interface web.
2. Flask envoie cette expression au serveur via une requête POST.
3. Le serveur analyse et évalue l’expression.
4. Le résultat (ou un message d’erreur) est retourné à la page web.

Hypothèses :
- Le module `operators` fournit les fonctions : `add`, `subtract`, `multiply` et `divide`.
- Seules les expressions comportant un seul opérateur arithmétique sont prises en charge.
- Le gabarit HTML (`index.html`) attend une variable `result` pour afficher le résultat.
===============================================================================
"""

from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

app = Flask(__name__)

# Dictionnaire associant chaque symbole d’opérateur à sa fonction correspondante.
OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}


def calculate(expr: str):
    """
    Évalue une expression arithmétique simple contenant exactement un opérateur.

    Rôle :
    - Analyser la chaîne reçue.
    - Identifier l’opérateur et séparer les deux opérandes.
    - Convertir les valeurs en flottants.
    - Appeler la fonction d’opération appropriée (add, subtract, etc.).

    Paramètres :
    - expr (str) : L’expression à évaluer (ex. "12+3" ou "7 / 2").

    Retourne :
    - Le résultat numérique de l’opération (type float ou similaire).

    Exceptions :
    - ValueError si l’expression est vide, mal formée ou contient plusieurs opérateurs.
    - ValueError si les opérandes ne sont pas des nombres valides.
    """
    if not expr or not isinstance(expr, str):
        # Vérifie que l’entrée est une chaîne non vide.
        raise ValueError("empty expression")

    # Retire les espaces pour simplifier l’analyse.
    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    # Recherche de l’opérateur dans la chaîne.
    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                # Si un deuxième opérateur est trouvé, l’expression est invalide.
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    # Vérifie que l’opérateur n’est ni au début ni à la fin, et qu’il existe.
    if op_pos <= 0 or op_pos >= len(s) - 1:
        # Empêche les cas comme "+5", "5+", ou l’absence d’opérateur.
        raise ValueError("invalid expression format")

    # Séparation des deux opérandes.
    left = s[:op_pos]
    right = s[op_pos + 1:]

    try:
        # Conversion des opérandes en nombres flottants.
        a = float(left)
        b = float(right)
    except ValueError:
        # Si la conversion échoue, l’expression contient des caractères non numériques.
        raise ValueError("operands must be numbers")

    # Appelle la fonction correspondant à l’opérateur et retourne le résultat.
    return OPS[op_char](a, b)


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Route principale de l’application Flask.

    Rôle :
    - En mode GET : afficher la page de la calculatrice avec un champ vide.
    - En mode POST : lire l’expression saisie, la calculer et afficher le résultat.

    Entrées :
    - Méthode HTTP : GET ou POST.
    - Donnée de formulaire : champ 'display' contenant l’expression.

    Sorties :
    - Rendu HTML du gabarit 'index.html' avec une variable 'result' contenant :
      • le résultat du calcul, ou
      • un message d’erreur.
    """
    result = ""
    if request.method == 'POST':
        # Récupère l’expression envoyée depuis le formulaire HTML.
        expression = request.form.get('display', '')
        try:
            # Tente d’évaluer l’expression saisie.
            result = calculate(expression)
        except Exception as e:
            # Capture toute erreur et la renvoie sous forme de message texte.
            result = f"Error: {e}"

    # Affiche la page HTML avec le résultat (ou vide par défaut).
    return render_template('index.html', result=result)


if __name__ == '__main__':
    # Lancement du serveur Flask en mode développement.
    app.run(debug=True)
