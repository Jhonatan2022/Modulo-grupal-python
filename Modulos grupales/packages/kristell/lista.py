listaNombres=[]

def agregar ():
    nombreUsuario=input("Por favor, ingrese un nombre: ")
    listaNombres.append(nombreUsuario)
    print("¿Quiere añadir otro nombre?")
    añadir= input("Use (S) para si y (N) para no: ")

    while añadir == "s" or añadir == "S":
        nombreUsuario=input("Por favor, ingrese un nombre: ")
        listaNombres.append(nombreUsuario)
        print("¿Quiere añadir otro nombre?")
        añadir= input("Use (S) para si y (N) para no: ")

    listaNombres.sort()

    print(f"Los nombres introducidos son {listaNombres}")
    input("Por favor, presione una tecla para salir.")