# ¿Qué son estructuras de datos?

Son formas sistematicas de organizar datos para ser usadas de forma eficiente.

Cada estructura de datos contiene:
* Una interfaz: Representa un conjunto de operaciones the soporta esa estructura de datos.
* Una implementación: Representación interna de la estructura de datos.

# Características de las estructuras de datos

* Exactitud: La implementación de la estructura de datos debe implementar su interfaz de forma correcta.
* Complejidad de tiempo: El tiempo de execución de las operaciones debe ser el menor posible.
* Complejidad de espacio: El uso de memoria de de una operación usando una estructura de datos debe ser el menor posible.

# Necesidades de una estructura de datos

Si almacenas millones o billones de datos en tu aplicación, necesitarás usarla eficientemente si tienes un alto volumen de personas
usando tu app.

# Maneras de comparar el tiempo de ejecución de una estructura de datos

* Peor Caso: Se representan como funciones, el peor caso, es donde la estructura de datos toma el tiempo máximo que podría obtener.
Si el peor caso de una estructura de datos es f(n), entonces nunca tomara mas de f(n).

* Caso Promedio: Describe el tiempo promedio de ejecución de una estructura de datos, si una operación dura f(n), entonces "m" operaciones podrian tomar m*f(n) tiempo.

* Mejor Caso: Este escenario describe el menor tiempo de execucion posible, 

# Glosario:

* Data: valores o conjunto de valores,
* Data Item: Se refiere a una unidad dentro de un conjunto de valores,
* Group Items: Subconjunto de varios Data Items,
* Elementary Items: Datos que no pueden ser separados son llamados Elementary Items,
* Atributos y Entidades: Una entidad es algo que contiene ciertos atributos o propiedades, que se le pueden asignar valores,
* Entity Set: Entidades de atributos similares forman una Entity Set,
* Campo: Unidad de información  que representa el atributo de una entidad,
* Record: Colección de valores de campos de una entidad dada,
* Archivos: Colección de Records de entidades de un conjunto de entidades.

# Algoritmos

Un algoritmo es un procedimiento desglosado paso a paso, que define una serie de instrucciones que son executadas en cierto orden, para obtener el resultado deseado.

Un algoritmo puede ser creado independientemente del lenguaje de programación usado, debido a que no depende de un lenguaje de programación en específico para ser implementado.

Hay distintas categorías de algoritmos:
* Busqueda: Se usan para buscar un(os) elemento(s) en una estructura de datos,
* Sorteo / Ordenamiento: Se usan para que los elementos en una estructura de datos estén presentados de una forma secuencial específica.
* Inserción: Añade elementos a la estructura de datos,
* Actualización: Busca un elemento en la estructura de datos y lo reemplaza con un nuevo valor,
* Eliminación: Elimina un elemento en una estructura de datos.

# Caraterísticas para que un procedimiento sea llamado algoritmo:

* Inambigüo: Cada uno de los pasos del algoritmo debe ser preciso y claro y solo hacer 1 cosa.
* Input: Un algoritmo debe tener 0 o más inputs bien definidos,
* Output: Un algoritmo debe tener 1 o más resultados, y debe coincidir con el resultado esperado, 
* Finitud (Finiteness): Un algoritmo debe tener un número de pasos finito, contable, 
* Factibilidad (Feasibility): Un algoritmo debe ser factible con los recursos disponibles, 
* Independiente: Un algoritmo debe ejecutarse sin importar el lenguaje de programación.

# Como escribir un algoritmo

Lo más importante para escribir un algoritmo, es definir y entender el problema que se quiere solucionar de manera clara y correcta, los algoritmos se escriben como procedimientos paso a paso.

### Ejemplo de estructuración de Algoritmos

**PROBLEMA**: Diseñar un algoritmo que sume dos números y muestre el resultado de la operación

1. INICIO
2. Declarar tres variables: **a**, **b**, & **c**.
3. Definir valores de **a** & **b**.
4. Sumar valores de **a** & **b**
5. Almacenar valores del paso 4 en **c**
6. Imprimir el valor de **c**
7. PARA

Un problema **puede ser resuelto en más de 1 forma**.

# Análisis Asintótico

# Greedy Algorithms (Algoritmos Voraces en español según wikipedia)

Problemas para investigar:
* [Travelling Salesman Problem]()
* [Prim's Minimal Spanning Tree Algorithm]()
* [Kruskal's Minimal Spanning Tree Algorithm]()
* [Dijkstra's Minimal Spanning Tree Algorithm]()
* [Graph - Map Coloring]()
* [Graph - Vertex Cover]()
* [Knapsack Problem]()
* [Job Scheduling Problem]()

# Divide and Conquer

Esta solución ofrece dividir el la data formando grupos, luego subgrupos, y así hasta que el problema pueda ser resuelto atómicamente, es decir, con una sola pieza de todo el conjunto de datos a la vez.

[Ejemplo de Divide and Conquer para hacer uppercasing de un string](https://www.tutorialspoint.com/data_structures_algorithms/images/divide_and_conquer.jpg)

## Algoritmos de Divide and Conquer
* Merge Sort
* Quick Sort
* Bubble Sort
* Multiplicación de matrices de Strassen's
* Par más cercano (puntos)

# Dynammic Programming (Programación Dinamica)

La programación dinámica es igual a Divide and Conquer, con la diferencia de que aquí los resultados de los sub problemas son recordados para su posterior uso.

## Algoritmos de programación dinámica
* Fibonacci number series
* Knapsack problem
* Tower of Hanoi
* All pair shortest path by Floyd-Warshall
* Shortest path by Dijkstra
* Project scheduling