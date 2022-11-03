from importlib.resources import path
from deividbautista.escrita import encriptar
from davidflorez.menu import menu_principal
from juanmoreno.polindromo import polindromo
from kristell.lista import agregar
import hashlib


listaNombres=[]
agregar ()

palindromo=input("Ingresa la palabra: ")
polindromo(palindromo)

contraseña= str(input("digite su contraseña :"))
encriptar(contraseña)

menu_principal()