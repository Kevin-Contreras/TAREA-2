import xml.etree.ElementTree as dato
def Xml (datos):
  n=0
  print("--------------------ESTRUCTURA DE DATOS: XML-----------------------------")

  archivoXml= dato.parse(datos)
  archivos = archivoXml.getiterator()
  for archivo in archivos:
    print(archivo.text)
  print("--------------------ESTRUCTURA DE DATOS: XML-----------------------------")
   
  
