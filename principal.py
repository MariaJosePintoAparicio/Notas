import os
import menus as menu
import alumnos as st 


alumnos ={}
isActive = True
opMenu=0

while (isActive):
    os.system("cls")
    try:
        opMenu = int(menu.menuprincipal())
    except ValueError:
        print("error en el dato de ingreso")
        os.system("pause")
    else:
        if(opMenu == 1):
            rta = "S"
            while (rta in ["S" , "s"]):
                os.system("cls")
                alumnos.update(st.regAlumnos())
                rta = input ("deceas registrar otro alumno? S(si) o N(no)").upper
            print (alumnos)
            os.system("pause")   
        elif (opMenu == 2): 
            # opNotas = 0
            # isActiveGrades = True
            # while isActiveGrades:
            #     try:
            #         opNotas = int(menu.menuNotas())
            #     except ValueError:
            #         print("error en el dato de ingreso")
            #         os.system("pause")
            #     else:
            #         if (opNotas == 1): 
            #             registroNotas ()
            codigo = input("ingrese el codigo a buscar : ") 
            menu.menuNotas(st.buscar(codigo,alumnos))       
        elif (opMenu == 3):
            codAlumno = input("ingrese el codigo a buscar : ")
            st.buscarAlumno (codAlumno ,alumnos) 
            os.system("pause")
        elif (opMenu == 4):
             isActive = False 