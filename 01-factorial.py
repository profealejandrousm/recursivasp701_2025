from os import system
system("cls")



def factorial(num:int)->int:
    #condicion de termino
    if num==1:
        return 1
    #Caso recursivo
    return num*factorial(num-1)
    
   

n=int(input("Ingrese un número:")) 
print(f"El factorial de {n} es {factorial(n)}")