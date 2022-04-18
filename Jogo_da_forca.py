import random
titulo = "Jogo da forca"
linha = "-" * 50

print(linha)
print(titulo)
print(linha)

lista = ["item", "gratuito", "proibido", "rubrica", "recorde", "pudico", "menu", "ali", "raiz", "higiene", "somente",
         "sozinho", "coco", "flor", "cor"]

palavra = random.choice(lista).upper().strip()
listacerto = []
listaerrado = []

while True:
    adivinha = str(input("Qual letra você quer? ")).strip().upper()[0]
    if adivinha in palavra:
        print("Você acertou uma letra da palavra ")
        listacerto.append(adivinha)
        print(linha)
    else:
        print("Você errou! Tente Novamente")
        listaerrado.append(adivinha)
        print(linha)
    s = str(input("Escolha uma das opções"
                  "\n1 - Saber a palavra [1]"
                  "\n2 - Tenta uma nova letra [2]"
                  "\n3 - Tentar adivinhar a palavra [3] "
                  "\nQual opção você deseja: ")).strip().upper()[0]
    print(linha)
    if s in "1":
        break
    if s in "2":
        print(f"Letras digitadas que contém na palavra: {listacerto}")
        print(f"Letras digitadas que não contém na palavra:{listaerrado}")
    if s in "3":
        print(f"Letras acertadas por você {listacerto}")
        ad = str(input("Qual é a palavra? ")).strip().upper()
        if ad == palavra:
            print(f"Voce acertou! Parabêns")
            print("       ___________      ")
            print("      '._==_==_=_.'     ")
            print("      .-||:      /-.    ")
            print("     | (|:.     |) |    ")
            print("      '-|:.     |-'     ")
            print("        ||::.    /      ")
            print("         '::. .'        ")
            print("           ) (          ")
            print("         _.' '._        ")
            print("        '-------'       ")
            break
        else:
            print(f"Você errou! Tente Novamente")
            print(f"A palavra era {palavra}")
            exit()
print(f"A palavra era {palavra}")
input()
