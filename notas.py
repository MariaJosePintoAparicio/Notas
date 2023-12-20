import os 
def addGrades(alumno :dict,categoria :str):
    dataNota = alumno.get("notas")
    evaluacion = dataNota.get(categoria)
    nota = float(input(f"ingrese a nota de {alumno.get("nombre").upper()}  :"))
    evaluacion.append(nota)