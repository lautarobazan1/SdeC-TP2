import requests

def obtener_indice_gini():
    # URL provista en el enunciado del TP
    url = "https://api.worldbank.org/v2/en/country/ARG/indicator/SI.POV.GINI?format=json&date=2011:2020&per_page=32500&page=1"
    
    try:
        response = requests.get(url)
        
        # Verificar que la respuesta HTTP sea exitosa (código 200)
        if response.status_code == 200:
            datos = response.json()
            
            # La API del Banco Mundial devuelve una lista donde el segundo elemento [1] tiene la lista de registros
            registros = datos[1]
            
            # Buscamos el primer registro que contenga un valor no nulo
            for registro in registros:
                if registro['value'] is not None:
                    valor_gini = float(registro['value'])
                    anio = registro['date']
                    print(f"[Python] Datos obtenidos correctamente de la API REST.")
                    print(f"[Python] País: Argentina | Año: {anio} | Índice GINI: {valor_gini}")
                    return valor_gini
                    
            print("[Python] No se encontraron valores válidos de GINI.")
            return None
        else:
            print(f"[Python] Error al consultar la API: Status {response.status_code}")
            return None
            
    except Exception as e:
        print(f"[Python] Error en la conexión: {e}")
        return None

if __name__ == "__main__":
    print("--- INICIANDO CAPA SUPERIOR (PYTHON) ---")
    gini = obtener_indice_gini()
