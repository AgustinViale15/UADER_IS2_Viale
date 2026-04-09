#!/usr/bin/env python3
"""
Tests unitarios para la calculadora RPN.
"""

import unittest
import math
from rpn import RPNCalculator, RPNError

class TestRPNCalculator(unittest.TestCase):
    """Pruebas para la calculadora RPN."""
    
    def setUp(self):
        """Configuración inicial para cada prueba."""
        self.calc = RPNCalculator()
    
    def test_basic_operations(self):
        """Prueba operaciones básicas."""
        self.assertEqual(self.calc.eval("3 4 +"), 7)
        self.assertEqual(self.calc.eval("5 1 2 + 4 * + 3 -"), 14)
        self.assertEqual(self.calc.eval("10 2 /"), 5)
        self.assertEqual(self.calc.eval("5 3 -"), 2)
        self.assertEqual(self.calc.eval("4 5 *"), 20)
    
    def test_float_numbers(self):
        """Prueba números de punto flotante."""
        result = self.calc.eval("3.5 2.5 +")
        self.assertAlmostEqual(result, 6.0)
        
        result = self.calc.eval("7.5 2.5 /")
        self.assertAlmostEqual(result, 3.0)
    
    def test_negative_numbers(self):
        """Prueba números negativos."""
        result = self.calc.eval("-5 3 +")
        self.assertEqual(result, -2)
        
        result = self.calc.eval("-4 -2 *")
        self.assertEqual(result, 8)
    
    def test_constants(self):
        """Prueba constantes predefinidas."""
        result = self.calc.eval("p")
        self.assertAlmostEqual(result, math.pi)
        
        result = self.calc.eval("e")
        self.assertAlmostEqual(result, math.e)
        
        result = self.calc.eval("j")
        self.assertAlmostEqual(result, (1 + math.sqrt(5)) / 2)
    
    def test_stack_commands(self):
        """Prueba comandos de pila."""
        # Test dup
        calc2 = RPNCalculator()
        calc2.eval("5 dup +")
        self.assertEqual(calc2.eval("5 dup +"), 10)
        
        # Test swap
        calc3 = RPNCalculator()
        result = calc3.eval("3 5 swap +")
        self.assertEqual(result, 8)
        
        # Test drop
        calc4 = RPNCalculator()
        result = calc4.eval("3 4 drop")
        self.assertEqual(result, 3)
        
        # Test clear
        calc5 = RPNCalculator()
        result = calc5.eval("1 2 3 clear 4")
        self.assertEqual(result, 4)
    
    def test_unary_functions(self):
        """Prueba funciones unarias."""
        result = self.calc.eval("5 chs")
        self.assertEqual(result, -5)
        
        result = self.calc.eval("4 inv")
        self.assertAlmostEqual(result, 0.25)
        
        result = self.calc.eval("16 sqrt")
        self.assertEqual(result, 4)
        
        result = self.calc.eval("100 log")
        self.assertEqual(result, 2)
        
        result = self.calc.eval("e ln")
        self.assertAlmostEqual(result, 1)
    
    def test_trigonometric_functions(self):
        """Prueba funciones trigonométricas."""
        result = self.calc.eval("90 sin")
        self.assertAlmostEqual(result, 1)
        
        result = self.calc.eval("0 cos")
        self.assertAlmostEqual(result, 1)
        
        result = self.calc.eval("45 tg")
        self.assertAlmostEqual(result, 1)
        
        result = self.calc.eval("1 asin")
        self.assertAlmostEqual(result, 90)
    
    def test_memory_operations(self):
        """Prueba operaciones de memoria."""
        self.calc.eval("42 sto 0")
        result = self.calc.eval("rcl 0")
        self.assertEqual(result, 42)
        
        calc2 = RPNCalculator()
        calc2.eval("10 sto 1")
        calc2.eval("20 sto 2")
        result = calc2.eval("rcl 1 rcl 2 +")
        self.assertEqual(result, 30)
    
    def test_power_function(self):
        """Prueba función de potencia."""
        result = self.calc.eval("2 3 yx")
        self.assertEqual(result, 8)
        
        result = self.calc.eval("5 0 yx")
        self.assertEqual(result, 1)
        
        result = self.calc.eval("2 ex")
        self.assertAlmostEqual(result, math.exp(2))
    
    def test_error_handling(self):
        """Prueba manejo de errores."""
        # Token inválido
        with self.assertRaises(RPNError):
            self.calc.eval("3 4 invalid")
        
        # División por cero
        with self.assertRaises(RPNError):
            self.calc.eval("3 0 /")
        
        # Stack final con más de un elemento
        with self.assertRaises(RPNError):
            self.calc.eval("3 4")
    
    def test_complex_expression(self):
        """Prueba expresiones complejas."""
        result = self.calc.eval("3 4 + 5 2 - *")
        self.assertEqual(result, 21)
        
        result = self.calc.eval("3 2 yx 4 2 yx + sqrt")
        self.assertAlmostEqual(result, 5.0)
    
    def test_additional_unary_functions(self):
        """Prueba funciones unarias adicionales."""
        # Test 10x
        result = self.calc.eval("2 10x")
        self.assertEqual(result, 100)
        
        # Test ex
        result = self.calc.eval("1 ex")
        self.assertAlmostEqual(result, math.e)
        
        # Test atan
        result = self.calc.eval("1 atan")
        self.assertAlmostEqual(result, 45)
        
        # Test acos
        result = self.calc.eval("0 acos")
        self.assertAlmostEqual(result, 90)
    
    def test_error_cases(self):
        """Prueba casos de error adicionales."""
        # Raíz cuadrada negativa
        with self.assertRaises(RPNError):
            self.calc.eval("-1 sqrt")
        
        # Logaritmo de cero
        with self.assertRaises(RPNError):
            self.calc.eval("0 log")
        
        # Logaritmo natural de negativo
        with self.assertRaises(RPNError):
            self.calc.eval("-5 ln")
        
        # Arcsen fuera de dominio
        with self.assertRaises(RPNError):
            self.calc.eval("2 asin")
        
        # Arccos fuera de dominio
        with self.assertRaises(RPNError):
            self.calc.eval("2 acos")
        
        # Memoria inválida
        with self.assertRaises(RPNError):
            self.calc.eval("42 sto 99")
        
        # Token inválido en constantes
        with self.assertRaises(RPNError):
            self.calc.eval("x")
    
    def test_power_variants(self):
        """Prueba variantes de potencia."""
        # 10x con negativo
        result = self.calc.eval("-1 10x")
        self.assertAlmostEqual(result, 0.1)
        
        # ex con negativo
        result = self.calc.eval("-1 ex")
        self.assertAlmostEqual(result, math.exp(-1))
    
    def test_stack_edge_cases(self):
        """Prueba casos extremos de pila."""
        # Swap con pila vacía
        calc2 = RPNCalculator()
        with self.assertRaises(RPNError):
            calc2.eval("swap")
        
        # Dup con pila vacía
        calc3 = RPNCalculator()
        with self.assertRaises(RPNError):
            calc3.eval("dup")
        
        # Drop con pila vacía
        calc4 = RPNCalculator()
        with self.assertRaises(RPNError):
            calc4.eval("drop")
    
    def test_memory_edge_cases(self):
        """Prueba casos extremos de memoria."""
        # STO sin valor en pila
        calc2 = RPNCalculator()
        with self.assertRaises(RPNError):
            calc2.eval("sto 0")
        
        # RCL de memoria vacía
        calc3 = RPNCalculator()
        with self.assertRaises(RPNError):
            calc3.eval("rcl 5")
    
    def test_command_parsing(self):
        """Prueba parsing de comandos."""
        # Comando clear
        self.calc.eval("1 2 3 clear 5")
        self.assertEqual(self.calc.eval("5"), 5)


if __name__ == "__main__":
    unittest.main()