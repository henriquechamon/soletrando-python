import random

letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

pontos = 0

def jogo_soletrando():
    print("SOLETRANDO")
    print("Vamos jogar soletrando! Digite 'iniciar' para começar.")
    escolha = input()

    if escolha == "iniciar":
        while True:
            numero_aleatorio = random.randint(0, len(letras) - 1)
            letra = letras[numero_aleatorio].upper()

            print("Perfeito. A primeira letra é: " + letra)
            print("Insira uma palavra com a letra " + letra + ":")
            resposta = input()

            if letra.lower() or letra.upper() in resposta:
                print("Ok! Você acertou!")
                print("Sua palavra foi:" + resposta)
            else:
                print("Você errou! Reinicie o jogo.")

            print("Digite qualquer coisa para continuar ou 'sair' para encerrar o jogo.")
            continuar = input()
            if continuar == 'sair':
                break

jogo_soletrando()
