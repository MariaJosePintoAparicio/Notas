import os
menu = "1. registrar alumno\n2. registrar notas\n3. buscar estudiante\n4. salir\n:)"
subMenuNotas = "1. parciales\n2.quises\n3. trabajos\n4. regresa al menu principal" 
hasError = True
def menuprincipal () -> int:
    global hasError
    hasError = True
    print (menu)
    while (hasError == True):
      try:
        hasError = False
        return int (input(" :)"))
      except ValueError:
        hasError = True
def menuNotas () -> int : 
   os.system ("cls")
   global hasError
   hasError = True
   print (subMenuNotas)
   while (hasError == True):
      try:
        hasError = False
        return int (input(" :)"))
      except ValueError:
        hasError = True