def sistema_mru():
    print("=== SISTEMA DE MOVIMIENTO RECTILÍNEO UNIFORME (MRU) ===")
    print("1. Calcular distancia")
    print("2. Calcular velocidad")
    print("3. Calcular tiempo")
    print("4. Calcular velocidad en m/s (desde km y minutos)")

    opcion = int(input("Seleccione una opción (1-4): "))

    match opcion:

        case 1:
            print("\n--- Cálculo de Distancia ---")
            velocidad = float(input("Ingrese la velocidad (m/s): "))
            tiempo = float(input("Ingrese el tiempo (s): "))

            if velocidad > 0 and tiempo > 0:
                distancia = velocidad * tiempo
                print(f"Distancia recorrida: {distancia} metros")
            else:
                print("Los valores deben ser mayores que 0")

        case 2:
            print("\n--- Cálculo de Velocidad ---")
            distancia = float(input("Ingrese la distancia (m): "))
            tiempo = float(input("Ingrese el tiempo (s): "))

            if tiempo > 0:
                velocidad = distancia / tiempo
                print(f"Velocidad media: {velocidad} m/s")
            else:
                print("El tiempo debe ser mayor que 0")

        case 3:
            print("\n--- Cálculo de Tiempo ---")
            distancia = float(input("Ingrese la distancia (m): "))
            velocidad = float(input("Ingrese la velocidad (m/s): "))

            if velocidad > 0:
                tiempo = distancia / velocidad
                print(f"Tiempo requerido: {tiempo} segundos")
            else:
                print("La velocidad debe ser mayor que 0")

        case 4:
            print("\n--- Conversión a m/s ---")
            distancia_km = float(input("Ingrese la distancia (km): "))
            tiempo_min = float(input("Ingrese el tiempo (min): "))

            if tiempo_min > 0:
                distancia_m = distancia_km * 1000
                tiempo_s = tiempo_min * 60
                velocidad = distancia_m / tiempo_s
                print(f"Velocidad en el SI: {velocidad} m/s")
            else:
                print("El tiempo debe ser mayor que 0")

        case _:
            print("Opción inválida")


sistema_mru()
