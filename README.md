# Flask Calculator

## Informations du projet

**Nom du projet :** Flask Calculator  
**Numéro d'équipe :** 20  
**Cours :** LOG3000

## Table des matières

- [Description du projet](#description-du-projet)
- [Portée et objectifs](#portée-et-objectifs)
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Lancement de l'application](#lancement-de-lapplication)
- [Utilisation](#utilisation)
- [Architecture du projet](#architecture-du-projet)
- [Tests](#tests)
- [Flux de contribution](#flux-de-contribution)
- [Équipe](#équipe)
- [Licence](#licence)

## Description du projet

Flask Calculator est une application web développée avec le framework Flask permettant d'effectuer des opérations arithmétiques de base via une interface web minimaliste et intuitive.

Le projet a été conçu dans le cadre du cours LOG3000 avec pour objectifs de :
- Corriger et améliorer une base de code existante
- Documenter l'ensemble des composants du projet
- Mettre en place un flux de développement collaboratif
- Appliquer les bonnes pratiques de gestion de versions et de maintenance logicielle

### Fonctionnalités supportées

- **Addition** : Additionner deux ou plusieurs nombres
- **Soustraction** : Soustraire des nombres
- **Multiplication** : Multiplier des nombres
- **Division** : Diviser des nombres (avec gestion des divisions par zéro)

## Portée et objectifs

Ce projet illustre la création et la maintenance d'une application web full-stack simple. Il démontre l'interaction entre :

- **Backend Python** : Serveur Flask qui traite les requêtes HTTP et exécute les calculs
- **Frontend HTML/CSS/JS** : Interface utilisateur pour saisir les expressions et afficher les résultats
- **Logique métier** : Module Python (`operators.py`) contenant les fonctions arithmétiques

### Objectifs pédagogiques

1. **Correction de bogues** : Identifier et corriger les erreurs présentes dans le code initial
2. **Documentation** : Documenter clairement le code, les modules et les interfaces
3. **Collaboration** : Mettre en place un workflow Git structuré avec branches, pull requests et revues de code
4. **Maintenabilité** : Permettre à un nouveau développeur de comprendre et exécuter le projet sans aide externe
5. **Tests** : Implémenter des tests unitaires pour assurer la qualité du code

## Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants installés sur votre machine :

- **Python** : Version 3.7 ou supérieure
- **pip** : Gestionnaire de paquets Python (généralement inclus avec Python)
- **Git** : Système de contrôle de versions
- **Navigateur web moderne** : Chrome, Firefox, Edge ou Safari

### Vérifier les installations

```
Flask==2.3.0
pytest==7.4.0
```

## Lancement de l'application

### 1. Crée un environnement virtuel
Si ce n'est pas déjà fait, créez l'environnement virtuel :

**Windows :**
```bash
python -m venv venv
```
**macOS / Linux :**
```bash
python3 -m venv venv
```

### 2. Activer l'environnement virtuel

**Windows :**
```bash
venv\Scripts\activate
```

**macOS / Linux :**
```bash
source venv/bin/activate
```

### 3. Démarrer le serveur Flask

```bash
python app.py
```

Vous devriez voir un message similaire à :

```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

### 4. Accéder à l'application

Ouvrez votre navigateur web et accédez à :

```
http://localhost:5000
```

ou

```
http://127.0.0.1:5000
```

### 4. Arrêter le serveur

Pour arrêter le serveur, appuyez sur `Ctrl+C` dans le terminal.

## Utilisation

### Interface utilisateur

L'application présente une interface de calculatrice simple avec :

- **Champ de saisie** : Zone de texte pour entrer votre expression arithmétique
- **Bouton « = »** : Déclenche le calcul de l'expression
- **Zone de résultat** : Affiche le résultat ou un message d'erreur

### Saisir une expression

Les expressions peuvent contenir :
- **Nombres** : Entiers (ex: `42`)
- **Opérateurs** : `+`, `-`, `*`, `/`
- **Symbole d’exécution** : `=` 

### Exemples d'utilisation

| Expression | Résultat attendu | Description |
|------------|------------------|-------------|
| `2 + 3` | `5.0` | Addition simple |
| `10 - 4` | `6.0` | Soustraction |
| `6 * 7` | `42.0` | Multiplication |
| `12 / 3` | `4.0` | Division |
| `5 + 3 * 2` | Erreur | Calcul trop complexe |
| `10 / 0` | Erreur | Division par zéro |

### Gestion des erreurs

L'application gère les cas d'erreur suivants :

- **Division par zéro** : Message d'erreur approprié
- **Expression invalide** : Notification lorsque l'expression ne peut être évaluée
- **Opérateurs non supportés** : Avertissement si un opérateur n'est pas reconnu

## Architecture du projet

```
TP3---LOG3000/
│
├── app.py                 # Point d'entrée de l'application Flask
├── operators.py           # Module contenant les fonctions arithmétiques
│
├── templates/
│   └── index.html         # Template HTML de l'interface utilisateur
│
├── static/
│   └── style.css          # Feuille de style CSS
│
├── tests/                 # Dossier des tests unitaires (à venir)
│   ├── __init__.py
│   ├── test_operators.py  # Tests des fonctions arithmétiques
│   └── test_app.py        # Tests des routes Flask
│
├── venv/                  # Environnement virtuel (ignoré par Git)
│
├── .gitignore             # Fichiers et dossiers à ignorer par Git
├── requirements.txt       # Liste des dépendances Python
└── README.md              # Documentation du projet
```

### Description des fichiers principaux

#### `app.py`

Fichier principal de l'application Flask contenant :
- Configuration du serveur Flask
- Définition des routes HTTP
- Logique de traitement des requêtes
- Gestion des erreurs

#### `operators.py`

Module contenant les fonctions arithmétiques de base :
- `add(a, b)` : Addition
- `subtract(a, b)` : Soustraction
- `multiply(a, b)` : Multiplication
- `divide(a, b)` : Division avec gestion des erreurs

#### `templates/index.html`

Template HTML contenant :
- Structure de la page
- Formulaire de saisie
- Scripts JavaScript pour la communication avec le backend

#### `static/style.css`

Feuille de style définissant :
- Mise en page de l'interface
- Styles visuels de la calculatrice
- Responsivité pour différents écrans

## Tests

### Structure des tests

Les tests sont organisés dans le dossier `tests/` et utilisent le framework `pytest`.

```
tests/
├── __init__.py
├── test_operators.py      # Tests unitaires des fonctions arithmétiques
└── test_app.py            # Tests d'intégration des routes Flask
```

### Installation des dépendances de test

```bash
pip install pytest pytest-flask
```

### Exécuter tous les tests

```bash
pytest
```

### Exécuter des tests spécifiques

```bash
# Tester uniquement le module operators
pytest tests/test_operators.py

# Tester uniquement les routes Flask
pytest tests/test_app.py

# Exécuter avec plus de détails
pytest -v

# Afficher la couverture de code
pytest --cov=. --cov-report=html
```

### Types de tests

1. **Tests unitaires** (`test_operators.py`)
   - Validation des opérations arithmétiques
   - Gestion des cas limites (division par zéro, etc.)
   - Tests avec différents types de nombres

2. **Tests d'intégration** (`test_app.py`)
   - Tests des routes Flask
   - Validation des réponses HTTP
   - Tests de l'interface utilisateur

3. **Tests de validation** (à venir)
   - Tests end-to-end
   - Validation de l'expérience utilisateur complète

### Bonnes pratiques de test

- Tous les nouveaux codes doivent être accompagnés de tests
- Viser une couverture de code minimale de 80%
- Tester les cas normaux ET les cas d'erreur
- Utiliser des noms de test descriptifs

## Flux de contribution

### Workflow Git

Ce projet utilise un workflow Git basé sur les branches avec revue de code obligatoire.

### 1. Conventions de nommage des branches

Les branches doivent suivre le format : `<type>/<description-courte>`

| Type | Description | Exemple |
|------|-------------|---------|
| `feature/` | Nouvelle fonctionnalité | `feature/add-square-root` |
| `fix/` | Correction de bogue | `fix/division-by-zero` |
| `docs/` | Modification de documentation | `docs/update-readme` |
| `test/` | Ajout ou modification de tests | `test/add-operator-tests` |
| `refactor/` | Refactorisation sans changement de fonctionnalité | `refactor/simplify-calculator` |

### 2. Créer une nouvelle branche

```bash
# S'assurer d'être sur la branche principale et à jour
git checkout main
git pull origin main

# Créer et basculer sur une nouvelle branche
git checkout -b feature/ma-fonctionnalite
```

### 3. Développement

```bash
# Faire vos modifications
# ...

# Ajouter les fichiers modifiés
git add .

# Faire un commit avec un message descriptif
git commit -m "feat: add a square root function"
```

### 4. Conventions de messages de commit

Utiliser le format suivant : `<type>: <description>`

**Types de commit :**
- `feat`: Nouvelle fonctionnalité
- `fix`: Correction de bogue
- `docs`: Documentation
- `test`: Tests
- `refactor`: Refactorisation
- `style`: Formatage, point-virgules manquants, etc.
- `chore`: Maintenance, mise à jour des dépendances

**Exemples :**
```bash
git commit -m "feat: add modulo operation"
git commit -m "fix: fix division by zero"
git commit -m "docs: update installation guide"
git commit -m "test: add tests for multiplication"
```

### 5. Pousser les changements

```bash
# Pousser la branche vers GitHub
git push origin feature/my-functionality
```

### 6. Créer une Pull Request

1. Aller sur le dépôt GitHub
2. Cliquer sur **« Pull requests »** puis **« New pull request »**
3. Sélectionner votre branche comme source
4. Remplir le template de PR avec :
   - **Description** : Qu'est-ce qui a été fait et pourquoi
   - **Tests effectués** : Comment vous avez vérifié que ça fonctionne
   - **Captures d'écran** : Si applicable
   - **Issues liées** : Référencer les issues concernées (ex: `Closes #42`)

### 7. Revue de code

- Au moins **un membre de l'équipe** doit approuver la PR
- Répondre aux commentaires et apporter les corrections demandées
- Une fois approuvée, la PR peut être fusionnée dans `main`

### 8. Issues et suivi

#### Créer une issue

Pour signaler un bogue ou proposer une fonctionnalité :

1. Aller dans l'onglet **« Issues »**
2. Cliquer sur **« New issue »**
3. Utiliser un titre clair et descriptif
4. Fournir tous les détails nécessaires

#### Labels recommandés

- `bug` : Quelque chose ne fonctionne pas
- `enhancement` : Nouvelle fonctionnalité ou amélioration
- `documentation` : Documentation à améliorer
- `good first issue` : Bon pour les nouveaux contributeurs
- `help wanted` : Aide souhaitée
- `priority: high` : Priorité élevée

### 9. Bonnes pratiques

- **Commits atomiques** : Un commit = une modification logique
- **Branches courtes** : Fusionner rapidement pour éviter les conflits
- **Tests avant PR** : Toujours exécuter les tests localement
- **Code propre** : Respecter les conventions de codage Python (PEP 8)
- **Documentation** : Mettre à jour la documentation si nécessaire

## Équipe

**Équipe 20**

- **William Wang** - Développeur
- **Kim Desroches** - Développeur
- **Kimia Foroudian** - Développeur

## Licence

Ce projet est réalisé dans le cadre du cours **LOG3000** à Polytechnique Montréal.

**Usage :** Ce projet est destiné à des fins pédagogiques et éducatives uniquement.

---

## FAQ et Dépannage

### L'application ne démarre pas

**Problème :** Erreur lors du lancement de `python app.py`

**Solutions :**
1. Vérifier que l'environnement virtuel est activé
2. Vérifier que Flask est installé : `pip show flask`
3. Vérifier que vous êtes dans le bon répertoire

### Erreur d'import de module

**Problème :** `ModuleNotFoundError: No module named 'flask'`

**Solution :**
```bash
pip install flask
```

### Le port 5000 est déjà utilisé

**Problème :** `Address already in use`

**Solutions :**
1. Arrêter le processus utilisant le port 5000
2. Modifier le port dans `app.py` : `app.run(port=5001)`

### Problèmes avec l'environnement virtuel

**Sous Windows** : Si `venv\Scripts\activate` ne fonctionne pas, essayez :
```bash
venv\Scripts\activate.bat
```

**Sous macOS/Linux** : Si vous avez des problèmes de permissions :
```bash
chmod +x venv/bin/activate
```

---

## Ressources supplémentaires

- [Documentation Flask](https://flask.palletsprojects.com/)
- [Guide Git](https://git-scm.com/doc)
- [PEP 8 - Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [Pytest Documentation](https://docs.pytest.org/)

---

**Dernière mise à jour :** Novembre 2025bash
# Vérifier la version de Python
python --version
# ou
python3 --version

# Vérifier pip
pip --version
# ou
pip3 --version

# Vérifier Git
git --version
```

## Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/WilliamWang5632/TP3---LOG3000.git
cd TP3---LOG3000
```

### 2. Créer un environnement virtuel

La création d'un environnement virtuel est recommandée pour isoler les dépendances du projet.

#### Sous Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Sous macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

**Note :** Une fois l'environnement virtuel activé, vous verrez `(venv)` apparaître au début de votre ligne de commande.

### 3. Installer les dépendances

```bash
pip install flask
```

Pour une installation plus complète incluant les dépendances de test (à venir) :

```bash
pip install -r requirements-test.txt
```

**Note :** Si le fichier `requirements.txt` n'existe pas encore, créez-le avec le contenu suivant :

```