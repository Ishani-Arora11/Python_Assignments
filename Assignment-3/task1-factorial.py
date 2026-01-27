#Calculate the factorial of a number


def fact(number):
    """
    using recursion to calculate the factorial of a given number
    function will keep calling itself until a base condition is met
    :return: int
    """
    if number == 1:
        return 1
    return number * fact(number - 1)

num = int(input("Enter a number: "))
factorial = fact(num)
print(f"Factorial of {num} is {factorial}")