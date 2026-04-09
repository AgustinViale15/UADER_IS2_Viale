#!/usr/bin/env python3
"""
Calculadora RPN con pila, funciones, constantes y memorias.
"""

import math
import sys


class RPNError(Exception):
    """Excepción personalizada para errores RPN."""

    pass


class RPNCalculator:
    def __init__(self):
        self.stack = []
        self.mem = [None] * 10  # Usar None para memorias vacías

    # ----------- helpers -----------

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.stack:
            raise RPNError("Pila insuficiente")
        return self.stack.pop()

    def need(self, n):
        if len(self.stack) < n:
            raise RPNError("Pila insuficiente")

    # ----------- operaciones -----------

    def binary(self, op):
        self.need(2)
        b = self.pop()
        a = self.pop()

        if op == "+":
            self.push(a + b)
        elif op == "-":
            self.push(a - b)
        elif op == "*":
            self.push(a * b)
        elif op == "/":
            if b == 0:
                raise RPNError("División por cero")
            self.push(a / b)

    def unary(self, op):
        self.need(1)
        x = self.pop()

        if op == "sqrt":
            if x < 0:
                raise RPNError("Raíz cuadrada de número negativo")
            self.push(math.sqrt(x))
        elif op == "log":
            if x <= 0:
                raise RPNError("Logaritmo de número no positivo")
            self.push(math.log10(x))
        elif op == "ln":
            if x <= 0:
                raise RPNError("Logaritmo natural de número no positivo")
            self.push(math.log(x))
        elif op == "sin":
            self.push(math.sin(math.radians(x)))
        elif op == "cos":
            self.push(math.cos(math.radians(x)))
        elif op == "tg":
            self.push(math.tan(math.radians(x)))
        elif op == "asin":
            if x < -1 or x > 1:
                raise RPNError("Arcsen fuera de dominio")
            self.push(math.degrees(math.asin(x)))
        elif op == "acos":
            if x < -1 or x > 1:
                raise RPNError("Arccos fuera de dominio")
            self.push(math.degrees(math.acos(x)))
        elif op == "atan":
            self.push(math.degrees(math.atan(x)))
        elif op == "chs":
            self.push(-x)
        elif op == "inv":
            if x == 0:
                raise RPNError("División por cero")
            self.push(1 / x)
        else:
            raise RPNError(f"Función inválida: {op}")

    def power(self, op):
        if op == "ex":
            self.need(1)
            x = self.pop()
            self.push(math.exp(x))
        elif op == "10x":
            self.need(1)
            x = self.pop()
            self.push(10**x)
        elif op == "yx":
            self.need(2)
            b = self.pop()
            a = self.pop()
            self.push(a**b)

    # ----------- pila -----------

    def stack_cmd(self, cmd):
        if cmd == "dup":
            self.need(1)
            self.push(self.stack[-1])
        elif cmd == "swap":
            self.need(2)
            self.stack[-1], self.stack[-2] = self.stack[-2], self.stack[-1]
        elif cmd == "drop":
            self.need(1)
            self.pop()
        elif cmd == "clear":
            self.stack.clear()

    # ----------- memorias -----------

    def memory(self, cmd, idx):
        i = int(idx)
        if not 0 <= i <= 9:
            raise RPNError("Memoria inválida")

        if cmd == "sto":
            self.need(1)
            valor = self.pop()
            self.mem[i] = valor
            self.push(valor)  # Devolver el valor a la pila
        elif cmd == "rcl":
            if self.mem[i] is None:
                raise RPNError(f"Memoria {i:02d} vacía")
            self.push(self.mem[i])

    # ----------- constantes -----------

    def constant(self, token):
        if token == "p":
            self.push(math.pi)
        elif token == "e":
            self.push(math.e)
        elif token == "j":
            self.push((1 + math.sqrt(5)) / 2)
        else:
            raise RPNError(f"Token inválido: {token}")

    # ----------- ejecución -----------

    def eval(self, expr):
        # Reiniciar la pila para cada expresión
        self.stack = []
        tokens = expr.split()

        i = 0
        while i < len(tokens):
            t = tokens[i]

            # Intentar parsear como número
            try:
                self.push(float(t))
            except ValueError:
                # Operaciones binarias
                if t in "+-*/":
                    self.binary(t)
                # Funciones unarias
                elif t in (
                    "sqrt",
                    "log",
                    "ln",
                    "sin",
                    "cos",
                    "tg",
                    "asin",
                    "acos",
                    "atan",
                    "chs",
                    "inv",
                ):
                    self.unary(t)
                # Funciones de potencia
                elif t in ("ex", "10x", "yx"):
                    self.power(t)
                # Comandos de pila
                elif t in ("dup", "swap", "drop", "clear"):
                    self.stack_cmd(t)
                # Comandos de memoria
                elif t in ("sto", "rcl"):
                    if i + 1 >= len(tokens):
                        raise RPNError("Falta índice de memoria") from None
                    i += 1
                    self.memory(t, tokens[i])
                # Constantes
                elif t in ("p", "e", "j"):
                    self.constant(t)
                else:
                    raise RPNError(f"Token inválido: {t}") from None

            i += 1

        if len(self.stack) != 1:
            raise RPNError("La pila no terminó con un único valor")

        return self.stack.pop()


def main():
    try:
        if len(sys.argv) > 1:
            expr = " ".join(sys.argv[1:])
        else:
            expr = input("RPN> ")
        calc = RPNCalculator()
        result = calc.eval(expr)
        print(result)
    except RPNError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
