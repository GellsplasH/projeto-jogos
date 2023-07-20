import jogo_forca
import Jogo_advinhação2

print("---------------------")
print("--- PROJETO JOGOS ---")
print("---------------------")


def game_select():
    try:
        while True:
            print("(1) Forca - (2) Advinhação")
            jogo = int(input("QUAL JOGO VOCÊ QUER JOGAR? "))
            if jogo == 1:
                print("Forca Escolhido...")
                jogo_forca.jogar()
            
            elif jogo == 2:
                print("Advinhação Escolhido...")
                Jogo_advinhação2.jogar()
                
            else:
                return False

    except ValueError:
        print("Escolha um dos jogos (1) Forca ou (2) Advinhação...")

game_select()