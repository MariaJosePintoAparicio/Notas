import os
def regAlumnos() -> dict:
    codigo = input("ingrese el codigo del estudiante:")
    nombre = input("ingrese el nombre del estudiante:")
    edad = input("ingrese la edad del estudiante:")
    alumno = { 
        "codigo" : codigo,
        "nombre" : nombre,
        "edad" : edad,
        "notas" :{
               "parciales" :[],
               "quices" : [],
               "trabajos" : []
        }
    }
    return {codigo : alumno}
def buscarAlumno(codAlumno : str , alumnos:dict):
    data = alumnos.get(codAlumno, -1)
    if (type (data) == dict):
        for llave,valor in data.items(): 
         print(f"{llave} : {valor}")
        os.system 
    else:
      print ("no se encontro el estuduante con el codigo {codAlumno}")
      os.system("pause")
def buscar(codAlumno : str, alumnos : dict )->dict:
   data = alumnos.get(codAlumno,-1)
   if(type(data)==dict):
      return data
   else:
      print (f"nop se encontro el estudiantecon el cofigo {codAlumno} ") 
      os.system("pause")    