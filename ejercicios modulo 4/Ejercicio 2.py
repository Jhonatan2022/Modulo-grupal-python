from os import strerror

contando = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
archivo = input("Digite la direccion del archivo: ")
try:
    documento = open(archivo, "rt")
    for line in documento:
        for char in line:
            if char.isalpha():
                contando[char.lower()] += 1
    documento.close()

    documento = open(archivo + '.hist', 'wt')
    for char in sorted(contando.keys(), key=lambda x: contando[x], reverse=True):
        resultado= contando[char]
        if resultado> 0:
            documento.write(char + '  --->  ' + str(resultado)+ (resultado*' +')+ '\n')
    documento.close()

except IOError as e:
    print("No se puede abrir: ", strerror(e.errno))
