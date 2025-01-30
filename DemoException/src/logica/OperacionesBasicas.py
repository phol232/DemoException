class OperacionesBasicas:
    def suma(self, sumando1, sumando2):
        return sumando1 + sumando2

    def division(self, dividendo, divisor):
        return dividendo / divisor


    def ingresoParametro(self, parametro):
        if not isinstance(parametro, (int, float)):
            try:
                parametro=float(parametro)
            except ValueError:
                 raise ValueError
        return parametro