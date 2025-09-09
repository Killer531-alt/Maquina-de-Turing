# ---------------------------------------------------------------
# Clase MaquinaDeTuring: Manejo de operaciones basicas
# ---------------------------------------------------------------

class MaquinaDeTuring:
    def __init__(self):
        print("Máquina de Turing inicializada")

    def sumar(self, a: int, b: int) -> int:
        """Simula la suma como incrementos sucesivos."""
        resultado = a
        paso = 1 if b > 0 else -1
        for _ in range(abs(b)):
            resultado += paso
        return resultado

    def restar(self, a: int, b: int) -> int:
        """Simula la resta como decrementos sucesivos."""
        resultado = a
        paso = -1 if b > 0 else 1
        for _ in range(abs(b)):
            resultado += paso
        return resultado

    def multiplicar(self, a: int, b: int) -> int:
        """Simula la multiplicación como suma repetida."""
        negativo = (a < 0) ^ (b < 0)
        a, b = abs(a), abs(b)
        resultado = 0
        for _ in range(b):
            resultado = self.sumar(resultado, a)
        return -resultado if negativo else resultado

    def dividir(self, a: int, b: int):
        """Simula la división como restas repetidas."""
        if b == 0:
            return "Error: División por cero"
        negativo = (a < 0) ^ (b < 0)
        a, b = abs(a), abs(b)
        cociente = 0
        while a >= b:
            a = self.restar(a, b)
            cociente = self.sumar(cociente, 1)
        return -cociente if negativo else cociente

    def potenciar(self, base: int, exponente: int):
        """Simula la potenciación como multiplicaciones repetidas."""
        if exponente < 0:
            return "Error: Exponente negativo no soportado"
        resultado = 1
        for _ in range(exponente):
            resultado = self.multiplicar(resultado, base)
        return resultado

    def raiz_cuadrada(self, numero: int):
        """Simula la raíz cuadrada como búsqueda sucesiva."""
        if numero < 0:
            return "Error: Raíz de número negativo no soportada"
        resultado = 0
        while self.multiplicar(resultado + 1, resultado + 1) <= numero:
            resultado = self.sumar(resultado, 1)
        return resultado


# ---------------------------------------------------------------
# Casos de prueba para validar todas las operaciones
# ---------------------------------------------------------------

mt = MaquinaDeTuring()

print("\nSUMA")
print("3 + 5 =", mt.sumar(3, 5))             # 8
print("-2 + 4 =", mt.sumar(-2, 4))           # 2
print("0 + 0 =", mt.sumar(0, 0))             # 0

print("\nRESTA")
print("10 - 4 =", mt.restar(10, 4))          # 6
print("4 - 10 =", mt.restar(4, 10))          # -6
print("0 - 0 =", mt.restar(0, 0))            # 0

print("\nMULTIPLICACIÓN")
print("7 * 6 =", mt.multiplicar(7, 6))       # 42
print("-3 * 5 =", mt.multiplicar(-3, 5))     # -15
print("-3 * -2 =", mt.multiplicar(-3, -2))   # 6

print("\nDIVISIÓN")
print("20 / 4 =", mt.dividir(20, 4))         # 5
print("10 / 0 =", mt.dividir(10, 0))         # Error
print("-15 / 3 =", mt.dividir(-15, 3))       # -5

print("\nPOTENCIACIÓN")
print("2 ^ 3 =", mt.potenciar(2, 3))         # 8
print("5 ^ 0 =", mt.potenciar(5, 0))         # 1
print("2 ^ -1 =", mt.potenciar(2, -1))       # Error

print("\nRAÍZ CUADRADA")
print("√16 =", mt.raiz_cuadrada(16))         # 4
print("√20 =", mt.raiz_cuadrada(20))         # 4
print("√-9 =", mt.raiz_cuadrada(-9))         # Error
