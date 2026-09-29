# Grade calculator.

marks = int(input("marks(0-100): "));

if(marks < 0 and marks > 100):
     print("Invalid number");
elif(marks >= 90):
     print("Grade A")
elif(marks >= 80):
     print("Grade B")
elif(marks >= 70):
     print("Grade C")
elif(marks >= 40):
     print("Grade D")
else:
     print("Fail")