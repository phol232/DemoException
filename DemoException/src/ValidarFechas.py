class FechaInvalidaError(Exception):
    pass


class ValidarFecha:
    @staticmethod
    def es_bisiesto(año):

        return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)

    @staticmethod
    def dias_en_mes(mes, año):

        dias_por_mes = {
            1: 31, 2: 29 if ValidarFecha.es_bisiesto(año) else 28, 3: 31, 4: 30, 5: 31, 6: 30,
            7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
        }
        return dias_por_mes.get(mes, 0)

    @staticmethod
    def validar_formato_fecha(entrada_fecha):

        partes = entrada_fecha.split('/')
        if len(partes) != 3:
            raise FechaInvalidaError("Formato incorrecto. Use el formato DD/MM/YYYY Ejemplo (12/10/2021).")
        return partes

    @staticmethod
    def validar_numeros(dia_str, mes_str, año_str):

        try:
            dia = int(dia_str)
            mes = int(mes_str)
            anio = int(año_str)
        except ValueError:
            raise FechaInvalidaError("Los valores de día, mes y año deben ser números enteros.")

        return dia, mes, anio

    @staticmethod
    def validar_rango_fecha(dia, mes, año):

        if año < 0:
            raise FechaInvalidaError("El año no puede ser negativo.")

        if mes < 1 or mes > 12:
            raise FechaInvalidaError("El mes debe estar entre 1 y 12.")

        dias_max = ValidarFecha.dias_en_mes(mes, año)
        if dia < 1 or dia > dias_max:
            raise FechaInvalidaError(f"El día debe estar entre 1 y {dias_max} para el mes {mes}.")

        return dia, mes, año

    @classmethod
    def validar_fecha(cls, entrada_fecha):

        partes = cls.validar_formato_fecha(entrada_fecha)
        dia, mes, año = cls.validar_numeros(*partes)
        return cls.validar_rango_fecha(dia, mes, año)


def leer_fecha():

    while True:
        try:
            entrada_fecha = input("Ingrese la fecha en formato DD/MM/YYYY: ")
            return ValidarFecha.validar_fecha(entrada_fecha)
        except FechaInvalidaError as e:
            print(f"Error: {e}. Inténtelo nuevamente.")


if __name__ == "__main__":
    try:
        dia_valido, mes_valido, anio_valido = leer_fecha()
        print(f"La fecha ingresada es: {dia_valido}/{mes_valido}/{anio_valido}")
    except KeyboardInterrupt:
        print("\nOperación cancelada por el usuario.")
