'''

Suma de dígitos: Crea una función recursiva que sume los dígitos de un número (ejemplo: 123 → 1+2+3 = 6).

'''
def sumar_digitos(n:int)->int: #123//10->12//10->1
    if n<10:
        return n
    return n%10+sumar_digitos(n//10)


# print(123%10)
# print(123//10)
# print(12%10)
numero=10101
print("La suma de los digitos es",sumar_digitos(numero))