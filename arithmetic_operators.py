# The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:

# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.

a = int(input("Ingrese n° a: "))
b = int(input("Ingrese n° b: "))

suma = str(a+b)
diferencia = str(a-b)
producto = str(a*b)
print(suma + "\n" + diferencia + "\n" + producto)