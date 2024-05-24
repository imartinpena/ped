import unittest
from cliserv import Cliserv

class CliservTest(unittest.TestCase):

    def setUp(self):
        self.devuelve = Cliserv()

    # Comprueba que la palabra introducida es un palíndromo
    def test_palindromo(self):
        cadena = "asa"
        valido = self.devuelve.esPalindromo(cadena)
        self.assertTrue(valido)

    # Comprueba que la palabra no es un palíndromo
    def test_nopalindromo(self):
        cadena = "numero"
        valido = self.devuelve.esPalindromo(cadena)
        self.assertFalse(valido)

    # Comprueba que el número es capicúa
    def test_capicua(self):
        self.assertTrue(self.devuelve.esCapicua("2002"))

    # Comprueba que el número no es capicúa
    def test_nocapicua(self):
        cadena = "428"
        valido = self.devuelve.esCapicua(cadena)
        self.assertFalse(valido)

    # Comprueba que no es un número natural
    def test_nonatural(self):
        cadena = "hola"
        valido = self.devuelve.esNatural(cadena)
        self.assertFalse(valido)

    # Comprueba que es un número natural
    def test_natural(self):
        cadena = "1234"
        valido = self.devuelve.esNatural(cadena)
        self.assertTrue(valido)

    # Comprueba que los caracteres especiales devuelven el mensaje adecuado
    def test_caracteres_especiales(self):
        cadena = "??"
        self.assertEqual(self.devuelve.pide(cadena), "NO CAPICUA Y NO PALINDROMO")


if __name__ == '__main__':
    unittest.main()