# The provided code stub reads two integers, a and b, from STDIN.

# Add logic to print two lines. The first line should contain the result of integer division, a // b. The second line should contain the result of float division, a / b.

# No rounding or formatting is necessary.

a = int(input("Ingrese n° a: "))
b = int(input("Ingrese n° b: "))

div_entera = str(a // b)
div_decimal = str(a / b)

print(div_entera + "\n" + div_decimal)