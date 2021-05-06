#José Andrés Villarreal Montemayor  A00829355
#Ricardo Daniel Díaz Granados       A00827266
"""Reflexión Andrés: Esta actividad me hizo tener ciertos problemas que no entendía y me frustró bastante,
sin embargo, gracias a escuchar dudas de compañeros, entendí que debía usar variables globales para poder
referenciarlas."""
"""Reflexión Ricardo: Para mí esta actividad fue bastante complicada, ya que yo no estudio programación ni
tampoco conocimientos avanzados de Python. Sin embargo, con ayuda de mi profesora y compañeros logré cumplir
con mi parte del trabajo. Aún así, creo que la parte del código que realicé aún podría mejorar."""

"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.

"""

from turtle import *
from random import randrange, sample
from freegames import square, vector

food = vector(0, 0)
# lista con las posibles direcciones en las que se puede mover la comida
movimiento_food = [vector(10, 0), vector(-10,0), vector(0,10), vector(0,-10)]
snake = [vector(10, 0)]
aim = vector(0, -10)

# se establece una lista con los colores que tomará la snake y la comida
colores = ['blue', 'pink', 'cyan', 'green', 'orange']
colorRandom = sample(colores, 2)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    # si la cabeza está dentro de la ventana retorna True, si no regresa False
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    global colorRandom
    # define la posición de la cabeza dentro del vector "snake"    
    head = snake[-1].copy()
    # mueve "head" en la dirección indicada por el usuario
    head.move(aim)
    # verifica si la cabeza está dentro de la ventana o si se superpone con "snake"
    # si se cumple una de las condiciones, "head"=rojo y acaba el juego
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    # agrega un un cuadro al final del cuerpo de la serpiente
    snake.append(head)
    
    # verifica si la cabeza tocó la comida
    if head == food:
        # imprime en consola el largo de la serpiente
        print('Snake:', len(snake))
        # genera una nueva posición aleatoria para la comida dentro de la ventana
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        #obtiene dos colores aleatorios de la lista previamente dada
        colorRandom = sample(colores,2)
    else:
        # borra el primer cuadro que se añadió al cuerpo de la serpiente si no se tocó la comida
        snake.pop(0)
        # mueve la comida de manera aleatoria en una de las 4 direcciones previamente establecidas
        food.move(movimiento_food[randrange(0, 4)])
        # si la comida sale de la ventana, la devuelve al origen
        if not inside(food):
            food.x = 0
            food.y = 0
        
    # borra la serpiente y la comida antes de redibujarlas en sus nuevas posiciones
    clear()

    # dibuja el cuerpo de la serpiente y le asigna el primer color obtenido aleatoriamente
    for body in snake:
        square(body.x, body.y, 9, colorRandom[0])

    # dibuja la comida y le asigna el segundo color obtenido aleatoriamente
    square(food.x, food.y, 9, colorRandom[1])
    # actualiza los dibujos de la serpiente y de la comida en la ventana del turtle
    update()
    # llama a la función de movimiento cada 100 ms
    ontimer(move, 200)

# ubicación y tamaño de la ventana
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
# cambios de dirección de la serpiente asignados a las flechas del teclado
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
