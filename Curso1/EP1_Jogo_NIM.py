def  campeonato():
        y = 1
        while (y <= 3):
            print("\n**** Rodada", y, "****\n")
            partida()
            y += 1
        print("\n**** Final do campeonato! ****")
        print("\nPlacar: Você 0 X 3 Computador")   

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    if (n % (m + 1) == 0):
        print("\nVocê começa!")
        while(n > 0):
            n -= usuario_escolhe_jogada(n,m)
            if (n > 0):
                n -= computador_escolhe_jogada(n,m)
                if (n > 0):
                    print("Agora restam", n,"peças no tebuleiro.")
        
    else:
        print("\nComputador começa!")
        while(n > 0):
            n -= computador_escolhe_jogada(n,m)
            if(n > 0):
                print("Agora restam", n,"peças no tabuleiro.")
                n -= usuario_escolhe_jogada(n,m)
                
    print("Fim do Jogo! O Computador ganhou!")

def usuario_escolhe_jogada(n, m):
    x = int(input("\nQuantas peças você vai tirar? "))

    while (x > m or x <= 0 or x > n):
        print("\nOops! Jogada inválida! Tente de novo.")
        x = int(input("\nQuantas peças você vai tirar? "))
        
    if (x == 1):
        print("\nVocê tirou uma peça.")
    else:
        print("\nVocê tirou", x, "peças.")

    n -= x

    if (n > 1):
        print("Agora restam", n, "peças no tabuleiro")
    else:
        print("Agora resta apenas uma peça no tabuleiro")
    
    return x 

def computador_escolhe_jogada(n, m):
    if (n <= m):
        print("\nO computador tirou", n, "peças.")
        return n
    else:
        x = n % (m + 1)
        if (x > 0):
            print("\nO computador tirou", x, "peças.")
            return x
        else:
            print("\nO computador tirou", m, "peças.")
            return m

print("Bem-vindo ao jogo do NIM! Escolha: ")
print("1 - para jogar uma partida isolada")
x = int(input("2 - para jogar um campeonato "))
if (x == 1):
    print("\nVoce escolheu uma partida isolada!")
    partida()
elif (x == 2):
    y = 1
    print("\nVoce escolheu um campeonato!")
    campeonato()