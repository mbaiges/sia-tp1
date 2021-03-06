# Trabajo Práctico Métodos Informados y Desinformados para la materia Sistemas de Inteligencia Artificial

## Instalación

Para correr el programa debe ser necesario instalar python 3

[Descargar Python 3](https://www.python.org/downloads/)

Una vez instalado python, se necesitan las librerías numpy y pygame.
Para eso, se debe tener instalado pip para python
La guía de instalación se encuentra en el siguiente link:

[Instalar Pip](https://tecnonucleous.com/2018/01/28/como-instalar-pip-para-python-en-windows-mac-y-linux/)

Una vez instalado pip, se debe correr, dentro de la carpeta del repositorio, el comando:

```python
pip install -r requirements.txt
```

## Guía de uso

Finalmente, para correr el trabajo se debe ejecutar el comando:

```python
python .\sokoban.py
```

Luego de esto, se pedirá que se elija el nivel, si se desea utilizar una optimización y el algoritmo a utilizar.

Para la busqueda IDDFS se pedirá también el numero de profundidad limite a utilizar

Para las busquedas informadas (GGS, A* y IDA*), se pedirá que se elija la heurística a utilizar.
Las posibles heurísticas son:
* Heurística 1: 
    
    Utiliza la suma entre la distancia de el jugador a la caja mas cercana y de esa caja al objetivo mas cercano
* Heurística 2:

    Se suman las distancias entre todas las cajas y su objetivo mas cercano disponible (que no haya sido tomado previamente por otra caja que se encontraba mas cercana a este objetivo) y se le suma la distancia entre el jugador y la caja mas cercana
* Heurística 3:

    Se toma la cantidad de cajas que no se encuentran en un objetivo
* Heurística 4:

    Crea un vector para el eje x y otro para el eje y del estado. En este array se cuenta la cantidad de objetivos - cajas que hay en esta fila o columna. Al final devuelve la mitad de la suma de los modulos de los distintos elementos del array. 
* Heurística 5:

    Devuelve la distancia entre el centro de masa de las cajas y el centro de masa de los objetivos

Cuando finalmente se ejecuta un nivel, se abre el visualizador. Los controles para controlarlos son los siguientes:

    → : Avanza al siguiente estado
    ← : Retrocede al estado anterior
    p : Inicia/pausa el avance de los estados de forma automática
    r : Reinicia el nivel
    esc : Cierra la ventana

## Agregar un mapa
Para agregar un mapa, se debe crear un archivo .txt en la carpeta levels y escribir el mapa donde cada caracter representa un cuadrado del tablero.
Los caracteres a usar son los siguientes:

    "#" : Pared
    "$" : Caja
    "@" : Jugador
    "." : Objetivo
    " " (espacio) : piso en blanco
    "*" : Caja arriba de un goal
    "+" : Player arriba de un goal


