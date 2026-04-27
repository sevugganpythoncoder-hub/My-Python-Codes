# inputs and libraries used
import math
a = int(input("Enter value of a:"))
b = int(input("Enter value of b:"))
c = int(input("Enter value of c:"))
print("\nForming calculations...")
# calculations
try:
    Formula1 = (-b + math.sqrt(b**2 - 4*a*c))/ (2*a)
    Formula2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
except ValueError:
    print("You have imaginary roots!")
except ZeroDivisionError:
    print("This is not a Quadratic equation")
# results
D = (b**2 - 4*a*c)
if D > 0:
    print("You got 2 distinct real roots")
    print(f"Root 1 of Eq : {Formula1}")
    print(f"Root 2 of Eq: {Formula2}")
elif D == 0:
    print("You got one real root")
    print(f"Root 1 of Eq : {Formula1}")
    print(f"Root 2 of Eq: {Formula2}")
else:
    pass
