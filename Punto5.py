def convertir_temp(valor, inicial, final):
    if inicial == "C":
        if final == "F":
            return (valor * 9/5) + 32
        elif final == "K":
            return valor + 273.15
    elif inicial == "F":
        if final == "C":
            return (valor - 32) * 5/9
        elif final == "K":
            return (valor - 32) * 5/9 + 273.15
    elif inicial == "K":
        if final == "C":
            return valor - 273.15
        elif final == "F":
            return (valor - 273.15) * 9/5 + 32
    else:
        print("La unidad de medida ingresada no es correcta")
        
        
        
# C = Celsius
# F = Fahrenheit
# = Kelvin
        