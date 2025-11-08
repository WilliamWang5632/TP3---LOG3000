# Tests de Flask Calculator

Ce dossier contient l'ensemble des tests pour le projet de Flask Calculator. Les tests sont écrits avec pytest et couvrent à la fois les tests unitaires, les tests d'intégration et tests de validation.

## Installation des dépendances

Pour exécuter les tests, vous devez d'abord installer les dépendances nécessaires :

```bash
pip install -r requirements-test.txt
pip install pytest pytest-flask
```

## Structure des tests

Le projet contient deux fichiers de test principaux :

### 1. `test_operators.py`

Tests unitaires pour les opérations mathématiques de base. Couvre :
- Addition (`add`)
- Soustraction (`subtract`)
- Multiplication (`multiply`)
- Division (`divide`)

#### Classes de test :
- `TestAddition` : Tests des opérations d'addition
- `TestSubtraction` : Tests des opérations de soustraction
- `TestMultiplication` : Tests des opérations de multiplication
- `TestDivision` : Tests des opérations de division
- `TestOperatorsEdgeCases` : Tests des cas limites
- `TestKnownBugs` : Documentation des bugs connus

### 2. `test_app.py`

Tests d'intégration pour l'application Flask. Couvre :
- Les routes HTTP (GET et POST)
- La fonction `calculate()`
- L'intégration frontend/backend
- La gestion des erreurs

#### Classes de test :
- `TestCalculateFunction` : Tests de la fonction de calcul
- `TestFlaskRoutes` : Tests des routes Flask
- `TestErrorHandling` : Tests de gestion des erreurs
- `TestIntegration` : Tests d'intégration end-to-end
- `TestBoundaryConditions` : Tests des conditions limites

## Exécution des tests

### Exécuter tous les tests
```bash
pytest
```

### Exécuter les tests avec le mode verbeux
```bash
pytest -v
```

### Exécuter un fichier de test spécifique
```bash
pytest tests/test_operators.py
pytest tests/test_app.py
```

### Exécuter avec couverture de code
```bash
pytest --cov=.
```

### Générer un rapport de couverture HTML
```bash
pytest --cov=. --cov-report=html
```

## Notes importantes

1. Bugs connus :
   - La fonction `multiply()` utilise l'exponentiation (`**`) au lieu de la multiplication (`*`)
   - La fonction `subtract()` fait `b-a` au lieu de `a-b`
   - La fonction `divide()` fait une division entière (`//`) au lieu d'une division flottante (`/`)

2. Configuration :
   - Les tests utilisent des fixtures pytest pour la configuration
   - L'application est configurée en mode test pendant l'exécution des tests

3. Performance :
   - Pour les tests de performance, vous pouvez utiliser pytest-benchmark (inclus dans requirements-test.txt)
   - Pour une exécution plus rapide, utilisez pytest-xdist pour la parallélisation :
     ```bash
     pytest -n auto
     ```

## Couverture des tests

Les tests couvrent :
- Opérations mathématiques de base
- Gestion des erreurs et cas limites
- Interface utilisateur et routes HTTP
- Validation des entrées
- Cas spéciaux (nombres négatifs, zéro, grands nombres)
- Indépendance des sessions
