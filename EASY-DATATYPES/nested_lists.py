# Given the names and grades for each student in a class of n students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

records, calif, res = [], [], []

for _ in range(int(input())):
    name = input()
    score = float(input())
        
    calif.append(score)
        
    lista = [name, score]
    records.append(lista)

calificaciones = list(set(calif))
calificaciones.sort()
# print(calificaciones[1])
# print(records)
for i in range(0,len(records)):
    # print(records[i][1])
    if calificaciones[1] == records[i][1]:
        res.append(records[i])
res.sort()

for j in range(0,len(res)):
    print(res[j][0])