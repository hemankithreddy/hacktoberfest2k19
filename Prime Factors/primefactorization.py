import sympy
n=int(input('Enter a number:'))
for i in range(1,n):
    print(sympy.isprime(i),end=" ")
