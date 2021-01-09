## Linked Lists

Es una estructura de datos lineal (Lo que significa que los elementos están dispuestos de una manera *secuencial* y cada miembro está conectado al anterior y al siguiente elemento)

Las linked lists no están almacenadas en locación contigua, los elementos se enlazan a través de apuntadores.

* Su tamaño es dinámico, a diferencia de los arreglos.
* El acceso aleatorio no está permitido, para acceder a los elementos, hay que recorrerlos desde el primer nodo.
* Se requiere espacio extra por cada nodo por el apuntador.

El primer nodo se le llama cabeza o _head_

```python

class Node:

    ## Inicializar el objeto nodo con un constructor
    def __init__(self, data):
        self.data = data # Asignar data
        self.next = None # Inicializa next como nulo

class LinkedList:

    # Funcion para inicializar el objeto LinkedList
    def __init__(self):
        self.head = None
```