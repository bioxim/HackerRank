# Given an integer, n, print the following values for each integer from 1 to n:

# Decimal
# Octal
# Hexadecimal (capitalized)
# Binary

# Prints

# The four values must be printed on a single line in the order specified above for each from 1  to number. Each value should be space-padded to match the width of the binary value of number and the values should be separated by a single space.

# Explanation

# We can solve this challenge using the .format tool.
# "{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i,width = width)
# Other approach: We can solve this using the rjust function to align the rows.
# The oct, hex and bin can be used to convert the integer into octal, hexadecimal and binary format, respectively.

def print_formatted(number):
    # El ancho del number es la longitud del número en binario - 2
    width = len(bin(number)) - 2
    for i in range(1,number+1):
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i,width = width))

n = int(input())
print_formatted(n)