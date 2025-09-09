# Maquina-de-Turing

# Proyecto: Máquina de Turing Simulada en Python

Este proyecto implementa una **simulación avanzada de una Máquina de Turing** en Python para realizar operaciones aritméticas básicas: **suma, resta, multiplicación, división, potenciación y raíz cuadrada**.

---

## Objetivos

- Comprender el modelo de Máquina de Turing y su importancia histórica.
- Implementar operaciones básicas simulando la lógica paso a paso de una máquina primitiva.
- Usar Python como herramienta de desarrollo.
- Aplicar buenas prácticas de programación, pruebas y documentación.

---

## Proceso de Diseño

### Planificación y roles sugeridos:
- Programador principal
- Diseñador lógico (pseudocódigo, diagramas)
- Tester/documentador

### Principios de diseño:
- Suma y resta mediante incrementos y decrementos.
- Multiplicación como suma repetida.
- División como resta sucesiva.
- Potenciación como multiplicación repetida.
- Raíz cuadrada por búsqueda secuencial.

---

## Operaciones implementadas

- `sumar(a, b)` → suma simulada.
- `restar(a, b)` → resta simulada.
- `multiplicar(a, b)` → multiplicación como sumas.
- `dividir(a, b)` → división como restas.
- `potenciar(base, exponente)` → multiplicación repetida.
- `raiz_cuadrada(n)` → búsqueda de raíz entera más cercana.

---

## Casos de prueba

| Operación       | Entrada        | Salida Esperada | Estado  |
|----------------|----------------|------------------|---------|
| Suma           | 3, 5           | 8                | ✅ OK   |
| Suma           | -2, 4          | 2                | ✅ OK   |
| Resta          | 10, 4          | 6                | ✅ OK   |
| Resta          | 4, 10          | -6               | ✅ OK   |
| Multiplicación | 7, 6           | 42               | ✅ OK   |
| Multiplicación | -3, 5          | -15              | ✅ OK   |
| División       | 20, 4          | 5                | ✅ OK   |
| División       | 10, 0          | Error            | ✅ OK   |
| Potenciación   | 2, 3           | 8                | ✅ OK   |
| Potenciación   | 2, -1          | Error            | ✅ OK   |
| Raíz cuadrada  | 16             | 4                | ✅ OK   |
| Raíz cuadrada  | 20             | 4                | ✅ OK   |
| Raíz cuadrada  | -9             | Error            | ✅ OK   |

---

## Archivos incluidos

- `maquina_de_turing.ipynb` → Cuaderno Colab con implementación y pruebas.
- `README.txt` → Este documento.
- (Opcional) `diagramas/` → Diagramas de flujo.
- (Opcional) `docs/` → Informe en PDF o Markdown.

---

## Diagrama de flujo sugerido

[Inicio]
↓
[Leer a, b]
↓
[Verificar operación]
↓
[Ejecutar bucles]
↓
[Mostrar resultado]
↓
[Fin]


---

## Cómo ejecutar

1. Abrir el archivo `maquina_de_turing.ipynb` en [Google Colab](https://colab.research.google.com/).
2. Ejecutar cada celda secuencialmente.
3. Verificar que todas las pruebas pasen correctamente.

---

## Recomendaciones para entrega en GitHub

- Sube todos los archivos al repositorio.
- Asegúrate de que el README.txt esté en la raíz del proyecto.
- Incluye capturas de los resultados si lo deseas.
- Agrega enlace al cuaderno Colab compartido.

---




