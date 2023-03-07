# The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.

n = int(input("Cantidad de estudiantes: "))
student_marks = {}

for _ in range(n):
    name, *line = input("Nombres de los estudiantes:").split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input("Ingrese el nombre para sacar el promedio: ")
    
res = 0
    
# print(student_marks)
# print(query_name)
# print(student_marks[query_name])
    
for i in range(0,len(student_marks[query_name])):
    # print(student_marks[query_name][i])
    res = res + student_marks[query_name][i] 

res = res / len(student_marks[query_name])
    
print(format(res, '.2f')) # Imprimo con 2 decimales siempre.