import unittest
from kataDeBolos import Partida

class TestKataDeBolos(unittest.TestCase):
    # Tests para requisito 1
    def test_partida_inicia_en_cero(self):
        partida = Partida()
        self.assertEqual(partida.puntuacion_total(), 0)

    def test_agregar_un_tiro(self):
        partida = Partida()
        partida.agregar_tiro(5)
        self.assertEqual(partida.puntuacion_total(), 5)

    # Tests para requisito 2
    def test_strike_sin_siguientes_tiros(self):
        partida = Partida()
        partida.agregar_tiro(10)  # Strike
        self.assertEqual(partida.puntuacion_total(), 10)

    def test_strike_con_siguientes_tiros(self):
        partida = Partida()
        partida.agregar_tiro(10)  # Strike
        partida.agregar_tiro(3)
        partida.agregar_tiro(4)
        # Puntuación: 10 (strike) + 3 + 4 (siguientes tiros) + 3 + 4 (suma de los siguientes tiros como bonus)
        self.assertEqual(partida.puntuacion_total(), 24)

    def test_strike_con_dos_tiros_posteriores_en_diferentes_rondas(self):
        partida = Partida()
        partida.agregar_tiro(10)  # Strike
        partida.agregar_tiro(3)
        partida.agregar_tiro(4)
        partida.agregar_tiro(2)  # Comienzo de la siguiente ronda
        partida.agregar_tiro(3)
        # Puntuación: 10 + (3+4) (bonus) + 3 + 4 + 2 + 3
        self.assertEqual(partida.puntuacion_total(), 29)

    def test_strike_en_ultima_ronda_con_bonus(self):
        partida = Partida()
        # Llenar 9 rondas con tiros sin strikes
        for _ in range(9):
            partida.agregar_tiro(0)
            partida.agregar_tiro(0)
        partida.agregar_tiro(10)  # Strike en la última ronda
        # Bonus de la última ronda
        partida.agregar_tiro(3)
        partida.agregar_tiro(4)
        # Puntuación: 10 (strike) + 3 (bonus) + 4 (bonus)
        self.assertEqual(partida.puntuacion_total(), 17)

    # Tests para requisito 3
    def test_spare_sin_siguientes_tiros(self):
        partida = Partida()
        partida.agregar_tiro(7)
        partida.agregar_tiro(3)  # Spare
        self.assertEqual(partida.puntuacion_total(), 10)

    def test_spare_con_siguiente_tiro(self):
        partida = Partida()
        partida.agregar_tiro(6)
        partida.agregar_tiro(4)  # Spare
        partida.agregar_tiro(5)
        # Puntuación: 6 + 4 (spare) + 5 (siguiente tiro) + 5 (bonus por spare)
        self.assertEqual(partida.puntuacion_total(), 20)

    def test_spare_en_ultima_ronda_con_bonus(self):
        partida = Partida()
        # Llenar 9 rondas con tiros sin spares
        for _ in range(9):
            partida.agregar_tiro(0)
            partida.agregar_tiro(0)
        partida.agregar_tiro(3)
        partida.agregar_tiro(7)  # Spare en la última ronda
        partida.agregar_tiro(4)  # Tiro bonus
        self.assertEqual(partida.puntuacion_total(), 14)

    def test_ronda_abierta(self):
        # Test para verificar el puntaje en una ronda abierta (sin strike ni spare)
        partida = Partida()
        partida.agregar_tiro(3)
        partida.agregar_tiro(4)  # 3 + 4 = 7 puntos en esta ronda
        self.assertEqual(partida.puntuacion_total(), 7)

    def test_varias_rondas_abiertas(self):
        # Test para verificar el puntaje acumulado en varias rondas abiertas
        partida = Partida()
        partida.agregar_tiro(2)
        partida.agregar_tiro(5)  # Ronda 1: 2 + 5 = 7 puntos
        partida.agregar_tiro(3)
        partida.agregar_tiro(4)  # Ronda 2: 3 + 4 = 7 puntos, total = 14
        self.assertEqual(partida.puntuacion_total(), 14)

    def test_ronda_abierta_despues_de_strike(self):
        # Test para verificar el puntaje después de un strike seguido por una ronda abierta
        partida = Partida()
        partida.agregar_tiro(10)  # Ronda 1: Strike, puntos dependen de los siguientes tiros
        partida.agregar_tiro(3)
        partida.agregar_tiro(4)  # Ronda 2: 3 + 4 = 7 puntos, total = 24 (10 + 3 + 4 + 3 + 4)
        self.assertEqual(partida.puntuacion_total(), 24)

    def test_ronda_abierta_despues_de_spare(self):
        # Test para verificar el puntaje después de un spare seguido por una ronda abierta
        partida = Partida()
        partida.agregar_tiro(5)
        partida.agregar_tiro(5)  # Ronda 1: Spare, puntos dependen del siguiente tiro
        partida.agregar_tiro(3)
        partida.agregar_tiro(4)  # Ronda 2: 3 + 4 = 7 puntos, total = 20 (10 + 3 + 3 + 4)
        self.assertEqual(partida.puntuacion_total(), 20)

    def test_mezcla_de_rondas(self):
        # Test para verificar el puntaje en una partida con una mezcla de strikes, spares y rondas abiertas
        partida = Partida()
        partida.agregar_tiro(10)  # Ronda 1: Strike
        partida.agregar_tiro(5)
        partida.agregar_tiro(5)  # Ronda 2: Spare
        partida.agregar_tiro(3)
        partida.agregar_tiro(4)  # Ronda 3: Ronda abierta
        self.assertEqual(partida.puntuacion_total(), 40)

    def test_acumulacion_puntuacion_en_varias_rondas(self):
        # Verifica que la puntuación se acumula correctamente a lo largo de varias rondas
        partida = Partida()
        partida.agregar_tiro(1)  # Ronda 1: 1 pin
        partida.agregar_tiro(4)  # Ronda 1: 4 pines, total = 5
        partida.agregar_tiro(4)  # Ronda 2: 4 pines
        partida.agregar_tiro(5)  # Ronda 2: 5 pines, total = 14
        partida.agregar_tiro(6)  # Ronda 3: 6 pines
        partida.agregar_tiro(4)  # Ronda 3: 4 pines (spare), total = 24 + bonus próximo tiro
        partida.agregar_tiro(5)  # Ronda 4: 5 pines, total = 24 + 5 (bonus) + 5 = 34
        self.assertEqual(partida.puntuacion_total(), 34)

    def test_bonus_en_decima_ronda_con_strike(self):
        partida = Partida()
        # Llenando las primeras 9 rondas con tiros que no son strikes ni spares
        for _ in range(9):
            partida.agregar_tiro(0)
            partida.agregar_tiro(0)
        # Décima ronda con strike
        partida.agregar_tiro(10)
        # Tiros extra después de un strike en la décima ronda
        partida.agregar_tiro(7)
        partida.agregar_tiro(2)
        # Verifica que se calcula correctamente el puntaje total
        self.assertEqual(partida.puntuacion_total(), 19)

    def test_bonus_en_decima_ronda_con_spare(self):
        partida = Partida()
        # Llenando las primeras 9 rondas con tiros que no son strikes ni spares
        for _ in range(9):
            partida.agregar_tiro(0)
            partida.agregar_tiro(0)
        # Décima ronda con spare
        partida.agregar_tiro(7)
        partida.agregar_tiro(3)
        # Tiro extra después de un spare en la décima ronda
        partida.agregar_tiro(5)
        # Verifica que se calcula correctamente el puntaje total
        self.assertEqual(partida.puntuacion_total(), 15)

    def test_agregar_tiro_con_valor_negativo(self):
        partida = Partida()
        with self.assertRaises(ValueError):
            partida.agregar_tiro(-5)

    def test_agregar_tiro_con_valor_no_entero(self):
        partida = Partida()
        with self.assertRaises(ValueError):
            partida.agregar_tiro(5.5)

    def test_agregar_tiro_con_valor_no_entero_positivo(self):
        partida = Partida()
        with self.assertRaises(ValueError):
            partida.agregar_tiro("cinco")
            
    def test_toda_la_partida_con_strikes(self):
        partida = Partida()
        for _ in range(12):  # Hasta 12 tiros para permitir tiros extras en la última ronda
            partida.agregar_tiro(10) 
        self.assertEqual(partida.puntuacion_total(), 300)

if __name__ == '__main__':
    unittest.main()
