import random

def jogar():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    ganhou = False

    print("="*30)
    print("BEM-VINDO AO ADIVINHE O NÚMERO!")
    print("Tente adivinhar o número entre 1 e 100.")
    print("="*30)

    while not ganhou:
        try:
            chute = int(input("Digite seu palpite: "))
            tentativas += 1

            if chute < numero_secreto:
                print("Mais alto... Tente novamente!")
            elif chute > numero_secreto:
                print("Mais baixo... Tente novamente!")
            else:
                ganhou = True
                print(f"\n🎉 PARABÉNS! Você acertou em {tentativas} tentativas.")
        
        except ValueError:
            print("Ops! Digite apenas números inteiros.")

if __name__ == "__main__":
    jogar()