# Ejemplo de iteración de dos listas al mismo tiempo con zip()

# animal = ["Perro", "Gato"]
# sonido = ["Ladra", "Maulla"]

# for animal, sonido in zip(animal,sonido):
#     print(f"El {animal} {sonido}")

# animales = ["Perro", "Gato", "Loro", "Iguana"]

# for i in enumerate(animales):
#     print(i)
    
# for animal in animales:
#     if animal == "Gato":
#         continue
#     print(animal)
    
#  El continue omite al animal gato

# numeros = [1,2,3]

# numeros_al_cubo = [x**3 for x in numeros]

# print(numeros_al_cubo)

#######################################################################################################

# Exercise
# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

s = input("Ingresar una frase: ")

def swap_case(s):
    # frase = []
    # for x in range(len(s)):
    #     if s[x].isupper() == True:
    #         frase.append(s[x].lower())
    #     else:
    #         frase.append(s[x].upper()) 
    # s = ''.join(str(x) for x in frase)
    # return s
    
    return s.swapcase()



result = swap_case(s)
print(result)