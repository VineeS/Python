import cmath # its used for complex number
a = float(input("Enter the value of a :"))
b = float(input("Enter the value of b : "))
c = float(input("Enter the value of c :"))
d = pow(b, 2) - (4*a*c)
print(cmath.sqrt(d))
sol1 = (-b - cmath.sqrt(d))/(2*a)
sol2 = (-b + cmath.sqrt(d))/(2*a)
print(sol1)
print(sol2)
print("Quadratic equation {0} and {1}   ".format(sol1, sol2))
