import random

def jogar():

    print("------------------")
    print("JOGO DA ADVINHAÇÃO")
    print("------------------")

    numero_secreto = random.randint(1, 100)

    pontos = 1000
    tentativas_max = 0
    multiplicador_pontos = 0
    rodada = 0

    def dificuldade():
        global tentativas_max
        while True:
            try:
                print("Selecione um Nível de dificuldade:")
                nivel_dificuldade = int(input("'1' = Fácil / '2' = Médio / '3' = Difícil: "))
                if nivel_dificuldade == 1:
                    print("Nível Fácil Selecionado:")
                    tentativas_max = 20
                elif nivel_dificuldade == 2:
                    print("Nível Médio Selecionado:")
                    tentativas_max = 10
                elif nivel_dificuldade == 3:
                    print("Nível Difícil Selecionado:")
                    tentativas_max = 5
                return tentativas_max
            except:
                print("Selecione o Nível de Dificuldade!")

    tentativas_max = dificuldade()

    def multiplicador_pontuacao():
        if tentativas_max == 20:
            multiplicador_pontos = 50
        elif tentativas_max == 10:
            multiplicador_pontos = 30
        elif tentativas_max == 5:
            multiplicador_pontos = 10
        return multiplicador_pontos
        
    multiplicador_pontos = multiplicador_pontuacao()

    def engine_jogo():
        def conferir():
            if chute_usuario <= 0:
                print("O número deve ser maior que 0")
                return False
            elif chute_usuario >= 100:
                print("O número deve ser menor que 100")
                return False
            return True

        for rodada in range(1, tentativas_max + 1):
            print(f"Tentativa {rodada} de {tentativas_max}")
            while True:
                try:
                    chute_usuario = int(input("Digite um número entre 1 e 100: "))
                    if not conferir():
                        continue
                    break
                except ValueError:
                    print("Digite apenas números!")

            if chute_usuario == numero_secreto:
                print(f"Você acertou!\nE fez {pontuacao} pontos.")
                print(f"O número secreto é {numero_secreto}")
                print("Fim de jogo")
                break
            
            else:
                if chute_usuario > numero_secreto:
                    print("O número secreto é menor que esse...")
                elif chute_usuario < numero_secreto:
                    print("O número secreto é maior que esse...")
                pontos_perdidos = rodada * multiplicador_pontos
                pontuacao = pontos - pontos_perdidos

            if rodada == tentativas_max:
                print("Suas tentativas acabaram!")
                print(f"O número secreto era: {numero_secreto} você fez 0 pontos")

    engine_jogo()

if(__name__ == "__main__"):
    jogar()

