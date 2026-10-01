
#PRACTICA 11
#REALIZA UN PROGRAMA QUE SIMULE UN CONTADOR DE NUMEROS DEL 1-5 
#USANDO FOR Y EL BOTON A, EN EL LENGUAJE PYTHON

def on_button_pressed_a():
    for i in range (1,5 +1):
        basic.show_number(i)
        basic.pause(300)
    # al terminar el bucle

    basic.show_icon(IconNames.YES)
    basic.show_string("FINAL")
    basic.pause (500)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)
