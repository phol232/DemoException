import unittest
from ValidarFechas import Fecha, FechaInvalidaError


class TestFecha(unittest.TestCase):
    def test_validar_formato_formato_completo_formato_ok(self):
        # Arrange
        fecha = Fecha("01/01/2000")  # Creamos una instancia temporal
        entrada_fecha = "15/07/2023"

        # Act
        resultado = fecha.validar_formato(entrada_fecha)

        # Assert
        self.assertEqual(resultado, ["15", "07", "2023"])

    def test_validar_formato_sin_separadores_lanza_excepcion(self):
        # Arrange
        fecha = Fecha("01/01/2000")
        entrada_fecha = "15072023"

        # Act & Assert
        with self.assertRaises(FechaInvalidaError):
            fecha.validar_formato(entrada_fecha)

    def test_validar_formato_separadores_incorrectos_lanza_excepcion(self):
        # Arrange
        fecha = Fecha("01/01/2000")
        entrada_fecha = "15-07-2023"

        # Act & Assert
        with self.assertRaises(FechaInvalidaError):
            fecha.validar_formato(entrada_fecha)

    def test_validar_formato_partes_incompletas_lanza_excepcion(self):
        # Arrange
        fecha = Fecha("01/01/2000")
        entrada_fecha = "15/07"

        # Act & Assert
        with self.assertRaises(FechaInvalidaError):
            fecha.validar_formato(entrada_fecha)

    def test_validar_formato_fecha_vacia_lanza_excepcion(self):
        # Arrange
        fecha = Fecha("01/01/2000")
        entrada_fecha = ""

        # Act & Assert
        with self.assertRaises(FechaInvalidaError):
            fecha.validar_formato(entrada_fecha)


if __name__ == '__main__':
    unittest.main()