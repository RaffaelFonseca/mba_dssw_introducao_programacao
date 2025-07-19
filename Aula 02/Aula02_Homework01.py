# --- Cálculo de Tempo de Viagem ---

try:
    # Solicita a distância da viagem em quilômetros
    distancia = float(input("Digite a distância total da viagem em km: "))

    # Solicita a velocidade média em quilômetros por hora
    velocidade_media = float(input("Digite a velocidade média esperada em km/h: "))

    # Verifica se a velocidade média é zero para evitar divisão por zero
    if velocidade_media <= 0:
        print("A velocidade média deve ser maior que zero para calcular o tempo de viagem.")
    else:
        # Calcula o tempo de viagem
        tempo_viagem_horas = distancia / velocidade_media

        # Exibe o resultado
        print(f"\nPara uma viagem de {distancia:.2f} km a uma velocidade média de {velocidade_media:.2f} km/h,")
        print(f"o tempo estimado de viagem é de {tempo_viagem_horas:.2f} horas.")

except ValueError:
    # Captura o erro se o usuário digitar algo que não seja um número
    print("\nEntrada inválida! Por favor, digite apenas números para a distância e a velocidade.")
except Exception as e:
    # Captura qualquer outro erro inesperado
    print(f"\nOcorreu um erro inesperado: {e}")