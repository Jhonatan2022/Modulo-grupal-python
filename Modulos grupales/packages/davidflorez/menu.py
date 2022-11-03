import hashlib
from deividbautista.escrita import encriptar
from kristell.lista import agregar
from juanmoreno.polindromo import polindromo
def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')

def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a

def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()

def menu_principal():
    opciones = {
        '1': ('Ordenar nombres', agregar),
        '2': ('Encriptar texto', encriptar),
        '3': ('Contador ', escribir ),
        '4': ('definir si una palabra es un palidromo ', polindromo ),
        '5': ('Salir', salir)
    }

    generar_menu(opciones, '5')

def escribir ():

    print ('Este programa contara cuantos digitos numericos has puestro en los strings, escribe fin para terminar y + para hacer un conteo de los digitos')
    lineas=0
    digitos="0123456789"
    cantidadDigitos=0
    cadena=input("Cadena: ")
    while cadena!="fin":
        for caracter in cadena:
            if caracter in digitos:
                cantidadDigitos+=1
        if cadena=="+":
            lineas+=1
            print("Aparecen ", cantidadDigitos, " dígitos en la línea")
            cantidadDigitos=0
        cadena=input("Cadena: ")
    print("Se leyeron ",lineas," líneas completas")
    
def salir():
    print('Saliendo')

if __name__ == '__main__':
    menu_principal()