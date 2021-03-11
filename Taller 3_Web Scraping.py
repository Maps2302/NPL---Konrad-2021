#Importar Librerías
import requests
import time
from bs4 import BeautifulSoup
import re

animales = ['perro', 'gato','delfín', 'caballo', 'cangrejo', 'orangután', 'oso', 'pantera', 'ratón', 'Ñu'] #Lista de animales
resultados = open(r'C:\Users\silvafuentes.9\Documents\WS\resultados.txt','w') #Guardar scraping en archivo .txt


for elemento in animales:
	r = requests.get(f'https://es.wikipedia.org/wiki/{elemento}') #Obtener el link para la consulta
	soup = BeautifulSoup(r.content, 'html.parser') #Convertir la info en el html

	encabezado = soup.find('h1').text #Traer los encabezados y dejarlos sin el código html - solo el texto
	resultados.write('\n'+str(encabezado)) #Registra los resultados en el archivo .txt mencionado previamente
	print(encabezado) #Imprime el encabezado
	parrafo = soup.find_all('p') #Extrae los parrafos del texto
	info = parrafo[0].find_all('b') #Extrae las negritas del primer parrago
	resultados.write('\n'+str(info)) #Registra los resultados en el archivo .txt mencionado previamente
	negritas = str(info) #Convierte las negritas de objeto a string
	print(negritas) #Imprime las negritas como cadena de texto
	caracter_especial = r"[áéíóúñ]" #genera el patron RegEx
	cambio = re.sub(caracter_especial, "*", negritas) #Realiza la sustitución de caracteres especiales por *
	print(cambio) #imprime las lineas con la sustitucion 

resultados.close() #cerrar el archivo .txt







