def invertir_cadena(cadena):
    if len(cadena) == 0:
        return ""
    else:
        return cadena[-1] + invertir_cadena(cadena[:-1])
    
cadena = "Hola mundo!"
resultado = invertir_cadena(cadena)
print(resultado)