from os import strerror

cuento = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
archivo = input("Ingrese la direcciion del archivo: ")

try:
    archivoo = open(archivo, "rt")

    for line in archivoo:
        for char in line:
            if char.isalpha():
                cuento[char.lower()] += 1
    archivoo.close()

    for char in cuento.keys():
        resultado= cuento[char]
        if resultado> 0:
            print(char, '👉', resultado)

except IOError as e:
    print("No se puede leer el documento: ", strerror(e.errno))
