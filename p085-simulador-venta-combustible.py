# Archivo Principal: p085_Simulador VentaCombustible.py
# Descripción: Sistema interactivo de consola para la gestión de una estación de servicio.

while True:
    print("\n================================================================")
    print("          SISTEMA DE GESTIÓN - ESTACIÓN GASOLINERA")
    print("================================================================")
    print("1. Venta de Combustible")
    print("2. Simulación de Rendimiento")
    print("3. Clasificador de Cliente")
    print("4. Salir")
    print("================================================================")
    
    opcion = input("Seleccione una opción (1-4): ")
    
    # Validar que la opción sea un número entero
    if not opcion.isdigit():
        print("\n[ERROR] Opción inválida. Ingrese un número entre 1 y 4.")
        continue
        
    opcion = int(opcion)
    
    # Opción 1: Venta de Combustible
    if opcion == 1:
        print("\n--- MÓDULO DE VENTA DE COMBUSTIBLE ---")
        tipo_combustible = input("Ingrese el tipo de combustible (Ej. Magna, Premium, Diésel): ")
        
        precio_litro = float(input("Ingrese el precio por litro ($): "))
        if precio_litro <= 0:
            print("\n[ERROR] El precio por litro debe ser mayor a cero.")
            continue
            
        cantidad_litros = float(input("Ingrese la cantidad de litros a comprar: "))
        if cantidad_litros <= 0:
            print("\n[ERROR] La cantidad de litros debe ser mayor a cero.")
            continue
            
        total_pagar = precio_litro * cantidad_litros
        
        print("\n" + "="*40)
        print(f"{'TICKET DE VENTA':^40}")
        print("="*40)
        print(f"Combustible: {tipo_combustible:>27}")
        print(f"Precio por litro:          ${precio_litro:>13.2f}")
        print(f"Cantidad de litros:        {cantidad_litros:>14.2f} L")
        print("-" * 40)
        print(f"TOTAL A PAGAR:             ${total_pagar:>13.2f}")
        print("=" * 40)
        
    # Opción 2: Simulación de Rendimiento (Fase 4: Ciclo for con range() y tablas alineadas)
    elif opcion == 2:
        print("\n--- SIMULACIÓN DE RENDIMIENTO ---")
        kilometraje_inicial = float(input("Ingrese el kilometraje inicial del vehículo: "))
        factor_rendimiento = float(input("Ingrese el factor de rendimiento base (km por litro): "))
        
        if factor_rendimiento <= 0:
            print("\n[ERROR] El factor de rendimiento debe ser mayor a cero.")
            continue
            
        meses = int(input("Ingrese el número de meses a simular: "))
        if meses <= 0:
            print("\n[ERROR] El número de meses debe ser mayor a cero.")
            continue
            
        print("\n" + "="*65)
        print(f"{'TABLA DE PROYECCIÓN DE RENDIMIENTO Y CONSUMO':^65}")
        print("="*65)
        print(f"{'Mes':<6} | {'Km Estimado':<14} | {'Litros Consumidos':<18} | {'Factor (**)':<12}")
        print("-" * 65)
        
        # Uso obligatorio de ciclo for con range() y operadores aritméticos (//, %, **)
        for mes in range(1, meses + 1):
            desgaste = 1 + ((mes ** 1) * 0.01)  # Operador de potencia (**)
            km_acumulado = kilometraje_inicial + (mes * 500 * (factor_rendimiento ** 0.05))
            litros_estimados = (500 * mes) / factor_rendimiento
            
            # Operadores adicionales solicitados (división entera y residuo)
            verificacion_par = mes % 2  
            ciclo_revision = mes // 2   
            
            print(f"{mes:<6} | {km_acumulado:<14.2f} | {litros_estimados:<18.2f} | {desgaste:<12.2f}")
            
        print("=" * 65)
        
    # Opción 3: Clasificador de Cliente
    elif opcion == 3:
        print("\n--- CLASIFICADOR DE CLIENTES ---")
        volumen_mensual = float(input("Ingrese el volumen de compra mensual (en Litros): "))
        
        if volumen_mensual < 0:
            print("\n[ERROR] El volumen no puede ser negativo.")
            continue
            
        if volumen_mensual < 100:
            categoria = "Regular"
            beneficio = "Sin descuentos aplicables"
        elif volumen_mensual >= 100 and volumen_mensual <= 500:
            categoria = "Premium"
            beneficio = "Descuento del 5% en próxima compra"
        else:
            categoria = "Flotilla"
            beneficio = "Descuento del 10% y atención preferencial"
            
        print("\n" + "-"*40)
        print(f"Volumen Registrado: {volumen_mensual:,.2f} Litros")
        print(f"Categoría Asignada: {categoria}")
        print(f"Beneficio:          {beneficio}")
        print("-" * 40)
        
    # Opción 4: Salir
    elif opcion == 4:
        print("\nGracias por utilizar el sistema de la estación de servicio. ¡Hasta luego!")
        break
    else:
        print("\n[ERROR] Opción fuera de rango. Por favor, seleccione un número entre 1 y 4.")
        continue