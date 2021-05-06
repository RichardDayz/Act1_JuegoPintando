# Bitácora Semana Tec-Herramientas computacionales: el arte de la programación
## Actividad 1-Paint-Mayo 4, 2021
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

## Actividad 2-Snake
