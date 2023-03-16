# >>> a = "this is a string"
# >>> a = a.split(" ") # a is converted to a list of strings. 
# >>> print a
# ['this', 'is', 'a', 'string']

# >>> a = "-".join(a)
# >>> print a
# this-is-a-string 


def split_and_join(line):
    # write your code here
    line = line.split(" ")
    line = "-".join(line)
    print(line)

    
line = input("Ingrese una cadena: ")
result = split_and_join(line)