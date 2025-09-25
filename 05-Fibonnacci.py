

def fibonacci(n:int)->int: #1,1,2,3,5,8,13,21,34,55,89
    if n==1:
        return n
    
    return fibonacci(n-1)+fibonacci(n-2) 
    
    
    
enesimo=7
print(f"Fibo n {fibonacci(enesimo)}")