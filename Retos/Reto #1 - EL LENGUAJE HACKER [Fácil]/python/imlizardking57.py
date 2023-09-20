# Author: Imlizardking57
# Date: 19/9/23
# * Escribe un programa que reciba un texto y transforme lenguaje natural a
# * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
# *  se caracteriza por sustituir caracteres alfanuméricos.
# * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
# *   con el alfabeto y los números en "leet".
# *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
# Let's define our tranformation matrix with a Python dictionary

leet_matrix = {
    "A" : "4",
    "B" : "I3",
    "C" : "[",
    "D" : ")",
    "E" : "3",
    "F" : "|=",
    "G" : "&",
    "H" : "#",
    "I" : "1",
    "J" : ",_|",
    "K" : ">|",
    "L" : "1",
    "M" : "/\\/\\",
    "N" : "^/",
    "Ñ" : "^^/",
    "O" : "0",
    "P" : "|*",
    "Q" : "(_,)",
    "R" : "I2",
    "S" : "5",
    "T" : "7",
    "U" : "(_)",
    "V" : "\\/",
    "W" : "\\/\\/",
    "X" : "><",
    "Y" : "J",
    "Z" : "2"
}

def getLeetChar(char):
    # If the character is present in our dictionary just return it
    if char in leet_matrix:
        return leet_matrix[char]
    else: # If the character is not transformable, like "!,$"·$))!=$)= just return it
        return char
    
# Function that thansforms a natural language sentence into leet
def transform2leet(sentence):
    upper_sentence = sentence.upper()
    leet_sentence = ''
    for i in range(0, len(upper_sentence)):            
        leet_sentence = leet_sentence + getLeetChar(upper_sentence[i])   
    return leet_sentence

# Read input from the user
print("Please enter your sentence in natural language, followed by 'Enter'")
natural_sentence = input()
leet_sentence = transform2leet(natural_sentence)
print (leet_sentence)