# Given an integer, n, perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of  to , print Not Weird
# If n is even and in the inclusive range of  to , print Weird
# If n is even and greater than , print Not Weird

# .strip() saca los espacios en blanco
n = int(input("Ingresar número entero: ").strip()) 

if n % 2 == 0 and n >= 2 and n <= 5:
    print("Not Weird")
elif n >= 6 and n <= 20 or n % 2 != 0:
    print("Weird")
else:
    print("Not Weird")
