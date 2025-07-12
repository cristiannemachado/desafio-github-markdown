def analisar_depoimentos(depoimentos):
    suspeitos = list(depoimentos.keys())
    for hipotese in suspeitos:
        veredito = {}
        for pessoa in suspeitos:
            if pessoa == hipotese:
                veredito[pessoa] = "verdadeiro"
            else:
                veredito[pessoa] = "mentiroso"

        if verificar_consistencia(depoimentos, veredito):
            return veredito
    return None

def verificar_consistencia(depoimentos, veredito):
    for pessoa, fala in depoimentos.items():
        if veredito[pessoa] == "verdadeiro":
            if veredito.get(fala) != "verdadeiro":
                return False
        else:
            if veredito.get(fala) == "verdadeiro":
                return False
    return True

if __name__ == "__main__":
    print("🌴 Desafio: Ilha dos Mentirosos 🌴")
    depoimentos = {}

    n = int(input("Quantos moradores serão interrogados? "))
    for _ in range(n):
        nome = input("Nome do morador: ").strip()
        fala = input(f'O que {nome} disse? (Ex: "João é verdadeiro"): ').strip()
        partes = fala.split(" é ")
        if len(partes) == 2:
            depoimentos[nome] = partes[0]

    resultado = analisar_depoimentos(depoimentos)

    if resultado:
        print("\n🔍 Veredito final:")
        for pessoa, tipo in resultado.items():
            print(f"- {pessoa}: {tipo}")
    else:
        print("\n❌ Nenhuma combinação consistente encontrada.")

