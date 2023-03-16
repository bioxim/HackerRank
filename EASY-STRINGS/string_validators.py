# You are given a string .
# Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

import re

s = input("Ingrese cadena a validar: ")

print(bool(re.search("[a-zA-Z0-9]", s)))
print(bool(re.search("[a-zA-Z]", s)))
print(bool(re.search("[0-9]", s)))
print(bool(re.search("[a-z]", s)))
print(bool(re.search("[A-Z]", s)))