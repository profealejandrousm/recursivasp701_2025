'''
Invertir una cadena: Haz una función recursiva que invierta un string (ejemplo: 'hola' → 'aloh').
'''
def invertir(palabra:str)->str: #gato
    if palabra=="":
        return ""
    
    return invertir(palabra[1:])+palabra[0]
    
    
palabra="gato"
print(f"{palabra} al revés es {invertir(palabra)}")
