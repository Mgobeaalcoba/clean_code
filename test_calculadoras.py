from unittest import TestCase
from calculadoras import CalculadoraEstatica, Calculadora


class CalculadoraEstaticaTest(TestCase):

    def test_metodo_suma_deberia_retornar_la_suma_de_dos_numeros(self):
        # Given
        numero1 = 5
        numero2 = 10

        # When
        resultado = CalculadoraEstatica.suma(numero1, numero2)

        # Then
        self.assertEqual(resultado, 15)

    def test_metodo_resta_deberia_retornar_la_resta_de_dos_numeros(self):
        # Given
        numero1 = 10
        numero2 = 5

        # When
        resultado = CalculadoraEstatica.resta(numero1, numero2)

        # Then
        self.assertEqual(resultado, 5)

    def test_metodo_division_deberia_retornar_el_cociente_de_dos_numeros(self):
        # Given
        numero1 = 10
        numero2 = 2

        # When
        resultado = CalculadoraEstatica.division(numero1, numero2)

        # Then
        self.assertEqual(resultado, 5)
    
    def test_metodo_division_deberia_generar_un_error_si_el_divisor_es_cero(self):
        # Given
        numero1 = 10
        numero2 = 0

        # When & Then
        with self.assertRaises(ZeroDivisionError):
            CalculadoraEstatica.division(numero1, numero2)


class CalculadoraTest(TestCase):

    def test_metodo_suma_deberia_retornar_la_suma_de_dos_numeros(self):
        # Given
        mi_clase = Calculadora()
        numero1 = 5
        numero2 = 10

        # When
        resultado = mi_clase.suma(numero1, numero2)

        # Then
        self.assertEqual(resultado, 15)

    def test_metodo_resta_deberia_retornar_la_resta_de_dos_numeros(self):
        # Given
        mi_clase = Calculadora()
        numero1 = 10
        numero2 = 5

        # When
        resultado = mi_clase.resta(numero1, numero2)

        # Then
        self.assertEqual(resultado, 5)

    def test_metodo_division_deberia_retornar_el_cociente_de_dos_numeros(self):
        # Given
        mi_clase = Calculadora()
        numero1 = 10
        numero2 = 2

        # When
        resultado = mi_clase.division(numero1, numero2)

        # Then
        self.assertEqual(resultado, 5)
    
    def test_metodo_division_deberia_generar_un_error_si_el_divisor_es_cero(self):
        # Given
        mi_clase = Calculadora()
        numero1 = 10
        numero2 = 0

        # When & Then
        with self.assertRaises(ZeroDivisionError):
            mi_clase.division(numero1, numero2)