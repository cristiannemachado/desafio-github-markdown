def cifra_cesar(texto, chave, modo='codificar'):
    resultado = ''
    for char in texto:
        if char.isalpha():
            deslocamento = chave if modo == 'codificar' else -chave
            base = ord('A') if char.isupper() else ord('a')
            novo_char = chr((ord(char) - base + deslocamento) % 26 + base)
            resultado += novo_char
        else:
            resultado += char
    return resultado

if __name__ == '__main__':
    print("🌟 Cifra de César Interativa 🌟")
    modo = input("Você quer codificar ou decodificar? [codificar/decodificar] ").strip().lower()
    texto = input("Digite o texto: ")
    chave = int(input("Digite a chave de deslocamento (número): "))
    resultado = cifra_cesar(texto, chave, modo)
    print(f"\n🔐 Resultado: {resultado}")
 Ilha dos Mentirosos

