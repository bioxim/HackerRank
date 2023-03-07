# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.

n = int(input("Ingrese cantidad de participantes: "))
arr = map(int, input("Ingresar clasificaciones: ").split())

lista = set(arr)
res = list(lista)
res.sort()
print(res[-2])