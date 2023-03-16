# Read a given string, change the character at a given index and then print the modified string.
# We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).
# Let's try to understand this with an example.
# You are given an immutable string, and you want to make changes to it.
# How would you approach this?

# One solution is to convert the string to a list and then change the value.

# Another approach is to slice the string and join it back.

# >>> string = string[:5] + "k" + string[6:]
# >>> print string
# abrackdabra

def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    string = ''.join(l)
    return string

s = input("String: ")
i, c = input("Ingrese una posición y una letra: ").split()
s_new = mutate_string(s, int(i), c)
print(s_new)