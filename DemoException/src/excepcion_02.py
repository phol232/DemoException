try:
    x= float(input("Numero:"))
    inverse = 1.0 / x

except ValueError:
    print("Debe ser un int o float")
except ZeroDivisionError:
    print("infinito")
finally:
    print("puede que haya una habido una excepción o no.")

