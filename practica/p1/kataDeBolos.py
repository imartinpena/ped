class Partida:
    def __init__(self):
        self.rondas = [[]]

    def agregar_tiro(self, pinos):
        if not isinstance(pinos, int) or pinos < 0:
            raise ValueError("El número de pinos debe ser un entero positivo.")
        es_decima_ronda = len(self.rondas) == 10
        if not es_decima_ronda:
            if len(self.rondas[-1]) == 2 or (self.rondas[-1] and self.rondas[-1][0] == 10):
                self.rondas.append([pinos])
            else:
                self.rondas[-1].append(pinos)
        else:
            # En la décima ronda, permite hasta dos tiros extra para strike o uno para spare
            if sum(self.rondas[-1]) >= 10 and len(self.rondas[-1]) < 3 or len(self.rondas[-1]) < 2:
                self.rondas[-1].append(pinos)

    def puntuacion_total(self):
        total = 0
        for i, ronda in enumerate(self.rondas[:10]):
            if self.es_strike(ronda) and i < 9:
                total += 10 + self.bonus_strike(i)
            elif self.es_spare(ronda) and i < 9:
                total += 10 + self.bonus_spare(i)
            else:
                total += sum(ronda)
        return total

    def es_strike(self, ronda):
        return len(ronda) == 1 and ronda[0] == 10

    def es_spare(self, ronda):
        return len(ronda) == 2 and sum(ronda) == 10

    def bonus_strike(self, ronda_index):
        bonus = 0
        # Asegurarse de que hay rondas suficientes para calcular el bonus
        if ronda_index + 1 < len(self.rondas):
            bonus += sum(self.rondas[ronda_index + 1][:2])
            # Si el siguiente tiro fue un strike, añadir el tiro subsiguiente, si existe
            if self.es_strike(self.rondas[ronda_index + 1]) and ronda_index + 2 < len(self.rondas):
                bonus += self.rondas[ronda_index + 2][0]
        return bonus

    def bonus_spare(self, ronda_index):
        # Asegurarse de que hay un tiro adicional para sumar como bonus
        if ronda_index + 1 < len(self.rondas):
            return self.rondas[ronda_index + 1][0]
        return 0

    def puntuacion_total_con_detalle(self):
        total = 0
        for i, ronda in enumerate(self.rondas[:10]):
            ronda_puntos = sum(ronda)
            if self.es_strike(ronda) and i < 9:
                ronda_puntos += self.bonus_strike(i)
            elif self.es_spare(ronda) and i < 9:
                ronda_puntos += self.bonus_spare(i)
            total += ronda_puntos
            print(f"Puntuación después de la ronda {i + 1}: {total}")
        return total
