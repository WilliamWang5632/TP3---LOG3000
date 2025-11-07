# Module : Styles de la Calculatrice

## Raison d’être
Ce module définit l’apparence visuelle de l’application de calculatrice.  
Il gère la disposition, les couleurs, la typographie et les effets d’interaction afin d’offrir une interface claire, moderne et conviviale.

---

## Contenu du module
### `style.css`
Ce fichier contient toutes les règles CSS du projet.  
Il assure notamment :
- Le **centrage et la mise en page générale** de la calculatrice.  
- Le **style du conteneur principal** (`.calculator`), incluant la couleur, les bordures et les ombres.  
- L’apparence de **l’écran d’affichage** (`#display`).  
- La **mise en forme des boutons** (`.btn`, `.operator`) et leurs effets de survol ou de clic.  

---

## Dépendances et hypothèses
- Ce module suppose que le fichier **HTML principal (`index.html`)** référence correctement `style.css`.  
- Le code HTML contient les éléments attendus :
  - `.calculator` — conteneur principal  
  - `#display` — zone d’affichage des calculs  
  - `.buttons` — grille regroupant les boutons `.btn` et `.operator`  
- Aucune dépendance externe (bibliothèque CSS ou police personnalisée) n’est utilisée.  
- Les styles sont autonomes et compatibles avec une structure HTML simple.

---

## Pour les nouveaux développeurs
Ce répertoire contient **uniquement la feuille de style** utilisée par la calculatrice.  
Il ne comporte **aucun code logique ou fonctionnel** (JavaScript, traitement des entrées, etc.).  
Toute modification ici affecte uniquement **l’apparence visuelle** de l’application.

---

**Auteur(s)** : *William Wang, Kim Desroches, Kimia Foroudian*  
**Dernière mise à jour** : *Vendredi le 7 novembre 2025*  
