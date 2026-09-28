# Find the largest of three numbers.

a, b, c = map(int, input("Enter 3 numbers: ").split())

if(a >= b and a >= c):
     print(a, "is largest")
elif(b >= c):
     print(b, "is largest")
else:
     print(c, "is largest")
     
# Shortcut: print(max(a, b, c))