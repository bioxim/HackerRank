# You are given a string S and width w.
# Your task is to wrap the string into a paragraph of width w.

import textwrap

def wrap(string, max_width):
    return "\n".join(textwrap.wrap(string, max_width))

if __name__ == '__main__':
    string, max_width = input("Escriba una cadena de texto:"), int(input("Cantidad de caracteres para el salto de línea: "))
    result = wrap(string, max_width)
    print(result)