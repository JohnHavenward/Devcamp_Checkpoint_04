# PREGUNTAS TEÓRICAS
</br>

### ¿Cuál es la diferencia entre una lista y una tupla en Python?
---
</br>

La principal diferencia entre ambas es que las listas son un tipo de estructura de datos mutable mientras que en el caso de las tuplas se trata de una estructura inmutable. Eso supone que al contrario de lo que ocurre con las listas las tuplas no permitan modificar sus elementos individualmente, no puedan ser reordenados y tampoco que estos  sean eliminados o añadidos.

Otra diferencia importante es que las listas se denotan con corchetes `[]` mientras que las tuplas lo hacen con paréntesis `()`, tal y como se muestra en el siguiente ejemplo:

```python
mi_lista = [56, 8, 23, 75, 12]

mi_tupla = ('Sandra', 'Eduardo' , 'Tania', 'Jorge')
```
</br>

Debido a su inmutabilidad las tuplas dependen de la reasignación para poder ser modificadas. A continuación se muestran varios ejemplos de operaciones básicas con tuplas:

```python
mi_tupla += ('elemento_nuevo',) # añadir un elemento

mi_tupla = mi_tupla[1:] # eliminar el primer elemento

mi_tupla = mi_tupla[:-1] # eliminar el último elemento
```
</br>

Tanto las listas como las tuplas permiten la extracción de valores mediante el proceso llamado *unpacking* que permite reasignar estos a una serie de variables. En este proceso es importante que el número de valores y sus posiciones dentro de la estructura de datos sea constante por lo que el uso de tuplas resulta mucho más adecuado debido a su carácter inmutable. Podemos ver un ejemplo de ello a continuación:

```python
mi_tupla = ('rojo', 'fresa' , 'lunes', 'silla')

(color, fruta, día, mueble) = mi_tupla

print(color) #rojo

print(fruta) #fresa

print(día) #lunes

print(mueble) #silla
```
</br></br></br>



### ¿Cuál es el orden de las operaciones?
---
</br>

Las operaciones aritméticas en python se evalúan en el orden de precedencia determinado por el nivel de prioridad de cada una. En caso de que varias operaciones tengan el mismo nivel de prioridad siempre se ejecutan de izquierda a derecha.
</br></br>

En la siguiente tabla se muestra el nivel de prioridad de cada operación:

Prioridad | Signo | Operación |
---: | :-----: | ---
**nivel 1**
| | () | Paréntesis
**nivel 2**
| | ** | Potencia
**nivel 3**
| | // | División con redondeo a la baja
| | * | Multiplicación
| | / | División
| | % | Módulo
**nivel 4**
| | + | Suma
| | - | Substracción
</br></br>

A continuación se muestra paso a paso el orden en el que python ejecutaría las operaciones para resolver este cálculo:

```python
5 * (10 + 3 ** 2 / 2) - 8

5 * (10 + 9 / 2) - 8

5 * (10 + 4.5) - 8

5 * 14.5 - 8

72.5 - 8

64.5

```
</br>


En este otro ejemplo todos los operadores tienen la misma prioridad y por tanto se ejecutan de izquierda a derecha:

```python
3 // 2 * 5 / 4 % 1

1 * 5 / 4 % 1

5 / 4 % 1

1.25 % 1

0.25

```
</br></br></br>



### ¿Qué es un diccionario Python?
---
</br>

Un diccionario es una estructura de datos que permite almacenar parejas de clave y valor, a las cuales también se puede referir como ítems. La clave o *key* puede contener espacios y se tiene en cuenta el uso de mayúsculas. El valor o *value* puede contener cualquier tipo de variable e incluso una colección de datos como por ejemplo una lista.

Para su definición se emplean llaves `{}` que contienen en su interior los ítems  separados por comas; y estos a su vez separan con un signo de dos puntos `:` la clave del valor. La primera parte del ítem siempre corresponde a la clave y la segunda al valor. Podemos ver un ejemplo a continuación.

```python
mi_diccionario = {
  "clave 1": "valor 1",
  "clave 2": "valor 2",
  "clave 3": "valor 3",
  "clave 4": "valor 4",
  "clave 5": ["UNO", "DOS", "TRES", "CUATRO", "CINCO"],
}
```
</br>

Para acceder a un elemento cuya clave conocemos se usa esta misma dentro de corchetes `mi_diccionario[clave]`. En el caso de que el valor contenido sea una colección podemos acceder a elementos de esta añadiendo directamente el índice tal y como se muestra en el ejemplo siguiente:

```python
segundo_valor = mi_diccionario["clave 2"]

cuarto_elemento = mi_diccionario["clave 5"][3]
```
</br>

Para añadir un ítem al diccionario simplemente debemos declarar la clave nueva y asignarle el valor deseado tal y como se muestra a continuación:

```python
mi_diccionario["clave 6"] = "valor 6"
```
</br>

Para buscar un ítem dentro del diccionario podemos usar la función `get()` la cual nos devuelve el valor asociado a la clave solicitada. Esta función también nos permite definir un valor por defecto a devolver si no se ha encontrado el ítem dentro del diccionario. A continuación se muestra su uso:

```python
noveno_valor = mi_diccionario.get("clave 9", "Ítem no econtrado")
```
</br>

Para eliminar un ítem tenemos dos opciones. Podemos utilizar la palabra clave `del` eliminando el ítem directamente o también podemos usar el método `pop()` que nos permite almacenar el valor devuelto en una variable a la vez que eliminamos el ítem y además nos da la posibilidad de retornar un valor por defecto en caso de que el ítem solicitado no exista. A continuación se muestra el uso de ambas formas:

```python
del mi_diccionario["clave 3"]

valor_eliminado = mi_diccionario.pop("clave 5", "Ítem no econtrado")
```
</br>

Por último cabe mencionar que un diccionario nos permite visualizar los diferentes elementos que lo componen mediante tres tipos de *view objects* que son los siguientes: 

- `keys()` nos devuelve una lista de todas las claves del diccionario
- `values()` nos devuelve una lista de todos los valores del diccionario
- `items()` nos devuelve una lista de tuplas de todos los ítems contenidos en el diccionario
</br></br>

Se muestra un ejemplo con el uso de los tres tipos a continuación:

```python
resultados = {'x': 8, 'y': 2, 'z': 11}

keys_view = resultados.keys()
print(keys_view) #dict_keys(['x', 'y', 'z'])

values_view = resultados.values()
print(values_view) #dict_values([8, 2, 11])

items_view = resultados.items()
print(items_view) #dict_items([('x', 8), ('y', 2), ('z', 11)])
```
</br>

La visualización de estos elementos tiene una naturaleza dinámica y por ello al alterarlos se alterará el diccionario también. En caso de que ese no sea el resultado deseado debemos usar la función `copy()` que nos devuelve una copia desvinculada del diccionario original. También podemos usar la función `list()` para que el objeto retornado sea una lista tal y como se muestra a continuación:

```python
copied_keys_view = list(resultados.copy().keys())
print(copied_keys_view) #['x', 'y', 'z']

copied_values_view = list(resultados.copy().values())
print(copied_values_view) #[8, 2, 11]

copied_items_view = list(resultados.copy().items())
print(copied_items_view) #[('x', 8), ('y', 2), ('z', 11)]
```
</br></br></br>



### ¿Cuál es la diferencia entre el método ordenado y la función de ordenación?
---
</br>

Ambas funciones sirven para ordenar una lista de forma alfabética e igualmente permiten añadir el parámetro `reverse` para invertir el orden.

Sin embargo, la principal diferencia es que la función `sort()` altera la lista sobre la que se ejecuta mientras que `sorted()` no lo hace. Por ello el resultado obtenido con `sorted()` debe guardarse en otra variable o reasignarse a la propia lista para poder conservar el resultado obtenido.  Cabe resaltar que la función `sort()` no devuelve ningún resultado y por lo tanto no puede asignarse a una variable.
</br></br>

A continuación se muestra un ejemplo de  uso de ambas funciones:


#### SORT
```python
mi_lista = ['elemento_c', 'elemento_b', 'elemento_d', 'elemento_a']

mi_lista.sort()
print(mi_lista) # ['elemento_a', 'elemento_b', 'elemento_c', 'elemento_d']

mi_lista.sort(reverse = True)
print(mi_lista) # ['elemento_d', 'elemento_c', 'elemento_b', 'elemento_a']
```
</br>


#### SORTED
```python
mi_lista = ['elemento_c', 'elemento_b', 'elemento_d', 'elemento_a']

lista_ordenada = sorted(mi_lista)
print(lista_ordenada) # ['elemento_a', 'elemento_b', 'elemento_c', 'elemento_d']

lista_ordenada_invertida = sorted(mi_lista, reverse = True)
print(lista_ordenada_invertida) # ['elemento_d', 'elemento_c', 'elemento_b', 'elemento_a']
```
</br></br></br>



### ¿Qué es un operador de reasignación?
---
</br>

Un operador de reasignación realiza los siguientes dos pasos en uno solo:
- Realiza una operación matemática entre una variable y un valor
- Reasigna el resultado a la propia variable
</br></br>

Sirve para abreviar el código y hacerlo más legible ya que evita tener que repetir el nombre de la variable. En el siguiente ejemplo podemos ver su uso:

```python
total += 10
```
</br>

La siguiente línea de código sería la equivalente:

```python
total = total + 10
```
</br>

Los diferentes operador de reasignación se componen del signo igual precedido del símbolo que representa la operación matemática. En la siguiente tabla podemos ver algunos de los operadores de reasignación y la operación matemática a la que corresponden: 

Símbolo | Operación
:-----: | ---------
+= | Suma
-= | Substracción
*= | Multiplicación
/= | División
//= | División con redondeo a la baja
**= | Potencia
%= | Módulo