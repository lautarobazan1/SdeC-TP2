import requests

url = "https://api.worldbank.org/v2/en/country/ARG/indicator/SI.POV.GINI?format=json&date=2011:2020"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    registros = data[1]

    print("Datos extraidos de Argentina")
    valores= []
    for reg in registros:
        anio = reg ['date']
        valor = reg ['value']
        if valor is not None:
            valores.append(valor)
            print (f" Año {anio}: {valor}")

    print ("\nLista de valores obtenida:", valores)

else:
    print("error al consultar la API:",response.status_code)
