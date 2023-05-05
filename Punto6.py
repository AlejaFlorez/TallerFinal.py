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
        
        
temperaturas = [(32, "C", "F"), (32, "C", "K"), (32, "F", "C"), 
                (32, "F", "K"), (32, "K", "C"), (32, "K", "F")]
for temperatura in temperaturas:
    valor, inicial, final = temperatura
    print(f"{valor} grados {inicial} equivale a {convertir_temp(valor, inicial, final)} grados {final}")
    
    
    
# C = Celsius
# F = Fahrenheit
# = Kelvin