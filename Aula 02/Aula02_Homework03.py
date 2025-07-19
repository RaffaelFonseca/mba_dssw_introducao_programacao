# Importa a função pi do módulo math para maior precisão
import math

# --- Cálculo do Volume de uma Esfera ---

# Define a constante pi (você também pode usar math.pi para maior precisão)
PI = math.pi # Usando a constante pi do módulo math para precisão

try:
    # Solicita ao usuário o raio da esfera
    raio = float(input("Digite o raio da esfera (em unidades de medida, ex: cm, metros): "))

    # Verifica se o raio é negativo, pois um raio não pode ser negativo
    if raio < 0:
        print("O raio não pode ser um valor negativo. Por favor, digite um número positivo.")
    else:
        # Calcula o volume usando a fórmula V = (4/3) * pi * r³
        # O cálculo 4/3 deve ser feito com pelo menos um dos números como float (ex: 4.0/3)
        # para garantir um resultado decimal preciso.
        volume = (4/3) * PI * (raio ** 3) # raio ** 3 é o mesmo que raio * raio * raio

        # Exibe o volume calculado, formatado para duas casas decimais
        print(f"\nPara uma esfera com raio de {raio:.2f} unidades,")
        print(f"o volume calculado é de {volume:.2f} unidades cúbicas.")

except ValueError:
    # Lida com o erro caso o usuário não digite um número válido para o raio
    print("Entrada inválida. Por favor, digite um número para o raio.")
except Exception as e:
    # Captura qualquer outro erro inesperado
    print(f"Ocorreu um erro inesperado: {e}")