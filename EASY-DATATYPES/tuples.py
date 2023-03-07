# Given an integer, , and  space-separated integers as input, create a tuple, , of those  integers. Then compute and print the result of hash().
# Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

n = int(input("Entero 1: "))
integer_list = map(int, input("Entero 2: ").split())
t = tuple(integer_list)

print(hash(t))