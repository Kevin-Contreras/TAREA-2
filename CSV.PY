import csv
def Csv (archivo):
  n=0
  print("-------------------- ESTRUCTURA DE DATOS: CSV-----------------------------") 
  with open(archivo) as file:
    archivoCsv = csv.DictReader(file)
    for dato in archivoCsv:
      n+=1
      print("---------- DATO " + str(n)+" ---------") 
      print(dato.get("nombre"))
      print(dato.get("carnet"))
      print(dato.get("carrera"))
  print("-------------------- ESTRUCTURA DE DATOS: CSV-----------------------------")