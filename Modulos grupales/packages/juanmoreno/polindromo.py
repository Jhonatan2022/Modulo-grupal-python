
def polindromo():  
    palindromo=input("Ingresa la palabra: ")
    if palindromo==palindromo[::-1]:
        print("La palabra es palindromo")
    else:
        print("La palabra no es palindromo")