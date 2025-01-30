class ValidarFecha:
    def leer_dia(self):

        while True:
            dia_str = input("Ingrese el día (1-31): ")
            try:
                if '.' in dia_str:
                    raise ValueError("Los días no pueden contener decimales.")

                dia = int(dia_str)

                if dia <= 0:
                    raise ValueError("El día debe ser un número entero positivo.")
                if dia > 31:
                    raise ValueError("El día no puede ser mayor a 31.")

                return dia
            except ValueError as e:
                print(f"Error: {e}. Intente de nuevo.")

    def leer_mes(self):

        while True:
            mes_str = input("Ingrese el mes (1-12): ")
            try:
                if '.' in mes_str:
                    raise ValueError("Los meses no pueden contener decimales.")

                mes = int(mes_str)

                if mes <= 0:
                    raise ValueError("El mes debe ser un número entero positivo.")
                if mes > 12:
                    raise ValueError("El mes no puede ser mayor a 12.")

                return mes
            except ValueError as e:
                print(f"Error: {e}. Intente de nuevo.")

    def leer_anio(self):

        while True:
            anio_str = input("Ingrese el año (ej. 2025): ")
            try:
                if '.' in anio_str:
                    raise ValueError("El año no puede contener decimales.")

                anio = int(anio_str)

                if anio < 0:
                    raise ValueError("El año no puede ser negativo.")

                return anio
            except ValueError as e:
                print(f"Error: {e}. Intente de nuevo.")


if __name__ == "__main__":
    validador = ValidarFecha()
    dia_valido = validador.leer_dia()
    mes_valido = validador.leer_mes()
    anio_valido = validador.leer_anio()
    print(f"Fecha ingresada: {dia_valido}/{mes_valido}/{anio_valido}")