# Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of (i,j,k) is not equal to n. 

x = int(input("Ingrese número x: "))
y = int(input("Ingrese número y: "))
z = int(input("Ingrese número z: "))
n = int(input("Ingrese número n: "))

lista = [ [i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k)!=n ]
print(lista)