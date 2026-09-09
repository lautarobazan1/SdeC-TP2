import requests
import ctypes
import os

def obtener_indice_gini():
    url = "https://api.worldbank.org/v2/en/country/ARG/indicator/SI.POV.GINI?format=json&date=2011:2020&per_page=32500&page=1"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            datos = response.json()
            registros = datos[1]
            for registro in registros:
                if registro['value'] is not None:
                    valor_gini = float(registro['value'])
                    anio = registro['date']
                    print(f"[Python] Datos API -> Año: {anio} | GINI: {valor_gini}")
                    return valor_gini
            return None
        else:
            return None
    except Exception as e:
        print(f"[Python] Error: {e}")
        return None

if __name__ == "__main__":
    print("--- INICIANDO FLUJO PYTHON -> C ---")
    
    gini_float = obtener_indice_gini()
    
    if gini_float is not None:
        ruta_so = os.path.abspath("src/libpuente.so")
        lib = ctypes.CDLL(ruta_so)
        
        lib.ejecutar_calculo.argtypes = [ctypes.c_float]
        lib.ejecutar_calculo.restype = ctypes.c_int
        
        resultado_final = lib.ejecutar_calculo(gini_float)
        
        print(f"[Python] Resultado final recibido desde C: {resultado_final}")