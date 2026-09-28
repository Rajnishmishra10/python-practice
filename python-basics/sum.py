# Take two numbers as input and print their sum, 
# difference, product, and division.

num1 = float(input("First number: "));
num2 = float(input("Second number: "));

print(f"Sum: {num1 + num2}");
print(f"Difference: {num1 - num2}");
print(f"Product: {num1 * num2}"); 

if num2 != 0:
    print(f"Division: {num1 / num2}")
else:
    print("Cannot divide by zero")