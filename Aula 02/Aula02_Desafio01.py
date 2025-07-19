# Solicita que o usuário insira um número inteiro
try:
    numero = int(input("Digite um número inteiro: "))

    # Verifica se o número é par ou ímpar usando o operador de módulo (%)
    if numero % 2 == 0:
        print(f"O número {numero} é PAR.")
    else:
        print(f"O número {numero} é ÍMPAR.")

except ValueError:
    print("Isso não é um número inteiro válido. Por favor, digite um número inteiro.")

#Como este código funciona:
#input("Digite um número inteiro: "): Esta linha exibe a mensagem "Digite um número inteiro: " na tela e espera que você digite algo e pressione Enter. Tudo que você digita é lido como texto.

#numero = int(...): A função int() tenta converter o texto que você digitou em um número inteiro. Se você digitar algo que não pode ser convertido para um número inteiro (como "abc" ou "3.5"), um erro (ValueError) será gerado.

#try...except ValueError: Este bloco é para tratar erros.

#O código dentro do try é executado primeiro. Se tudo correr bem (se você digitar um número inteiro), ele continua.

#Se um ValueError acontecer (por exemplo, se você não digitar um número inteiro), o código dentro do except ValueError é executado, informando que a entrada é inválida.

#if numero % 2 == 0:: Esta é a mágica!

#O símbolo % é o operador de módulo. Ele retorna o resto de uma divisão.

#Um número é par se, quando dividido por 2, o resto é exatamente 0.

#Se o resto for 0, a condição numero % 2 == 0 é verdadeira, e o programa imprime que o número é PAR.

#else:: Se a condição acima não for verdadeira (ou seja, o resto da divisão por 2 não é 0), significa que o número é ímpar. Nesse caso, o programa imprime que o número é ÍMPAR.






