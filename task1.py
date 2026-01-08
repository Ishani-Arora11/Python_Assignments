"""
Perform basic mathematical calculations
    1. Take 2 numbers as input
    2. Perform addition , subtraction , multiplication and division
    3. Print all the results on screen

"""

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

#Addition
addition = num1 + num2
print("Sum of",num1,"and",num2,"is",addition)

#Subtraction
if num1 > num2:
    difference = num1 - num2
    print("Difference between",num1,"and",num2,"is",difference)
else:
    difference = num2 - num1
    print("Difference between",num1,"and",num2,"is",difference)

#Multiplication
product = num1 * num2
print("Product of",num1,"and",num2,"is",product)

#Division
if num2 == 0:
    print("Cannot divide by zero.")
else:
    quotient = num1 / num2
    print("The result of division of", num1, "and", num2, "is", quotient)







