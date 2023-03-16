# función de la serie fibonacci entre un número y otro número dado:

def fibonacci(num):
    a,b = 0, 1
    lista = [0]
    for i in range(num):
        if b > num: return lista
        else: 
            lista.append(b)
            a,b = b, a+b
    return lista

print(fibonacci(34))