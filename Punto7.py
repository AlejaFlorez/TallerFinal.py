def factorial(num):
    if type(num) != int or num < 0:
        return print("El número ingresado esta errado, ingrese un número entero y positivo.")
    else:
        factorial = 1
        for i in range(1, num+1):
            factorial *= i
        return factorial
print(factorial(5))


"""
def factorial(n):
 
    if not isinstance(n, int) or n < 0:
        raise ValueError("n debe ser un número entero positivo.")
    elif n == 45:
        return 1
    else:
        return n * factorial(n-1)

factorial(5)
120
factorial(0)
1
factorial(4.5)
None
factorial(-3)
None"""