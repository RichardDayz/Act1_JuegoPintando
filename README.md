# Act3_Pacman
#José Andrés Villarreal Montemayor  A00829355
#Ricardo Daniel Díaz Granados       A00827266

"""Pacman, classic arcade game.

Exercises

1. Change the board.
2. Change the number of ghosts.
3. Change where pacman starts.
4. Make the ghosts faster/slower.
5. Make the ghosts smarter.

"""

# se hace import de todas las librerías necesarias al inicio

# elige un valor aleatorio de una lista
from random import choice
from turtle import *
from freegames import floor, vector

# almacena la puntuación (cantidad de galletas consumidas por el Pacman)
state = {'score': 0}
# hace invisible la flecha creando dos objetos de la clase Turtle
path = Turtle(visible=False)
writer = Turtle(visible=False)

# da la dirección del Pacman
aim = vector(5, 0)

# crea pacman en la posición (-40,-80)
pacman = vector(-40, -80)
# lista de listas con la posición inicial de los fantasmas y su dirección de movimiento
ghosts = [
    [vector(-180, 160), vector(5, 0)],
    [vector(-180, -160), vector(0, 5)],
    [vector(100, 160), vector(0, -5)],
    [vector(100, -160), vector(-5, 0)],
]

# lista del tablero para simular 20 columnas y 20 renglones actualizado
tiles = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
    0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0,
    0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
    0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0,
    0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0,
    0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0,
    0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0,
    0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0,
    0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
    0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0,
    0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0,
    0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
    0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0,
    0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]

# dibuja un square con su esq. inf. izq en (x, y)
def square(x, y):
    "Draw square using path at (x, y)."
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()

    for count in range(4):
        path.forward(20)
        path.left(90)

    path.end_fill()

def offset(point):
    "Return offset of point in tiles."
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 20)
    return index

# retorna True si point es un tile válido
def valid(point):
    "Return True if point is valid in tiles."
    index = offset(point)

    # si la celda es 0 regresa False (muro)
    if tiles[index] == 0:
        return False

    index = offset(point + 19)

    # si la celda es 0 regresa False (muro)
    if tiles[index] == 0:
        return False

    return point.x % 20 == 0 or point.y % 20 == 0

def world():
    "Draw world using path."
    bgcolor('black')
    path.color('blue')

    # recorre toda la lista de (tiles)
    for index in range(len(tiles)):
        # extrae el valor que existe en la posición index
        tile = tiles[index]

        # si el valor 1
        if tile > 0:
            # calcula la x, y donde se dibuja el square
            x = (index % 20) * 20 - 200    # (21 % 20) * 20 - 200 = -180
            y = 180 - (index // 20) * 20   # 180 - (21 // 20) * 20 = 160
            square(x, y)                   # dibuja el square (-180, 160)

            # dibuja la galleta sobre el square
            if tile == 1:
                path.up()
                path.goto(x + 10, y + 10)
                path.dot(2, 'white')

def move():
    # establece los colores de los fantasmas
    colores = ['red', 'white', 'pink', 'cyan']
    k = 0
    "Move pacman and all ghosts."
    writer.undo()
    valor = state['score']
    # muestra el score en la ventana del juego
    writer.write(f'Score: {valor}')

    # limpia la ventana
    clear()

    # si es una posición válida (no pared) pacman.move(aim)
    if valid(pacman + aim):
        pacman.move(aim)
    
    # retorna la posición del Pacman en el tablero
    index = offset(pacman)

    #1 (camino)
    if tiles[index] == 1:
        # a esa posición le asigna 2 (comer la galleta)
        tiles[index] = 2
        # se incrementa el score
        state['score'] += 1
        # calcula la posición x, y del Pacman
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        # dibuja el square (sin la galleta)
        square(x, y)

    up()
    # se va a la posición del Pacman
    goto(pacman.x + 10, pacman.y + 10)
    # primera vez que dibuja el Pacman
    dot(20, 'yellow')

    # [vector(-180,160), vector(5,0)]
    for point, course in ghosts:
        # valida si el fantasma (point) se puede mover en course
        if valid(point + course):
            point.move(course)
        else: # si no se puede mover el fantasma en esa dirección
            # se actualiza la dirección del movimiento del mismo
            # compara posición del pacman con fantasmas para que lo sigan
            if pacman.x > point.x:
                options = vector(5,0)
            elif pacman.y > point.y:
                options = vector(0, 5)
            elif pacman.x < point.x:
                options = vector(-5,0)
            elif pacman.y < point.y:
                options = vector(0, -5)
            else:
                movimientos = [
                    vector(5, 0),
                    vector(-5, 0),
                    vector(0, 5),
                    vector(0, -5),
                ]
                options = choice(movimientos)
            course.x = options.x
            course.y = options.y
        # levanta
        up()
        # mueve a la posición del fantasma
        goto(point.x + 10, point.y + 10)
        # le asigna un color a cada fantasma
        dot(20, colores[k])
        k = k + 1

    update()
    # recorre la lista de fantasmas para ver si coinciden las
    # posiciones del Pacman y de algún fantasma
    for point, course in ghosts:
        if abs(pacman - point) < 20:
            # si el Pacman toca a un fantasma, se despliega "GAME OVER" y el score obtenido
            writer.goto(-110, 10)
            writer.write('GAME OVER', font=('Arial', 20, 'normal'))
            writer.goto(-80, -20)
            writer.write(f'Score: {valor}', font=('Arial', 20, 'normal'))
            return
    # vuelve a llamar la función dentro de 25 milisegundos
    ontimer(move, 25)

def change(x, y):
    "Change pacman aim if valid."
    if valid(pacman + vector(x, y)):
        aim.x = x
        aim.y = y

# inicializa la ventana ancho y alto 420, 420
# 0,0 indica la ubicación de la esquina  sup. izq. de la ventana en mi pantalla
setup(420, 420, 370, 0)

# esconde la flecha
hideturtle()

# oculta toda forma de dibujar
tracer(False)
# mueve la turtle writer a la posición 160, 160
writer.goto(160, 160)
writer.color('white')
writer.write(state['score'])
# escucha los eventos del teclado
listen()
# en caso de que el usuario oprima la tecla indicada, manda llamar a la función change
# con los argumentos indicados
onkey(lambda: change(5, 0), 'Right')
onkey(lambda: change(-5, 0), 'Left')
onkey(lambda: change(0, 5), 'Up')
onkey(lambda: change(0, -5), 'Down')
world()
move()
done()
