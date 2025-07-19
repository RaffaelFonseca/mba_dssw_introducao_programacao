# Definindo a taxa de câmbio fixa
TAXA_CAMBIO_BRL_USD = 5.0

# Solicita ao usuário o valor em Reais (BRL)
try:
    valor_em_reais = float(input("Digite o valor em Reais (BRL) para converter para Dólar: "))

    # Verifica se o valor inserido é negativo
    if valor_em_reais < 0:
        print("Por favor, digite um valor positivo em Reais.")
    else:
        # Realiza a conversão
        valor_em_dolar = valor_em_reais / TAXA_CAMBIO_BRL_USD

        # Exibe o resultado formatado
        print(f"\n{valor_em_reais:.2f} BRL equivalem a {valor_em_dolar:.2f} USD (considerando 1 USD = {TAXA_CAMBIO_BRL_USD:.2f} BRL).")

except ValueError:
    # Lida com o erro caso o usuário não digite um número válido
    print("Entrada inválida. Por favor, digite um número para o valor em Reais.")
except Exception as e:
    # Lida com qualquer outro erro inesperado
    print(f"Ocorreu um erro inesperado: {e}")