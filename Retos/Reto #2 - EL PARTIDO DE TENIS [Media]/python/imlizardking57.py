# Author: Imlizardking57
# Date: 19/9/23
# * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
# * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
# * gane cada punto del juego.
# * 
# * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
# * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
# *   15 - Love
# *   30 - Love
# *   30 - 15
# *   30 - 30
# *   40 - 30
# *   Deuce
# *   Ventaja P1
# *   Ha ganado el P1
# * - Si quieres, puedes controlar errores en la entrada de datos.   
# * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.
from enum import Enum
 
class TennisGameState(Enum):
    DEUCE_LOVE      = 1
    FIFTEEN_LOVE    = 2
    LOVE_FIFTEEN    = 3
    DEUCE_FIFTEEN   = 4
    THIRTY_FIFTEEN  = 5
    THIRTY_LOVE     = 6
    FIFTEEN_THIRTY  = 7
    DEUCE_THIRTY    = 8
    FOURTY_LOVE     = 9
    FOURTY_FIFTEEN  = 10
    FOURTY_THIRTY   = 11
    DEUCE           = 12
    LOVE_FOURTY     = 13
    FIFTEEN_FOURTY  = 14
    THIRTY_FOURTY   = 15
    ADVANTAGE_P1    = 16
    ADVANTAGE_P2    = 17
    P1_WINS         = 18
    P2_WINS         = 19
    LOVE_THIRTY     = 20
    
def changeGameState(currentState,player):
    if (currentState == TennisGameState.DEUCE_LOVE):
        if (player == "P1"):
            return TennisGameState.FIFTEEN_LOVE
        else:
            return TennisGameState.LOVE_FIFTEEN
    elif (currentState == TennisGameState.FIFTEEN_LOVE):
        if (player == "P1"):
            return TennisGameState.THIRTY_LOVE
        else:
            return TennisGameState.DEUCE_FIFTEEN
    elif (currentState == TennisGameState.LOVE_FIFTEEN):
        if (player == "P1"):
            return TennisGameState.DEUCE_FIFTEEN
        else:
            return TennisGameState.LOVE_THIRTY
    elif (currentState == TennisGameState.LOVE_FIFTEEN):
        if (player == "P1"):
            return TennisGameState.DEUCE_FIFTEEN
        else:
            return TennisGameState.LOVE_THIRTY

tennisGameState = TennisGameState.DEUCE_LOVE
inputCommand = ""
while True:
    print ("Please enter who won the point: ", end="")
    inputCommand = input()
    if inputCommand.upper() == "END":
        print("Exiting the program as per user request")
        break
    if inputCommand.upper() != "P1" and inputCommand.upper() != "P2":
        print("Please enter either P1 or P2")
    else:
        tennisGameState = changeGameState(tennisGameState,inputCommand)
        print(tennisGameState)
    

