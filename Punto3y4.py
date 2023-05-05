lista = [2,2,3,3,4,4,5,5,7,8,9,0,10,123,43,2,12,3,21,4,2,2,4,2,1,5,2]
def Repetido(lista, mayor=True):
    cantidad = {}
    for numero in lista:
        if numero in cantidad:
            cantidad[numero] += 1
        else:
            cantidad[numero] = 1
    if mayor:
        cantidadR = max(cantidad.values())
    else:
        cantidadR = min(cantidad.values())
    Repetidoss = [numero for numero, cantidad in cantidad.items() if cantidad == cantidadR]
    if mayor:
        return Repetidoss[0], cantidadR
    else:
        return Repetidoss[-1], cantidadR
numero, cantidad = Repetido(lista)
print(f"El mas repetido: {numero} con {cantidad} veces.")
print(f"El menos repetido: {numero} con {cantidad} veces.")

numero, cantidad = Repetido(lista, mayor=False)