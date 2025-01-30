def leer_fecha():

    while True:
        entrada_fecha = input("Ingrese la fecha en formato DD/MM/YYYY: ")
        partes = entrada_fecha.split('/')


        if len(partes) != 3:
            print("Error: Formato incorrecto. Use el formato DD/MM/YYYY.")
            continue

        dia_str, mes_str, anio_str = partes


        errores = []


        if '.' in dia_str:
            errores.append("No se permiten decimales para el día.")
        else:
            try:
                dia = int(dia_str)
                if dia < 1 or dia > 31:
                    errores.append("El día debe estar entre 1 y 31.")
            except ValueError:
                errores.append("El día debe ser un número entero (sin letras ni símbolos).")


        if '.' in mes_str:
            errores.append("No se permiten decimales para el mes.")
        else:
            try:
                mes = int(mes_str)
                if mes < 1 or mes > 12:
                    errores.append("El mes debe estar entre 1 y 12.")
            except ValueError:
                errores.append("El mes debe ser un número entero (sin letras ni símbolos).")


        if '.' in anio_str:
            errores.append("No se permiten decimales para el año.")
        else:
            try:
                anio = int(anio_str)
                if anio < 0:
                    errores.append("El año no puede ser negativo.")
            except ValueError:
                errores.append("El año debe ser un número entero (sin letras ni símbolos).")


        if errores:
            for error in errores:
                print(f"Error: {error}")
            print("Inténtelo nuevamente.\n")
        else:

            return dia, mes, anio



if __name__ == "__main__":
    try:
        dia_valido, mes_valido, anio_valido = leer_fecha()
        print(f"La fecha ingresada es: {dia_valido}/{mes_valido}/{anio_valido}")
    except KeyboardInterrupt:
        print("\nOperación cancelada por el usuario.")