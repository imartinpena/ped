import re

class Cliserv:

    def pide(self, peticion=None):
        if peticion is None:
            peticion = input("Introduzca una palabra o un número natural: ")
        # Verificar si la entrada está vacía o contiene caracteres especiales
        if not peticion or re.search(r'[^a-zA-Z0-9\s]', peticion):
            return "NO CAPICUA Y NO PALINDROMO"
        return peticion

    def esNatural(self, peticion):
        """
        Verifica si la entrada es un número natural.
        """
        peticion = peticion.replace(" ", "")  # Eliminar espacios en blanco

        try:
            peticion = int(peticion)
            return peticion >= 1
        except ValueError:
            return False    

    def esPalindromo(self, peticion):
        """
        Verifica si la entrada es un palíndromo.
        """
        # Si la cadena contiene caracteres especiales, no es un palíndromo
        if re.search(r'[^a-zA-Z0-9\s]', peticion):
            return False
        if len(peticion) <= 1:
            return False
        peticion = peticion.lower()  # Convertir la palabra a minúsculas
        peticion = peticion.replace(" ", "")  # Eliminar espacios en blanco
        # Verificar si la palabra es igual a su reverso
        return peticion == peticion[::-1]

    def esCapicua(self, peticion):
        """
        Verifica si la entrada es un número capicúa.
        """
        if len(str(peticion)) <= 1:
            return False
        peticion = str(peticion)
        return peticion == peticion[::-1]

    def resultado(self, peticion):
        """
        Imprime el resultado de verificar si la entrada es un número natural, capicúa o palíndromo.
        """
        if peticion == "NO CAPICUA Y NO PALINDROMO":
            print(peticion)
            return

        if self.esNatural(peticion):  # Comprueba si lo introducido es un número natural
            if self.esCapicua(peticion):  # Comprueba si el número es capicúa
                print("Sí es Capicúa")
            else:
                print("No es Capicúa")
        else:  # Si no es un número natural
            if self.esPalindromo(peticion):  # Comprueba si es un palíndromo
                print(f"{peticion} Sí es un Palíndromo.")
            else:
                print(f"{peticion} No es un Palíndromo.")
            print("NO NATURAL")

if __name__ == "__main__":
    cliserv = Cliserv()
    while True:
        peticion = cliserv.pide()
        if peticion.lower() == 'salir':
            break
        cliserv.resultado(peticion)