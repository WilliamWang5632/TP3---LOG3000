# Module : Interface de la Calculatrice Flask

## Raison d’être
Ce module contient la page HTML principale de la calculatrice.  
Il fournit la structure visuelle et interactive de l’application côté client.  
Le but est de permettre à l’utilisateur d’interagir avec la calculatrice via une interface simple, tout en déléguant le traitement des opérations au serveur Flask.

---

## Contenu du module
### index.html
Ce fichier définit :
- Le **formulaire principal** de la calculatrice, qui envoie les données au serveur Flask via la méthode POST.  
- La **zone d’affichage** (`#display`), utilisée pour montrer la saisie et les résultats.  
- Les **boutons de saisie** (nombres, opérateurs, actions).  
- Un petit **script JavaScript intégré** pour gérer l’affichage côté client (ajout et effacement des valeurs).  
- L’intégration de la feuille de style `style.css` depuis le répertoire `static/`.

---

## Dépendances et hypothèses
- Le projet repose sur un **serveur Flask** côté Python.  
- Ce fichier HTML utilise la fonction Jinja2 `url_for()` pour charger la feuille de style statique.  
- La variable `result` est transmise par Flask au moment du rendu de la page.  
- Aucune bibliothèque externe n’est requise.  
- Les fonctionnalités de calcul sont gérées par Flask, non par JavaScript.

---

## Informations complémentaires
Ce répertoire ne contient **que le fichier HTML** responsable de l’interface utilisateur.  
Les styles se trouvent dans le répertoire `static/`, et la logique du serveur est gérée par les fichiers Python du projet.

---

**Auteur(s)** : *William Wang, Kim Desroches, Kimia Foroudian*  
**Dernière mise à jour** : *Vendredi le 7 novembre 2025*
