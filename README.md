# Bitácora Semana Tec-Herramientas computacionales: el arte de la programación
## Actividad 1-Paint: Mayo 4, 2021
En la "Actividad 1-Paint" tuvimos la tarea de crear un programa usando el módulo **turtle** de Python. Para completar esta actividad fue necesario añadir un color adicional, así como realizar la programación necesaria para dibujar un círculo, un rectángulo y un triángulo.

Para dibujar el círculo Andrés añadió las siguientes líneas de código:

    #utiliza un ciclo de rango 4 para dibujar un cuadrado
    for count in range(4):
        #obtiene el lado
        forward(end.x - start.x)
        #rota 90°
        left(90)

    end_fill()

Por otro lado, para añadir un color nuevo, escribió lo siguiente:
    
    #se agrega color purple
    onkey(lambda: color('purple'), 'P')

Para dibujar el rectángulo, Ricardo añadió el siguiente código:

    def rectangle(start, end):
        "Draw rectangle from start to end."
        up()
        goto(start.x, start.y)
        down()
        begin_fill()

        #utiliza un ciclo de rango 2 para dibujar un rectángulo
        for count in range(2):
            #obtiene el largo
            forward(end.x - start.x)
            #rota 90°
            left(90)
            #obtiene la altura dividiendo el largo entre 2
            forward((end.x - start.x)/2)
            #rota 90°
            left(90)

        end_fill()

Finalmente, para dibujar el triángulo, añadió al código las siguientes líneas:

    def triangle(start, end):
        "Draw triangle from start to end."
        up()
        goto(start.x, start.y)
        down()
        begin_fill()

        #utiliza un ciclo de rango 3 para dibujar un triángulo equilátero
        for count in range(3):
            #obtiene el lado
            forward(end.x - start.x)
            #rota 120°
            left(120)

        end_fill()

## Actividad 2-Snake: Mayo 5, 2021
En la "Actividad 2-Snake" utilizamos los módulos **turtle**, **random** y **freegames** de Python para recrear el clásico juego de la serpiente. Partimos de un código base el cuál ya ejecutaba el juego, pero le hicimos modificaciones al código para que tanto la comida como la serpiente cambiaran de color aleatoriamente, adoptando un color nuevo de entre una lista de 5 colores distintos. Además de esto, hicimos que la comida se moviera aleatoriamente pero sin salirse de la ventana del **turtle** previamente delimitada.

Para que los colores cambiaran aleatoriamente pero sin que la serpiente y la comida tuvieran el mismo color, Andrés hizo lo siguiente:
1. Definió una lista con los 5 colores que podían adoptar tanto la serpiente como la comida, y definió una variable llamada *colorRandom*:

        # se establece una lista con los colores que tomará la snake y la comida
        colores = ['blue', 'pink', 'cyan', 'green', 'orange']
        colorRandom = sample(colores, 2)
        
2. Estableció la variable *colorRandom* como una variable **global**, insertando estas líneas de código dentro de la función *move()* creada para el juego:
        
        def move():
            "Move snake forward one segment."
            global colorRandom
            
3. Para que la serpiente y la comida cambiaran de color, hizo que cada vez que la serpiente coma la comida, se cree una lista con dos colores aleatorios distintos extraídos de la lista *colores*, y se guarden en la variable *colorRandom*:
        
                #obtiene dos colores aleatorios de la lista previamente dada
                colorRandom = sample(colores,2)
                
4. Finalmente, hizo que la serpiente tomara como color el primer valor guardado en *colorRandom*, mientras que la comida tomaría el segundo valor de esta misma lista:

            for body in snake:
                square(body.x, body.y, 9, colorRandom[0])

            # dibuja la comida y le asigna el segundo color obtenido aleatoriamente
            # dibuja la comida y le asigna "green" como color
            square(food.x, food.y, 9, colorRandom[1])
            
Para que la comida se moviera aleatoriamente pero sin salirse de la ventana del **turtle**, Ricardo añadió lo siguiente:
1. Creó una lista con las posibles direcciones (expresadas en forma de vectores) en las que se podía mover la comida:
        
        # lista con las posibles direcciones en las que se puede mover la comida
        movimiento_food = [vector(10, 0), vector(-10,0), vector(0,10), vector(0,-10)]
        
2. Finalmente, hizo que cuando la comida saliera de la ventana **turtle**, esta regresara al origen. Estas líneas de código las incluyo dentro del **else** de la función *move()*:

            else:
                # borra el primer cuadro que se añadió al cuerpo de la serpiente si no se tocó la comida
                snake.pop(0)
                # mueve la comida de manera aleatoria en una de las 4 direcciones previamente establecidas
                food.move(movimiento_food[randrange(0, 4)])
                # si la comida sale de la ventana, la devuelve al origen
                if not inside(food):
                    food.x = 0
                    food.y = 0

## Actividad 3-Pacman: Mayo 6, 2021
En la "Actividad 3-Pacman", se recreó el juego clásico de la consola ATARI *Pacman*. Se trabajó con un código base que ejecutaba el juego haciendo que los fantasmas se movieran aleatoriamente. Para completar la actividad, se modificó el código para que cambiara el tablero, los fantasmas se movieran más rápido y que además actuaran con un mayor nivel de inteligencia.

Para cambiar el tablero, se modificó la matriz de 1's y 0's que representaba al tablero. De esta forma, al desplegar la matriz actualizada la forma del tablero sería diferente:

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

Para que los fantasmas se movieran más rápido, se modificó la frecuencia con la que la función *ontimer* llamaba la función *move()* creada para el juego. Para hacer esto, se redujo el tiempo que tarda *ontimer* en llamar a *move()* otra vez, disminuyendo de 100ms a 25ms:

        # vuelve a llamar la función dentro de 25 milisegundos
        ontimer(move, 25)
        
Posteriormente, para que los fantasmas actuaran con mayor inteligencia se creó una serie de **if's** que comparan la posición relativa de los fantasmas con respecto al Pacman, y que en base a estas comparaciones tomaran la decisión de hacia dónde moverse:

            else:
                # se actualiza la dirección de movimiento del mismo
                # plan guarda la nueva dirección del fantasma
                # aqui se le agrega inteligencia a los fantasmas
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

Después de realizar los cambios principales al código, se realizaron otros cambios menores que iban más enfocados a la apariencia del juego, así como a añadir información sobre las personas que modificaron el juego:
1. Se modificaron los colores de los fantasmas:
    
            # establece los colores de los fantasmas
            colores = ['red', 'white', 'pink', 'cyan']
            k = 0
-------------------------------------------------------------------------------------------------------
                # dibuja el fantasma
                dot(20, colores[k])
                k = k + 1
                
2. Se añadieron los nombres y matrículas de los integrantes del equipo encargados de modificar el juego:

        info = Turtle(visible=False)
-------------------------------------------------------------------------------------------------------
            info.up()
            info.goto(-140,180)
            info.color('white')
            info.write('José Andrés Villarreal Montemayor  A00829355', font=('Arial', 8, 'normal'))
            info.up()
            info.goto(-140,-200)
            info.color('white')
            info.write('Ricardo Daniel Díaz Granados       A00827266', font=('Arial', 8, 'normal'))

3. Se añadió una leyenda que dice "GAME OVER" y el score obtenido por la persona, la cuál se despliega al momento de perder:

            # recorre la lista de fantasmas para ver si coinciden las
            # posiciones del Pacman y de algún fantasma
            for point, course in ghosts:
                if abs(pacman - point) < 20:
                    writer.goto(-120, 10)
                    writer.write('Game Over', font=('Arial', 30, 'normal'))
                    writer.goto(-90, -20)
                    writer.write(f'Score: {valor}', font=('Arial', 20, 'normal'))
                    return
