"""
===============================================================================
Module : test_operators.py
Auteur(s) : William Wang, Kim Desroches, Kimia Foroudian
Description :
Ce fichier contient les tests unitaires pour le module `operators.py`.
Il vérifie le bon fonctionnement de toutes les opérations arithmétiques :
- Addition
- Soustraction
- Multiplication
- Division

Objectif :
Valider que chaque fonction retourne les résultats attendus pour des cas
normaux, des cas limites et des cas d'erreur.

Exécution :
    pytest tests/test_operators.py
    pytest tests/test_operators.py -v  # mode verbose
===============================================================================
"""

import pytest
from operators import add, subtract, multiply, divide

class TestAddition:
    """Tests pour la fonction add()."""
    # NOTE: La fonction actuelle ne fait pas d'opération de décimaux.

    def test_add_positive_numbers(self):
        """Test l'addition de deux nombres positifs."""
        assert add(2, 3) == 5
        assert add(10, 20) == 30

    def test_add_negative_numbers(self):
        """Test l'addition de deux nombres négatifs."""
        assert add(-5, -3) == -8
        assert add(-10, -20) == -30

    def test_add_mixed_signs(self):
        """Test l'addition d'un nombre positif et d'un nombre négatif."""
        assert add(5, -3) == 2
        assert add(-5, 3) == -2

    def test_add_with_zero(self):
        """Test l'addition avec zéro."""
        assert add(0, 5) == 5
        assert add(5, 0) == 5
        assert add(0, 0) == 0

    def test_add_floats(self):
        """Test l'addition de nombres décimaux."""
        assert add(2.5, 3.5) == 6.0
        assert add(0.1, 0.2) == pytest.approx(0.3)

    def test_add_large_numbers(self):
        """Test l'addition de grands nombres."""
        assert add(1000000, 2000000) == 3000000
        
    def test_add_commutative(self):
        """L'addition doit être commutative: a + b == b + a."""
        assert add(5, 3) == add(3, 5)
        assert add(-1, 2.5) == add(2.5, -1)


class TestSubtraction:
    """Tests pour la fonction subtract()."""
    # NOTE: La fonction actuelle fait b - a, pas a - b
    # La fonction actuelle ne fait pas d'opération de décimaux.

    def test_subtract_positive_numbers(self):
        """Test la soustraction de deux nombres positifs."""
        assert subtract(3, 10) == -7  
        assert subtract(10,3) == 7

    def test_subtract_negative_numbers(self):
        """Test la soustraction de deux nombres négatifs."""
        assert subtract(-3, -10) == 7  # (-3) - (-10) = 7
        assert subtract(-10, -3) == -7  # (-10) - (-3) = -7

    def test_subtract_mixed_signs(self):
        """Test la soustraction avec des signes mixtes."""
        assert subtract(5, -3) == 8  
        assert subtract(-5, 3) == -8 

    def test_subtract_with_zero(self):
        """Test la soustraction avec zéro."""
        assert subtract(0, 5) == -5  
        assert subtract(5, 0) == 5 
        assert subtract(0, 0) == 0

    def test_subtract_floats(self):
        """Test la soustraction de nombres décimaux."""
        assert subtract(2.5, 10.5) == -8.0 
        assert subtract(0.3, 1.0) == pytest.approx(-0.7)

    def test_subtract_result_negative(self):
        """Test quand le résultat est négatif."""
        assert subtract(10, 3) == 7


class TestMultiplication:
    """Tests pour la fonction multiply()."""
     # NOTE: La fonction actuelle fait a ** b (exponentiation), pas a * b
     # Ces tests échoueront car multiply est implémenté comme exponentiation
    # La fonction actuelle ne fait pas d'opération de décimaux.

    def test_multiply_positive_numbers(self):
        """Test la multiplication de deux nombres positifs."""
        assert multiply(2, 3) == 6
        assert multiply(3, 2) == 6

    def test_multiply_by_zero(self):
        """Test la multiplication par zéro."""
        assert multiply(0, 5) == 0 
        assert multiply(5, 0) == 0 
    
    def test_multiply_by_zero_zero(self):
        """Test la multiplication de zéro par zéro."""
        pytest.mark.xfail(reason="multiply() utilise ** au lieu de *; 0**0 == 1 actuellement")
        assert multiply(0, 0) == 0

    def test_multiply_negative_numbers(self):
        """Test la multiplication de nombres négatifs."""
        assert multiply(-2, 3) == -6 
        assert multiply(2, -3) == -6  

    def test_multiply_by_one(self):
        """Test la multiplication par 1."""
        assert multiply(5, 1) == 5  
        assert multiply(1, 5) == 5  

    def test_multiply_floats(self):
        """Test la multiplication de nombres décimaux."""
        result = multiply(2.0, 3.0)  
        assert result == pytest.approx(6.0)

    def test_multiply_large_numbers(self):
        """Test la multiplication de grands nombres."""
        assert multiply(2, 10) == 20  

class TestDivision:
    """Tests pour la fonction divide()."""
    # NOTE: La fonction actuelle fait a // b (division entière)
    # La fonction actuelle ne fait pas d'opération de décimaux.

    def test_divide_positive_numbers(self):
        """Test la division de deux nombres positifs."""
        assert divide(10, 2) == 5
        assert divide(20, 4) == 5

    def test_divide_with_remainder(self):
        """Test la division avec reste (division entière)."""
        assert divide(10, 3) == 3  # 10 // 3 = 3
        assert divide(7, 2) == 3  # 7 // 2 = 3

    def test_divide_negative_numbers(self):
        """Test la division avec nombres négatifs."""
        assert divide(-10, 2) == -5
        assert divide(10, -2) == -5
        assert divide(-10, -2) == 5

    def test_divide_by_one(self):
        """Test la division par 1."""
        assert divide(5, 1) == 5
        assert divide(100, 1) == 100

    def test_divide_zero_by_number(self):
        """Test la division de zéro par un nombre."""
        assert divide(0, 5) == 0
        assert divide(0, 100) == 0

    def test_divide_by_zero(self):
        """Test la division par zéro (doit lever une exception)."""
        with pytest.raises(ZeroDivisionError):
            divide(10, 0)

    def test_divide_floats(self):
        """Test la division de nombres décimaux."""
        # Division entière de floats
        assert divide(10.0, 3.0) == 3.0
        assert divide(7.5, 2.5) == 3.0  # 7.5 // 2.5 = 3.0

    def test_divide_results_in_zero(self):
        """Test quand la division entière donne zéro."""
        assert divide(1, 2) == 0  # 1 // 2 = 0
        assert divide(3, 5) == 0  # 3 // 5 = 0


class TestOperatorsEdgeCases:
    """Tests de cas limites pour toutes les opérations."""

    def test_operations_with_very_large_numbers(self):
        """Test avec de très grands nombres."""
        large = 10**10
        assert add(large, large) == 2 * large
        assert subtract(large, large * 2) == large

    def test_operations_with_very_small_numbers(self):
        """Test avec de très petits nombres."""
        small = 0.0000001
        assert add(small, small) == pytest.approx(2 * small)

    def test_operations_preserve_type(self):
        """Test que les opérations préservent ou convertissent correctement les types."""
        # Addition d'entiers
        result = add(2, 3)
        assert isinstance(result, int)

        # Addition de floats
        result = add(2.0, 3.0)
        assert isinstance(result, float)


# Tests additionnels pour identifier les bugs connus
class TestKnownBugs:
    """Tests qui identifient les bugs connus dans l'implémentation actuelle."""

    @pytest.mark.xfail(reason="multiply() utilise ** au lieu de *")
    def test_multiply_should_be_multiplication_not_exponentiation(self):
        """Ce test devrait passer si multiply faisait vraiment de la multiplication."""
        assert multiply(3, 4) == 12 

    @pytest.mark.xfail(reason="subtract() fait b-a au lieu de a-b")
    def test_subtract_order_should_be_a_minus_b(self):
        """Ce test devrait passer si subtract faisait a - b."""
        assert subtract(10, 3) == 7 

    @pytest.mark.xfail(reason="divide() fait // au lieu de /")
    def test_divide_should_be_float_division(self):
        """Ce test devrait passer si divide faisait de la division flottante."""
        assert divide(10, 3) == pytest.approx(3.333, rel=0.01)
        # Devrait être 3.333..., pas 3