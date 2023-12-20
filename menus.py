import os
import notas as nota
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
def menuNotas(alumnos : dict):
    os.system("cls")
    header = """
    *
    MENU REGISTRO NOTAS
    *
    """
    isActiveMenu = True
    while (isActiveMenu):
        os.system("cls")
        print(header)
        try: 
            print(subMenuNotas)
            opMenu = int(input(":)"))
        except ValueError:
            print("Opcion invalida....Recuerde que son enteros")
            os.system("pause")
        else:
            if (opMenu == 1):
                nota.addGrades(alumnos,"parciales")
            elif (opMenu == 2):
                nota.addGrades(alumnos,"quices")
            elif (opMenu == 3):
                nota.addGrades(alumnos,"trabajos")
            elif (opMenu == 4):
                isActiveMenu = False
            else:
                print("La opcion ingresada es invalida...")
                os.system("pause")