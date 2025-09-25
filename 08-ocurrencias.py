'''
Contar ocurrencias de un carácter en un string: 
Una función que recorra la cadena de manera recursiva y 
cuente cuántas veces aparece un carácter

'''

def contar_ocurrencia(palabra:str,letra:str)->int:
    if palabra=="":
        return 0
    
    if palabra[0]==letra:
        return 1+contar_ocurrencia(palabra[1:],letra)
    else:
        return contar_ocurrencia(palabra[1:],letra)  
    
 
 
 
palabra="marca"
letra="a"
print(contar_ocurrencia(palabra,letra))
