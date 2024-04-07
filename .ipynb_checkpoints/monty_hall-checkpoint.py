import random

def simular_monty_hall(cambiar_puerta, imprimir = True):
    # Elección aleatoria de la puerta donde está el auto (1, 2 o 3)
    puerta_auto = random.randint(1, 3)
    
    # Elección aleatoria de la puerta por el participante (1, 2 o 3)
    puerta_participante = random.randint(1, 3)
    
    # Puertas restantes luego de la elección del participante
    puertas_restantes = [puerta for puerta in range(1, 4) if puerta != puerta_participante]
    
    # Si la puerta elegida por el participante contiene el auto, el presentador elige una de las otras dos puertas al azar
    if puerta_participante == puerta_auto:
        puerta_abierta = random.choice(puertas_restantes)
    else:
        # Si la puerta elegida por el participante no contiene el auto, el presentador abre la puerta que no contiene el auto
        puerta_abierta = [puerta for puerta in puertas_restantes if puerta != puerta_auto][0]
    
    # Si el participante decide cambiar de puerta
    if cambiar_puerta:
        nueva_puerta = [puerta for puerta in range(1, 4) if puerta != puerta_participante and puerta != puerta_abierta][0]
    else:
        nueva_puerta = puerta_participante
    
    # Resultado final
    gano_auto = nueva_puerta == puerta_auto

    if imprimir:
        # Imprimir resultados
        print("Puerta elegida por el participante:", puerta_participante)
        print("Puerta donde está el auto:", puerta_auto)
        print("Puerta abierta por el presentador:", puerta_abierta)
        if cambiar_puerta:
            print("El participante cambió a la puerta por la puerta numero ", nueva_puerta)
        print("Resultado del concurso: El participante", "gana el auto." if gano_auto else "no gana el auto.")
    
    return gano_auto

def simular_monty_hall_y_contar_victorias(num_simulaciones, cambiar_puerta):
    victorias = 0
    for _ in range(num_simulaciones):
        # Simular el juego de Monty Hall
        resultado = simular_monty_hall(cambiar_puerta, num_simulaciones == 1)
        if resultado:
            victorias += 1
    return victorias

def simular_juego_monty_hall():
    # Solicitar número de simulaciones al usuario
    num_simulaciones = int(input("Ingrese el número de simulaciones: "))
    
    # Solicitar estrategia al usuario
    cambio_puerta = input("¿Desea cambiar de puerta? (s/n): ").lower()
    if cambio_puerta == "s":
        cambiar_puerta = True
    else:
        cambiar_puerta = False

    # Simulaciones y contar victorias
    victorias = simular_monty_hall_y_contar_victorias(num_simulaciones, cambiar_puerta)

    # Imprimir resultados
    if cambiar_puerta:
        print(f"Para {num_simulaciones} simulaciones con cambio de puerta, el participante ganó el auto {victorias} veces.")
    else:
        print(f"Para {num_simulaciones} simulaciones sin cambio de puerta, el participante ganó el auto {victorias} veces.")

# Ejecutar la simulación del juego de Monty Hall, unicamente si el archivo es ejecutado, y no importado
if __name__ == '__main__':
    simular_juego_monty_hall()
