#PRACTICA 10
#REALIZA UN PROGRAMA QUE SIMULE UN MEDIOR DE VELOCIDAD USANDO NUMEROS AL AZAR Y EL BOTON B, EN EL LENGUAJE PYTHON
#SI VEWLOCIDAD ES <= 15- MOSTRAR UN SMS DE "RAPIDO", SINO UN SMS DE "LENTO"

#VARIABLES
VELOCIDAD= 0
MENSAJE1= "RAPIDO"
MENSAJE1= "LENTO"
def on_button_pressed_b():
    global VELOCIDAD
    VELOCIDAD = randint (1,100)
    basic.show_number(VELOCIDAD)
    basic.pause(1000)
    if VELOCIDAD >=70:
        basic.show_string("RAPIDO")
    else:
        basic.show_string("LENTO")
        basic.pause(500)
        basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)
