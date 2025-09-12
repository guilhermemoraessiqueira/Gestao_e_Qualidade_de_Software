# célula 1: função a ser testada
def is_par(n):
    return n % 2 == 0

# célula 2: testes com unittest
import unittest

class TestIsPar(unittest.TestCase):
    def test_numero_par(self):
        self.assertTrue(is_par(4))   # número par

    def test_numero_impar(self):
        self.assertFalse(is_par(7))  # número ímpar

    def test_zero(self):
        self.assertTrue(is_par(0))   # zero é par

    def test_negativo(self):
        self.assertTrue(is_par(-6))  # número negativo par

# importante para notebooks/colab
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

# célula 3: função a ser testada
def fatorial(n):
    if n < 0:
        raise ValueError("n deve ser >= 0")
    if n == 0:
        return 1
    resultado = 1
    for i in range(1, n+1):
        resultado *= i
    return resultado

# célula 42: testes com unittest
import unittest

class TestFatorial(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(fatorial(0), 1)   # caso base

    def test_cinco(self):
        self.assertEqual(fatorial(5), 120) # 5! = 120

    def test_negativo(self):
        with self.assertRaises(ValueError):
            fatorial(-1)  # deve lançar exceção

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)