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
