from os import system
system("cls")

def secuencia_desc(n:int)->list:
    if n==0:
        return []
    return [n]+secuencia_desc(n-1)

def secuencia_asc(n:int)->list:
    if n==0:
        return []
    return secuencia_asc(n-1)+[n]

n=5

print(f"La secuencia descendente {n} es {secuencia_desc(n)}")

n=5
print(f"La secuencia ascendente {n} es {secuencia_asc(n)}")