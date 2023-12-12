import locale
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
driver = webdriver.Chrome()
url = "https://datosmacro.expansion.com/pib/ecuador"
driver.get(url)
contenido = driver.page_source
soup = BeautifulSoup(contenido, 'html.parser')

tabla_pib = soup.find('table')
filas = tabla_pib.find_all('tr')
fechas = []
pib_anual = []
var_pib_percent = []
for fila in filas[1:]:
    columnas = fila.find_all('td')
    fechas.append(columnas[0].text.strip())

    # Modificar el formato del PIB Anual
    pib_valor = columnas[2].text.strip().replace('M$', '').replace('.', '')
    pib_anual.append(pib_valor)

    var_pib_percent.append(columnas[3].text.strip())


print("Fechas:")
for fecha in fechas:
    print(fecha)

print("\nPIB Anual:")
for pib in pib_anual:
    print(pib)

print("\nVariación del PIB %:")
for var_pib in var_pib_percent:
    print(var_pib)

# Crear un DataFrame de pandas
df = pd.DataFrame({
    'Fecha': fechas,
    'PIB Anual': pib_anual,
    'Var. PIB %': var_pib_percent
})

# Guardar el DataFrame en un archivo CSV
df.to_csv('PIB anual Ecuador.csv', index=False)
print("Archivo CSV PIB anual Ecuador generado exitosamente.")

# Cierra el navegador
driver.quit()


#integrantes
#Carrera Franco Camille Dallyana
#Jiménez Vera Nagely Jamilex
#Alvarado Pizarro Ashley Anabel
#José Luis García Fonseca


