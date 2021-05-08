# Ricardo Daniel Díaz Granados - A00827266
# Reflexión individual - En esta actividad utilicé los módulos random, turtle y freegames de Python
#                        para crear un memorama. Asimismo, aprendí a importar imágenes utilizando la
#                        función path del módulo freegames. Esta actividad representó grandes retos para
#                        mí, sobre todo porque inicialmente quise hacer que el memorama incluyera artistas
#                        y nombres de alguna de sus canciones como sus pares. Sin embargo, debido a que
#                        no soy programador y no tengo conocimientos tan avanzados de Python, al final
#                        decidí resolver este problema eliminando los nombres de las canciones y dejando
#                        solo los nombres de los artistas y grupos musicales. Pero, aunque no pude plasmar
#                        lo que inicialmente quería, creo que si pongo en práctica mis conocimientos de
#                        Python con más frecuencia, seré capaz de lograr mi propuesta inicial, así como
#                        otras propuestas más desafiantes.
# 7 - Mayo - 2021

# Link al video de demostración del juego: https://drive.google.com/file/d/1AzJmp62UajqHK9PvBmvE-46HMYcdHmz9/view?usp=sharing

"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.

"""

from random import *
from turtle import *
from freegames import path

# recorre la ruta completa al 'filename' en el módulo freegames
car = path('car.gif')

# lista compuesta con el nombre de 32 artistas y bandas musicales distintos
tiles = ['Green Day', 'Paramore', 'Bon Jovi', 'AC/DC', 'Metallica', 'Megadeth', 'Bring Me The Horizon',
         'Audioslave', 'Rage Against the Machine', 'Muse', 'Alter Bridge', 'Owl City', 'Foo Fighters',
         'Polyphia', 'Covet', 'Chon', 'Animals As Leaders', 'Normandie', 'Spiritbox', 'Jinjer',
         'Kim Petras', 'Bea Miller', 'Yonaka', 'K/DA', 'Billie Eilish', 'Rosalía', 'Babi',
         'Son Lux', 'Sub Urban', 'Bahari', 'Yorushika', 'Nothing But Thieves']
# se duplica la lista para que sean 64 cartas en total
tiles = tiles * 2
state = {'mark': None}
hide = [True] * 64

# se crea el contador taps y se iguala a 0
taps = 0

def square(x, y):
    "Draw pink square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'pink')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

# asigna un número a cada nombre de la lista en base a su ubicación dentro de la lista
def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

# convierte el índice a coordenadas
def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

# la función hace un callback al dar click sobre la ventana
def tap(x, y):
    global mark, taps
    
    # imprime las coordenadas donde se dio click
    print(x,y)
    
    taps = taps + 1
    
    "Update mark and hidden tiles based on tap."
    # retorna el índice correspondiente a (x,y) en tiles[spot]
    spot = index(x, y)
    
    # saca el valor de state (inicialmente es None)
    mark = state['mark']

    ''' si mark es None o si mark == spot, el usuario dio click en la misma carta al índice sobre el cuál
        el usuario dio click, o si la carta que ya esta marcada es diferente de la seleccionada'''
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        # el estado cambia a la carta donde el usuario dio click
        state['mark'] = spot
    else:
        # las cartas son pares (se hacen visibles)
        hide[spot] = False
        hide[mark] = False
        # vuelve mark a None (no tenemos una carta visible)
        state['mark'] = None

def draw():
    "Draw image and tiles."
    # limpia la ventana
    clear()
    
    # mueve el turtle a la posición 0,0
    goto(0, 0)
    
    # carga la imagen del auto en el turtle shape
    shape(car)
    
    # plasma una copia del turtle en el canvas en la posición actual del turtle
    # dibuja el auto, el centro de la imagen se pone en la coordenada donde está el turtle
    stamp()
    # dibuja las 64 cartas del memorama (tapa la imagen del auto)
    # inicialmente todas las cartas están escondidas (tapan el auto)
    contador = 0
    for count in range(64):
        # si la carta aún no está descubierta, su valor es True
        if hide[count]:
            # obtiene la esquina inferior izquierda a partir de la cual se dibujará la carta
            x, y = xy(count)
            # dibuja un square en la posición x,y (esquina inferior izquierda)
            square(x, y)
            # cuenta la cantidad de cartas escondidas
            contador = contador + 1
            
            #si hide[count]==False -> no lo dibuja
    
    # ¿qué almacena state?
    #    None (sin carta visible)
    #    #### (índice de la carta visible)
    mark = state['mark']

    # despliega la carta donde se dio el click
    # si no está visible, hide[mark] == True, por lo que no se dibujará nada
    # determina que hacer si el estado es None y no hay cartas visibles
    if (mark is not None) and (hide[mark] == True):
        # calcula la posición x,y de la carta
        x, y = xy(mark)
        # levanta el lápiz
        up()
        # mueve el turtle a la posición x+2, y
        goto(x + 2, y)
        # cambiar el color del lápiz a negro
        color('black')
        # despliega en esa posición x+2 y el número de la carta oculta
        write(tiles[mark], font=('Arial', 10, 'normal'))

    # verifica si ya logró encontrar todos los pares
    escondidas = hide.count(True)
    print("Sin encontrar hide.count(True)=", escondidas)
    print("Sin encontrar contador=", contador)
    if escondidas == 0:
        up()
        goto(-120,120)
        color('white')
        write('GANASTE :D', font=('Arial',30, 'normal'))
        up()
        goto(-35,110)
        color('white')
        write(f'Hiciste {taps} taps')
        nombres()
        return

    # muestra en la ventana lo dibujado
    update()
    # llama a la función draw() cada 100 ms
    ontimer(draw, 100)

# escribe en el turtle el nombre de la persona que escribió el código
def nombres():
    up()
    goto(-110,-120)
    color('white')
    write('Ricardo Daniel Díaz Granados A00827266', font=('Arial',10, 'normal'))

# revuelve o mezcla las cartas del memorama
shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()