# Classify a triangle by its sides.
a,b,c = int(input("Sides: ").split())

if a + b <= c or a + c <= b or b + c <= a:
     print("Invalid Triangle")
elif a == b == c:
     print("Equilateral")
elif  a == b or b == c or a == c:
     print("Isosceles")
else:
     print("Scalene") 