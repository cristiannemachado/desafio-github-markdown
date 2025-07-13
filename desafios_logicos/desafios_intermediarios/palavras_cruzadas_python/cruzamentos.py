def encontrar_cruzamentos(palavras):
    cruzamentos = []

    for i in range(len(palavras)):
        for j in range(i + 1, len(palavras)):
            p1 = palavras[i]
            p2 = palavras[j]
            limite = min(len(p1), len(p2))

            for k in range(limite):
                if p1[k] == p2[k]:
                    mensagem = f'"{p1}" e "{p2}" podem se cruzar na posição {k} ("{p1[k]}")'
                    cruzamentos.append(mensagem)

    return cruzamentos

if __name__ == "__main__":
    entrada = input("Digite as palavras separadas por vírgula: ")
    palavras = [p.strip() for p in entrada.split(",") if p.strip()]

    resultados = encontrar_cruzamentos(palavras)

    if resultados:
        print("\nCruzamentos encontrados:")
        for r in resultados:
            print("- " + r)
    else:
        print("\nNenhum cruzamento encontrado.")


