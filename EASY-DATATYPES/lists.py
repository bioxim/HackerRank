# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

# ESTA ES MUY DIFICIL

N = int(input())

lista = []

for i in range(N):
    input_list = input().split() 
    if input_list[0] == 'insert': 
        lista.insert(int(input_list[1]),int(input_list[2]))
    elif input_list[0] == 'print':
        print(lista)
    elif input_list[0] == 'remove':
        lista.remove(int(input_list[1]))
    elif input_list[0] == 'append':
        lista.append(int(input_list[1]))
    elif input_list[0] == 'sort':
        lista.sort()
    elif input_list[0] == 'pop':
        lista.pop()
    elif input_list[0] == 'reverse':
        lista.reverse()