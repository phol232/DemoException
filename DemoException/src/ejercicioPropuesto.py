class CalculadoraDivisores:
    def __init__(self):
        pass

    def leer_numero_natural(self):
        while True:
            entrada = input("Ingrese un número natural: ")
            try:

                if '.' in entrada:
                    raise ValueError("Debe ingresar un número entero (no se permiten decimales).")


                numero = int(entrada)


                if numero <= 0:
                    raise ValueError("Debe ingresar un número natural mayor que cero.")

                return numero

            except ValueError as e:

                print(f"Error: {e}. Intente de nuevo.")

    def calcular_divisores(self, numero):
        divisores = []
        for i in range(1, numero + 1):
            if numero % i == 0:
                divisores.append(i)
        return divisores



if __name__ == "__main__":
    calc = CalculadoraDivisores()
    num = calc.leer_numero_natural()
    resultado_divisores = calc.calcular_divisores(num)
    print(f"Los divisores de {num} son: {resultado_divisores}")
    print("¡Gracias por usar la Calculadora de Divisores!")