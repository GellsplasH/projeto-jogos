import random

def jogar():

    def titulo_jogo():
        print("---------------------")
        print("--- JOGO DA FORCA ---")
        print("---------------------")
    titulo_jogo()

    def palavras_secretas():
        arquivo = open("projeto jogos\palavras.txt", "r")
        palavras = []
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)
        numero = random.randrange(0, len(palavras))
        palavra = palavras[numero].upper()

        arquivo.close()
        return palavra
    
    palavra_secreta = palavras_secretas()
    letras_acertadas = ["_" for letra in palavra_secreta]

    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    
    while(not enforcou and not acertou):
        chute = input("Digite uma letra: ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1

        else:
            erros += 1
            desenho_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    def fim_de_jogo():
        if acertou:
            print("Você ganhou!")
            desenho_vencedor()
            print("Fim de jogo.")
        else:
            print("Você perdeu!")
            print("Fim de jogo.")
    fim_de_jogo()

def desenho_forca(erros):

    if erros == 1:
        print("    +---+    ")
        print("    |   |    ")
        print("        |    ")
        print("        |    ")
        print("        |    ")
        print("        |    ")
        print("    =========")


    if erros == 2:
        print("    +---+    ")
        print("    |   |    ")
        print("    O   |    ")
        print("        |    ")
        print("        |    ")
        print("        |    ")
        print("    =========")


    if erros == 3:
        print("    +---+    ")
        print("    |   |    ")
        print("    O   |    ")
        print("    |   |    ")
        print("        |    ")
        print("        |    ")
        print("    =========")


    if erros == 4:
        print("    +---+    ")
        print("    |   |    ")
        print("    O   |    ")
        print("   /|   |    ")
        print("        |    ")
        print("        |    ")
        print("    =========")


    if erros == 5:
        print("    +---+    ")
        print("    |   |    ")
        print("    O   |    ")
        print("   /|\  |    ")
        print("        |    ")
        print("        |    ")
        print("    =========")


    if erros == 6:
        print("    +---+    ")
        print("    |   |    ")
        print("    O   |    ")
        print("   /|\  |    ")
        print("   /    |    ")
        print("        |    ")
        print("    =========")
        
            
    if erros == 7:
        print("    +---+    ")
        print("    |   |    ")
        print("    O   |    ")
        print("   /|\  |    ")
        print("   / \  |    ")
        print("        |    ")
        print("    =========")
            
def desenho_vencedor():
    print("Este é seu premio!")     
    print("       ____      ")
    print("      |    |     ")
    print("      |    |     ")
    print("      |____|     ")
    print("      |    |     ")
    print("      (    )     ")
    print("      )    (     ")
    print("    .'      `.   ")
    print("   /          \  ")
    print("  |------------| ")
    print("  |JACK DANIELS| ")
    print("  |    ----    | ")
    print("  |   (No.7)   | ")
    print("  |    ----    | ")
    print("  | Tennessee  | ")
    print("  |  WHISKEY   | ")
    print("  |  40% Vol.  | ")
    print("  |------------| ")
    print("  |____________| ")




if(__name__ == "__main__"):
    jogar()