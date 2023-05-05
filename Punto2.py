numero = int(input("Ingrese un numero: "))
def num(numero):
    if(numero % 2 == 0):
        return False
    else:
        return True
print(num(numero))


lista = [5,6,7,3,4,14,2,3,5,3,8,18,10,20]
def list(listNumeros):
    listNueva = []
    for a in listNumeros:
        if(num(a)):
            listNueva.append(a)
    return listNueva
print("Esta lista solo contiene números primos: ", list(lista))