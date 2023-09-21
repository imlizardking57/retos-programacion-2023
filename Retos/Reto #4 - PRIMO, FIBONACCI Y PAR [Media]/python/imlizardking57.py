# Author: imlizarking57
# Date: 20/9/23
# * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
# * Ejemplos:
# * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
# * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
################################################################################################
def isEvenNumber(number):
    # Wikipedia definition: https://es.wikipedia.org/wiki/N%C3%BAmeros_pares_e_impares
    # Base case: Zero is an even number
    if number == 0 or number % 2 == 0:
        return True
    else:
        return False

def isPrimeNumber(number):
    absNumber = abs(number)
    if (absNumber == 0 or absNumber == 1):
        return False
    for i in range(2,absNumber):
        if (absNumber % i) == 0:
            return False
    return True

def fibonacci(number):
    if not type(number) is int and number < 0:
        raise TypeError("fibonacci: Only natural numbers are allowed")
    # Fibonnaci(n) = Fibonnaci(n-1) + Fibonnaci(n-2)
    # Base cases: n=0 or n=1
    if (number == 0):
        return 0
    elif (number == 1):
        return 1
    else: # Recursive case
        return fibonacci(number - 1) + fibonacci(number - 2)

def isFibonacci(number):
    if not type(number) is int and number < 0:
        raise TypeError("isFibonacci: Only natural numbers are allowed")
    n = 0
    while (auxFib := fibonacci(n)) < number:
        print("Calculating...")
        n = n + 1
    return (auxFib == number)

################################################################################################    
import sys

print("Please enter your natural number:")
number = input()
number = int(number)
if not type(number) is int and number < 0:
    print("Only natural numbers are allowed")
    sys.exit(2)
bIsEven         = isEvenNumber(number)
bIsPrimeNumber  = isPrimeNumber(number)
bIsFibonacci    = isFibonacci(number)

msg = "Tu número " + str(number)
if bIsEven:
    msg = msg + " es par,"
else:
    msg = msg + " no es par,"
if bIsPrimeNumber:
    msg = msg + " es primo,"
else:
    msg = msg + " no es primo,"
if bIsFibonacci:
    msg = msg + " y es fibonacci"
else:
    msg = msg + " y no es fibonacci"
print(msg)