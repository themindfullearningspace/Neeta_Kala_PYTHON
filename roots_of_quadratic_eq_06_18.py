import cmath  #Importing cmath for complex numbers

#Coefficient of the quadratic equation
a = float(input("Enter the coefficient of x^2(a): "))
b = float(input("Enter the coefficient of x(b): "))
c = float(input("Enter the constant term (c): "))


#Calculate the discriminant 
D = b**2 - 4*a*c

#Check the nature of roots and calculate roots accordingly
if D > 0: # Real and distinct roots
  root1 = (-b + D ** 0.5) /(2*a)
  root2 = (-b - D ** 0.5) /(2*a)
  print("Root 1: ", root1)
  print("Root 2: ", root2)
  
elif D == 0: #Real and equal roots
  root = -b / 2*a
  print("Root: ", root)
  
else: #Complex roots
  real_part = -b / 2*a
  imaginary_part = abs(D)**0.5 /(2*a)
  root1 = complex(real_part, imaginary_part)
  root2 = complex(real_part, -imaginary_part)
  print("Root 1: ",root1)
  print("Root 2: ",root2)
  