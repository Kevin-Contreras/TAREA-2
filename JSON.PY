import json
def Json (archivo):
  n=0
  print("--------------------ESTRUCTURA DE DATOS: JSON-----------------------------")
  with open(archivo) as archivojson:
    archivoJson = json.load(archivojson)
    for linea in archivoJson:
      n+=1
      print("---------- DATO " + str(n)+" ---------") 
      print(linea.get("nombre"))
      print(linea.get("carnet"))
      print(linea.get("carrera"))
      print(linea.get("edad"))
    
  print("--------------------ESTRUCTURA DE DATOS: JSON-----------------------------")
