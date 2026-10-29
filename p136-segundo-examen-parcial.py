# ==========================================================
# Archivo: p136-segundo-examen-parcial.py
# Descripción: Sistema de registro de vuelos ("AeroRegistro")
# Evaluación de colecciones en Python (Listas, Diccionarios, Sets y Tuplas)
# ==========================================================

def registrar_vuelos():
    """
    Función encargada de la captura interactiva de los datos de los vuelos.
    Implementa un ciclo while y almacena cada registro en una Lista de Diccionarios[cite: 1, 3].
    """
    # LISTA PRINCIPAL: Almacenará los diccionarios con los datos de cada vuelo capturado[cite: 1]
    inventario_vuelos = []
    
    print("AeroRegistro Sistema de Vuelos")
    print("Captura de datos de los vuelos (* para terminar):")
    
    while True:
        # Solicitar el identificador del vuelo
        numero_vuelo = input("\nNúmero de vuelo (ej. AA-101, * para terminar): ").strip()
        
        # Condición de salida: si el usuario ingresa '*' o deja vacío, se detiene el ciclo[cite: 1]
        if numero_vuelo == "*" or numero_vuelo == "":
            print("Finalizando captura de datos...")
            break
            
        # Solicitar atributos restantes del vuelo
        origen = input("Ciudad de origen (ej. Ciudad de México): ").strip()
        destino = input("Ciudad de destino (ej. Guadalajara): ").strip()
        aerolinea = input("Aerolínea (ej. Volaris): ").strip()
        
        # Validación de tipos de datos numéricos (Manejo de excepciones)
        try:
            pasajeros = int(input("Número de pasajeros a bordo: "))
            tarifa = float(input("Tarifa del boleto en pesos: "))
        except ValueError:
            print("❌ Error: Los pasajeros deben ser enteros y la tarifa un número válido. Vuelva a intentar este vuelo.")
            continue
        
        # DICCIONARIO: Almacena los atributos individuales del vuelo actual[cite: 1]
        vuelo = {
            "numero_vuelo": numero_vuelo,
            "origen": origen,
            "destino": destino,
            "aerolinea": aerolinea,
            "pasajeros": pasajeros,
            "tarifa": tarifa
        }
        
        # Agregar el diccionario del vuelo a la lista principal (Inventario)[cite: 1]
        inventario_vuelos.append(vuelo)
        
    return inventario_vuelos

def main():
    """
    Función principal que coordina el procesamiento, extracción de colecciones,
    visualización en tabla y la analítica matemática del sistema[cite: 1, 2, 3].
    """
    # 1. Capturar los datos utilizando la función interactiva
    inventario = registrar_vuelos()
    
    # Validar si se registraron datos antes de procesar
    if not inventario:
        print("\nNo se registraron vuelos en el sistema.")
        return

    print("\n" + "="*50)
    print("RESULTADOS DEL REGISTRO DE VUELOS")
    print("="*50)
    
    # 2. Datos Crudos: Impresión directa de la lista de diccionarios[cite: 2]
    print("\nDatos (Lista de diccionarios):")
    print(inventario)
    
    # ==========================================
    # Extracción de Colecciones Especiales
    # ==========================================
    
    # 3. CONJUNTOS (SETS): Extraer un conjunto con los destinos únicos sin repetir ciudades[cite: 1]
    destinos_unicos = {vuelo["destino"] for vuelo in inventario}
    print("\nDestinos Únicos (Conjunto):")
    print(destinos_unicos)
    
    # 4. TUPLAS: Generar una lista de tuplas para el registro histórico inmutable 
    # Contiene exclusivamente: (numero_vuelo, aerolinea, destino)[cite: 1]
    registro_historico = [
        (vuelo["numero_vuelo"], vuelo["aerolinea"], vuelo["destino"]) 
        for vuelo in inventario
    ]
    print("\nRegistro Inmutable (Tuplas):")
    print(registro_historico)
    
    # ==========================================
    # Formato Tabular y Visualización
    # ==========================================
    
    # 5. Formato Tabular: Organizar los datos en una tabla limpia y alineada con f-strings[cite: 2, 3]
    print("\nTabla de datos:")
    print(f"{'No. Vuelo':<10} | {'Origen':<12} | {'Destino':<12} | {'Aerolínea':<12} | {'Pasajeros':<10} | {'Tarifa':<10}")
    print("-" * 75)
    for vuelo in inventario:
        print(f"{vuelo['numero_vuelo']:<10} | {vuelo['origen']:<12} | {vuelo['destino']:<12} | {vuelo['aerolinea']:<12} | {vuelo['pasajeros']:<10} | ${vuelo['tarifa']:,.2f}")
    
    # ==========================================
    # Analítica y Cálculos Matemáticos
    # ==========================================
    total_vuelos = len(inventario)
    
    # Diccionarios auxiliares para conteos por categoría
    vuelos_por_aerolinea = {}
    vuelos_por_destino = {}
    
    # Acumuladores para sumatorias
    suma_pasajeros = 0
    suma_tarifas = 0.0
    
    # Inicialización de referencias para el vuelo más caro y más barato
    vuelo_mas_caro = inventario[0]
    vuelo_mas_barato = inventario[0]
    
    # Recorrido del inventario para procesar las métricas
    for vuelo in inventario:
        # Conteo de vuelos por aerolínea
        aerolinea = vuelo["aerolinea"]
        vuelos_por_aerolinea[aerolinea] = vuelos_por_aerolinea.get(aerolinea, 0) + 1
        
        # Conteo de vuelos por ciudad de destino
        destino = vuelo["destino"]
        vuelos_por_destino[destino] = vuelos_por_destino.get(destino, 0) + 1
        
        # Sumar totales de pasajeros y tarifas
        suma_pasajeros += vuelo["pasajeros"]
        suma_tarifas += vuelo["tarifa"]
        
        # Determinar extremos (precio máximo y mínimo)
        if vuelo["tarifa"] > vuelo_mas_caro["tarifa"]:
            vuelo_mas_caro = vuelo
        if vuelo["tarifa"] < vuelo_mas_barato["tarifa"]:
            vuelo_mas_barato = vuelo
            
    # Cálculo de promedios
    promedio_pasajeros = suma_pasajeros / total_vuelos
    promedio_tarifa = suma_tarifas / total_vuelos
    
    # Impresión del Resumen Analítico Final[cite: 2]
    print("\nResumen:")
    print(f"Vuelos totales: {total_vuelos}")
    
    print("Aerolíneas:")
    for aerolinea, cantidad in vuelos_por_aerolinea.items():
        print(f"{aerolinea}: {cantidad}")
        
    print("Destinos:")
    for destino, cantidad in vuelos_por_destino.items():
        print(f"{destino}: {cantidad}")
        
    print(f"Pasajeros -> Suma: {suma_pasajeros}, Promedio: {promedio_pasajeros:.2f}")
    print(f"Tarifa -> Suma: ${suma_tarifas:,.2f}, Promedio: ${promedio_tarifa:,.2f}")
    print(f"{vuelo_mas_caro['numero_vuelo']} de ${vuelo_mas_caro['tarifa']:,.2f} es el más caro, {vuelo_mas_barato['numero_vuelo']} de ${vuelo_mas_barato['tarifa']:,.2f} es el más barato.")

if __name__ == "__main__":
    main()