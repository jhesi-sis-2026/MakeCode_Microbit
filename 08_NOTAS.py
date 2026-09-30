
#PRACTICA 8
#REALIZA UN PROGRAMA QUE MUESTRE UN SMS, SI EL ESTUDIANTE ES APROBADO O REPROBADO, USANDO NUMEROS AL AZAR Y EL BOTON A EN EL LENGUAJE PYTHON

#VARIABLES
MENSAJE = 0
MENSAJE1= "APROBADO" 
MENSAJE1= "REPROBADO"
def on_button_pressed_b():
    global MENSAJE
    MENSAJE = randint (1,100)
    basic.show_number(MENSAJE)
    basic.pause(1000)
    if MENSAJE >=51:

        basic.show_string("APROBADO")
    else:
        basic.show_string("REPROBADO")
        basic.pause(500)
        basic.clear_screen()

input.on_button_pressed(Button.B, on_button_pressed_b)

