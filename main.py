import random

def simular_monty_hall(cambiar_puerta):
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
        puerta_participante = [puerta for puerta in range(1, 4) if puerta != puerta_participante and puerta != puerta_abierta][0]
    
    # Resultado final
    gano_auto = puerta_participante == puerta_auto
    
    # Imprimir resultados
    print("Puerta elegida por el participante:", puerta_participante)
    print("Puerta donde está el auto:", puerta_auto)
    print("Puerta abierta por el presentador:", puerta_abierta)
    if cambiar_puerta:
        print("El participante cambió a la puerta:", puerta_participante)
    print("Resultado del concurso: El participante", "gana el auto." if gano_auto else "no gana el auto.")

# Ejemplo de uso:
simular_monty_hall(cambiar_puerta=True)
