# In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

# note: String letters are case-sensitive.

# This can be solved by using a regex.

import re

def count_substring(string, sub_string):
    match = re.findall('(?='+sub_string+')',string)
    return len(match)    

if __name__ == '__main__':
    string = input("Ingrese cadena: ").strip()
    sub_string = input("Ingrese subcadena: ").strip()
    
    count = count_substring(string, sub_string)
    print(count)