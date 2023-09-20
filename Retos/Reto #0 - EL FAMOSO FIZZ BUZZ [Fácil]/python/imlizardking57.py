# Author: Imlizardking57
# Date: 19/9/23
# Function that determines if a number is multiple of other number
#
# * Escribe un programa que muestre por consola (con un print) los
# * números de 1 a 100 (ambos incluidos y con un salto de línea entre
# * cada impresión), sustituyendo los siguientes:
# * - Múltiplos de 3 por la palabra "fizz".
# * - Múltiplos de 5 por la palabra "buzz".
# * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

def isMultiple(number, multiple):
    if number % multiple == 0:
        return True
    else:
        return False
# Declare our number range
numbersRange = range(1,101)

# Iterate over the numbers
for n in numbersRange:
    if (isMultiple(n,3) and isMultiple(n,5)):
        print ("fizzbuzz")
    elif (isMultiple(n,3)):
        print ("fizz")
    elif (isMultiple(n,5)):
        print ("buzz")
    else:
        print(n)