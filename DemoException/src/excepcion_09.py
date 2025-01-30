import random

class Error(Exception):
    """Clase base para otras excepciones"""
    pass


class ValueTooSmallError(Error):
    """Aumenta cuando el valor de entrada es demasiado pequeño"""
    pass


class ValueTooLargeError(Error):
    """Aumenta cuando el valor de entrada es demasiado grande"""
    pass


# Necesitas adivinar este número
#random.seed(5)
number = random.randint(1, 20)

# El usuario adivina un número hasta que lo acierta
while True:
    try:
        i_num = int(input("Ingrese un numero: "))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("Este valor es demasiado pequeño, inténtelo de nuevo.")
        print()
    except ValueTooLargeError:
        print("Este valor es demasiado grande, inténtelo de nuevo.")
        print()

print("¡Felicidades! Lo adivinaste.")