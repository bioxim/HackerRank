# Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

# Mat size must be N x M. ( N is an odd natural number, and M is 3 times N.)
# The design should have 'WELCOME' written in the center.
# The design pattern should only use |, . and - characters.

n = int(input("Insertar: "))
m = 3 * n

for i in range(1, n, 2): 
    print(( str('.|.')*i ).center(m, '-'))
print(str('WELCOME').center(m, '-'))
for i in range(n-2, -1, -2): 
    print(( str('.|.')*i ).center(m, '-'))