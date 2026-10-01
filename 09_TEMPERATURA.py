
#PRACTICA 9
#REALIZA UN PROGRAMA QUE SIMULE UN MEDIOR DE TEMPERERATURA USANDO NUMEROS AL AZAR Y EL BOTON A, EN EL LENGUAJE PYTHON
#SI TEMPERATURA ES <= 15- MOSTRAR UN SMS DE "FRIO", SINO UN SMS DE "CALOR"

#VARIABLES
TEMPERATURA= 0
MENSAJE1= "FRIO"
MENSAJE1= "CALOR"
def on_button_pressed_a():
    global TEMPERATURA
    TEMPERATURA = randint (1,40)
    basic.show_number(TEMPERATURA)
    basic.pause(1000)
    if TEMPERATURA <=15:
        basic.show_string("FRIO")
    else:
        basic.show_string("CALOR")
        basic.pause(500)
        basic.clear_screen()

input.on_button_pressed(Button.A, on_button_pressed_a)
