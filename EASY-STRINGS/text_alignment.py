# In Python, a string of text can be aligned left, right and center.

# Task

# You are given a partial code that is used for generating the HackerRank Logo of variable thickness.
# Your task is to replace the blank (______) with rjust, ljust or center.

# Ingreso el grosor del logo
n = int(input())
# Caracter por el que quiero hacerlo
c = 'H'

# Cono
for i in range(n):
    print((c*i).rjust(n-1)+c+(c*i).ljust(n-1))
    
# Pilares
for i in range(n+1):
    print((c*n).center(n*2)+(c*n).center(n*6))

# El medio
for i in range((n+1)//2):
    print((c*n*5).center(n*6))    

# Pilares de abajo
for i in range(n+1):
    print((c*n).center(n*2)+(c*n).center(n*6))    

# Cono de abajo
for i in range(n):
    print(((c*(n-i-1)).rjust(n)+c+(c*(n-i-1)).ljust(n)).rjust(n*6))

