# --- Calculadora de Índice de Massa Corporal (IMC) ---

try:
    # Solicita a altura do usuário em metros
    altura = float(input("Digite sua altura em metros (ex: 1.75): "))

    # Solicita o peso do usuário em quilogramas
    peso = float(input("Digite seu peso em quilogramas (ex: 70.5): "))

    # Valida se a altura e o peso são valores positivos
    if altura <= 0 or peso <= 0:
        print("Altura e peso devem ser valores positivos. Por favor, tente novamente.")
    else:
        # Calcula o IMC usando a fórmula: IMC = peso / (altura * altura)
        imc = peso / (altura * altura)

        # Exibe o resultado do IMC formatado para duas casas decimais
        print(f"\nSua altura: {altura:.2f} m")
        print(f"Seu peso: {peso:.2f} kg")
        print(f"Seu Índice de Massa Corporal (IMC) é: {imc:.2f}")

except ValueError:
    # Captura o erro se o usuário digitar algo que não seja um número
    print("\nEntrada inválida! Por favor, digite apenas números para altura e peso.")
except Exception as e:
    # Captura qualquer outro erro inesperado
    print(f"\nOcorreu um erro inesperado: {e}")