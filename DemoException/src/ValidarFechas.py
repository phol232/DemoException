class FechaInvalidaError(Exception):
    pass


class Fecha:
    def __init__(self, entrada_fecha):
        self.dia, self.mes, self.año = self.validar_fecha(entrada_fecha)

    def es_bisiesto(self, año):
        return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)

    def dias_en_mes(self, mes, año):
        dias_por_mes = {
            1: 31, 2: 29 if self.es_bisiesto(año) else 28, 3: 31, 4: 30, 5: 31, 6: 30,
            7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
        }
        return dias_por_mes.get(mes, 0)

    def validar_fecha(self, entrada_fecha):
        partes = self.validar_formato(entrada_fecha)
        dia, mes, año = self.convertir_numeros(*partes)
        return self.validar_rango(dia, mes, año)

    def validar_formato(self, entrada_fecha):
        partes = entrada_fecha.split('/')
        if len(partes) != 3:
            raise FechaInvalidaError("Formato incorrecto. Use el formato DD/MM/YYYY Ejemplo (12/10/2021).")
        return partes

    def convertir_numeros(self, dia_str, mes_str, año_str):
        try:
            dia = int(dia_str)
            mes = int(mes_str)
            año = int(año_str)
        except ValueError:
            raise FechaInvalidaError("Los valores de día, mes y año deben ser números enteros.")
        return dia, mes, año

    def validar_rango(self, dia, mes, año):
        if año < 0:
            raise FechaInvalidaError("El año no puede ser negativo.")
        if mes < 1 or mes > 12:
            raise FechaInvalidaError("El mes debe estar entre 1 y 12.")
        dias_max = self.dias_en_mes(mes, año)
        if dia < 1 or dia > dias_max:
            raise FechaInvalidaError(f"El día debe estar entre 1 y {dias_max} para el mes {mes}.")
        return dia, mes, año

    def get_dia(self):
        return self.dia

    def get_mes(self):
        return self.mes

    def get_año(self):
        return self.año


def leer_fecha():
    while True:
        try:
            entrada_fecha = input("Ingrese la fecha en formato DD/MM/YYYY: ")
            fecha = Fecha(entrada_fecha)
            return fecha
        except FechaInvalidaError as e:
            print(f"Error: {e}. Inténtelo nuevamente.")


if __name__ == "__main__":
    try:
        fecha_valida = leer_fecha()
        print(f"La fecha ingresada es: {fecha_valida.get_dia()}/{fecha_valida.get_mes()}/{fecha_valida.get_año()}")
    except KeyboardInterrupt:
        print("\nOperación cancelada por el usuario.")
