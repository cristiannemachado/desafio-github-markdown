def desafio_impar_ou_par():
    print("Desafio 1 - Ímpar ou Par")
    try:
        numero = int(input("Digite um número inteiro: "))
        if numero % 2 == 0:
            print("Par")
        else:
            print("Ímpar")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")

def desafio_soma_simples():
    print("\nDesafio 2 - Soma Simples")
    try:
        entrada = input("Digite dois números separados por espaço: ")
        partes = entrada.strip().split()

        if len(partes) != 2:
            print("Por favor, digite exatamente dois números.")
            return

        num1 = int(partes[0])
        num2 = int(partes[1])
        resultado = num1 + num2
        print(resultado)
    except ValueError:
        print("Entrada inválida. Certifique-se de digitar dois números inteiros.")

if __name__ == "__main__":
    desafio_impar_ou_par()
    desafio_soma_simples()
