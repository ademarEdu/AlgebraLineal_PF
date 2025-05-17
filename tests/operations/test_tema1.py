# Tests unitarios para las funciones dentro de operations.tema1

# Importar librerías necesarias
import unittest
# Importar las funciones que serán testeadas
from src.operations.tema1.prod_esc import dot_product
from src.operations.tema1.prod_vec import cross_product
from src.operations.tema1.triple_prod_esc import triple_dot_product

class TestsTema1(unittest.TestCase):
    """Test case para operaciones dentro de tema 1."""

    def test_dot_product(self):
        """Test sobre la lógica del producto escalar."""
        result = dot_product([[2, 3, 5], [4, 7, 2]])
        self.assertEqual(result, 39)

    def test_cross_producy(self):
        """Test sobre la lógica del producto vectorial."""
        result = cross_product([[4, 1, 0], [0, -2, 1]])
        self.assertEqual(result, [1, -4, -8])

    def test_triple_dot(self):
        """Test sobre la lógica del triple producto vectorial."""
        result = triple_dot_product([[1, 3, 5], [2, -1, 0], [-3, 0, -1]])
        print(result)
        self.assertEqual(result, -8)

# Run the tests
if __name__ == '__main__':
    unittest.main()