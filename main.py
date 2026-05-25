import random

palavras = ["python", "programacao", "computador", "teclado", "internet"]

palavra = random.choice(palavras)

letras_corretas = []
letras_erradas = []
tentativas = 6

print("=== JOGO DA FORCA ===")

while tentativas > 0:

    palavra_oculta = ""

    for letra in palavra:
        if letra in letras_corretas:
            palavra_oculta += letra + " "
        else: 
            palavra_oculta += "_ "

    print("\nPalavra: ", palavra_oculta)

    # Verifica vitória
    if "_" not in palavra_oculta:
        print("Você venceu!")
        break

    tentativa = input("Digite um letra: ").lower().strip()

    # Validação
    if len(tentativa) != 1 or not tentativa.isalpha():
        print("Digite apenas uma letra válida.")
        continue

    # Evita repetir letra
    if tentativa in letras_corretas or tentativa in letras_erradas:
        print("Você já tentou essa letra. Tente outra.")
        continue

    # Acerto
    if tentativa in palavra:
        letras_corretas.append(tentativa)
        print("Letra correta!")

    # Erro
    else:
        letras_erradas.append(tentativa)
        tentativas -= 1

        print("Letra errada!")
        print(f"Tentativas restantes: {tentativas}")

 # Derrota
if tentativas == 0:
    print(f"\nVocê perdeu! A palavra era: {palavra}")
