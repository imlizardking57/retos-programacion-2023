# Author: imlizardking57
# Date: 20/9/23
# * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
# * Podrás configurar generar contraseñas con los siguientes parámetros:
# * - Longitud: Entre 8 y 16.
# * - Con o sin letras mayúsculas.
# * - Con o sin números.
# * - Con o sin símbolos.
# * (Pudiendo combinar todos estos parámetros entre ellos)

import sys, getopt
def showUsage():
   print ("Random password generator.")
   print ("usage: imlizardking57.py [options]")
   print (" options:")
   print ("-l, --length [number] password length between 8-15")
   print ("-u, --upper Use Uppercase letters")
   print ("-n, --numbers Use numbers")
   print ("-s, --symbols Use symbols")
   
def main(argv):
   passwordLength = 8
   bUseUpper = False
   bUseNumbers = False
   bUseSymbols = False

   try:
      opts, args = getopt.getopt(argv,"hl:uns",["length","upper","numbers","symbols"])
   except:
      showUsage()
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         showUsage()
         sys.exit()
      elif opt in ("-l", "--length"):
         passwordLength = arg
      elif opt in ("-u", "--upper"):
         bUseUpper = True
      elif opt in ("-n", "--numbers"):
         bUseNumbers = True
      elif opt in ("-s", "--symbols"):
         bUseSymbols = True
   print ("Generating password with the following attributes")
   print ("Password length: " + str(passwordLength))
   print ("Use Uppercase letters?: " + str(bUseUpper))
   print ("Use numbers?: " + str(bUseNumbers))
   print ("Use symbols?: " + str(bUseSymbols))
   
if __name__ == "__main__":
   main(sys.argv[1:])
