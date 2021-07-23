import pygame
from pygame.locals import *
from sys import exit

pygame.init()

tela = pygame.display.set_mode((600, 600), 0, 32)
pygame.display.set_caption("Jogo da velha")

ESTADO = "JOGANDO"
VEZ = "JOGADOR1"
ESCOLHA = "X"
CONTADOR_JOGADAS = 0

#Posições livres
free_positions = [0, 1, 2, 3, 4, 5, 6, 7, 8]

#Retangulos invisíveis presentes na tela (representam as 9 posições possíveis de jogo)
rect1 = Rect((0, 0), (200, 200))
rect2 = Rect((200, 0), (200, 200))
rect3 = Rect((400, 0), (200, 200))
rect4 = Rect((0, 200), (200, 200))
rect5 = Rect((200, 200), (200, 200))
rect6 = Rect((400, 200), (200, 200))
rect7 = Rect((0, 400), (200, 200))
rect8 = Rect((200, 400), (200, 200))
rect9 = Rect((400, 400), (200, 200))

#Lista com retangulos
rec = [rect1, rect2, rect3, rect4, rect5, rect6, rect7, rect8, rect9]


#Desenha tabuleiro na tela (Matriz 3x3)
def desenhar_tab():
    pygame.draw.line(tela, (255, 255, 255), (200, 0), (200, 600), 10)
    pygame.draw.line(tela, (255, 255, 255), (400, 0), (400, 600), 10)
    pygame.draw.line(tela, (255, 255, 255), (0, 200), (600, 200), 10)
    pygame.draw.line(tela, (255, 255, 255), (0, 400), (600, 400), 10)

def desenhar_peca(pos):
    x, y = pos
    if VEZ == 'JOGADOR2':
        pygame.draw.circle(tela, (0, 0, 255), pos, 50)
    else:
        img = pygame.image.load("x.png").convert_alpha() #Sem convert_alpha, distorce a imagem
        imgR = pygame.transform.scale(img, (100, 100))
        tela.blit(imgR, (x - 50, y - 50))

def faz_jogada():
    for p in rec:
        #Testa em qual dos retangulos invisíveis foi clicado
        if e.type == MOUSEBUTTONDOWN and p.collidepoint(mouse_pos):
            if p == rect1:
                confirmar(0, [100, 100])
            elif p == rect2:
                confirmar(1, [300, 100])
            elif p == rect3:
                confirmar(2, [500, 100])
            elif p == rect4:
                confirmar(3, [100, 300])
            elif p == rect5:
                confirmar(4, [300, 300])
            elif p == rect6:
                confirmar(5, [500, 300])
            elif p == rect7:
                confirmar(6, [100, 500])
            elif p == rect8:
                confirmar(7, [300, 500])
            elif p == rect9:
                confirmar(8, [500, 500])

def confirmar(indice, pos):
    if (free_positions[indice] == 'X' or free_positions[indice] == 'O'):
        print("Posicão ocupada!\n")
        pass
    else:
        free_positions[indice] = ESCOLHA
        desenhar_peca(pos)
        print(free_positions)

def ha_ganhador():
    #Para JOGADOR1 (X) -> Testando linhas (horizontal)
    if (free_positions[0] == 'X' and free_positions[1] == 'X' and free_positions[2] == 'X'):
        return True
    elif (free_positions[3] == 'X' and free_positions[4] == 'X' and free_positions[5] == 'X'):
        return True
    elif (free_positions[6] == 'X' and free_positions[7] == 'X' and free_positions[8] == 'X'):
        return True
    #Para JOGADOR1 (X) -> Testando colunas (vertical)
    elif (free_positions[0] == 'X' and free_positions[3] == 'X' and free_positions[6] == 'X'):
        return True
    elif (free_positions[1] == 'X' and free_positions[4] == 'X' and free_positions[7] == 'X'):
        return True
    elif (free_positions[2] == 'X' and free_positions[5] == 'X' and free_positions[8] == 'X'):
        return True
    #Para JOGADOR1 (X) -> Testando diagonais (principal e secundária)
    elif (free_positions[0] == 'X' and free_positions[4] == 'X' and free_positions[8] == 'X'):
        return True
    elif (free_positions[2] == 'X' and free_positions[4] == 'X' and free_positions[6] == 'X'):
        return True

     #Para JOGADOR2 (O) -> Testando linhas (horizontal)
    elif (free_positions[0] == 'O' and free_positions[1] == 'O' and free_positions[2] == 'O'):
        return True
    elif (free_positions[3] == 'O' and free_positions[4] == 'O' and free_positions[5] == 'O'):
        return True
    elif (free_positions[6] == 'O' and free_positions[7] == 'O' and free_positions[8] == 'O'):
        return True
    #Para JOGADOR2 (O) -> Testando colunas (vertical)
    elif (free_positions[0] == 'O' and free_positions[3] == 'O' and free_positions[6] == 'O'):
        return True
    elif (free_positions[1] == 'O' and free_positions[4] == 'O' and free_positions[7] == 'O'):
        return True
    elif (free_positions[2] == 'O' and free_positions[5] == 'O' and free_positions[8] == 'O'):
        return True
    #Para JOGADOR2 (O) -> Testando diagonais (principal e secundária)
    elif (free_positions[0] == 'O' and free_positions[4] == 'O' and free_positions[8] == 'O'):
        return True
    elif (free_positions[2] == 'O' and free_positions[4] == 'O' and free_positions[6] == 'O'):
        return True
    else:
        return False

def texto_vitoria(vencedor):
    arial = pygame.font.SysFont("arial", 70)
    mensagem = "JOGADOR {} VENCEU".format(vencedor)

    if (vencedor=="EMPATE"):
        mensagem_vitoria = arial.render("DEU VELHA", True, (0, 255, 0), 0)
    else:
        mensagem_vitoria = arial.render(mensagem, True, (0, 255, 0), 0)
    tela.blit(mensagem_vitoria, (0, 265))

while True:
    mouse_pos = pygame.mouse.get_pos()
    if (ESTADO == 'JOGANDO'):
        desenhar_tab()
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                exit()
            elif e.type == MOUSEBUTTONDOWN:
                faz_jogada()
                if (VEZ == "JOGADOR1"):
                    VEZ = "JOGADOR2"
                    ESCOLHA = 'O'
                else:
                    VEZ = "JOGADOR1"
                    ESCOLHA = 'X'
    
            elif (ha_ganhador()):
                if (VEZ == "JOGADOR2"):
                    texto_vitoria("X")
                    pygame.quit()
                else:
                    texto_vitoria("O")
                    pygame.quit()
    pygame.display.flip()

"""
#AS FUNÇÕES ABAIXO, FORAM FEITAS PARA TESTAR OS CÓDIGOS NO PROMPT, SEM INTERFACE GRÁFICA
def cria_tabuleiro(tabuleiro):
    contador = 1
    for i in range(3):
        for j in range(3):
            tabuleiro[i][j] = str(contador)
            contador = contador + 1

def exibe_tabuleiro(tabuleiro):
    for i in range(3):
        for j in range(3):
            print("                     ", tabuleiro[i][j], end=' ')
        print("\n")

#Verifica se é possível fazer a jogada
def verifica_jogada(posicao, tabuleiro):
    jogada_valida = False
    if (posicao == 1 and tabuleiro[0][0] != 'X' and tabuleiro[0][0] != 'O'):
        jogada_valida = True
    elif (posicao == 2 and tabuleiro[0][1] != 'X' and tabuleiro[0][1]!= 'O'):
        jogada_valida = True
    elif (posicao == 3 and tabuleiro[0][2] != 'X' and tabuleiro[0][2]!= 'O'):
        jogada_valida = True
    elif (posicao == 4 and tabuleiro[1][0] != 'X' and tabuleiro[1][0]!= 'O'):
        jogada_valida = True
    elif (posicao == 5 and tabuleiro[1][1] != 'X' and tabuleiro[1][1]!= 'O'):
        jogada_valida = True
    elif (posicao == 6 and tabuleiro[1][2] != 'X' and tabuleiro[1][2]!= 'O'):
        jogada_valida = True
    elif (posicao == 7 and tabuleiro[2][0] != 'X' and tabuleiro[2][0]!= 'O'):
        jogada_valida = True
    elif (posicao == 8 and tabuleiro[2][1] != 'X' and tabuleiro[2][1]!= 'O'):
        jogada_valida = True
    elif (posicao == 9 and tabuleiro[2][2] != 'X' and tabuleiro[2][2]!= 'O'):
        jogada_valida = True
    return jogada_valida

#Faz a jogada, alterando a posição escolhida pelo char do jogador atual
def faz_jogada(posicao, tabuleiro, jogador_atual):
    if (posicao == 1):
        tabuleiro[0][0] = jogador_atual
    elif (posicao == 2):
        tabuleiro[0][1] = jogador_atual
    elif (posicao == 3):
        tabuleiro[0][2] = jogador_atual
    elif (posicao == 4):
        tabuleiro[1][0] = jogador_atual
    elif (posicao == 5):
        tabuleiro[1][1] = jogador_atual
    elif (posicao == 6):
        tabuleiro[1][2] = jogador_atual
    elif (posicao == 7):
        tabuleiro[2][0] = jogador_atual
    elif (posicao == 8):
        tabuleiro[2][1] = jogador_atual
    else:
        tabuleiro[2][2] = jogador_atual

#Verifica se há ganhador
def ha_ganhador(tabuleiro):
    #Condições para X 
    #Testando linhas (na horizonal)
    if (tabuleiro[0][0] == 'X' and tabuleiro[0][1] == 'X' and tabuleiro[0][2] == 'X'):
        return True
    elif (tabuleiro[1][0] == 'X' and tabuleiro[1][1] == 'X' and tabuleiro[1][2] == 'X'):
        return True
    elif (tabuleiro[2][0] == 'X' and tabuleiro[2][1] == 'X' and tabuleiro[2][2] == 'X'):
        return True
    #Testando linhas (na vertical)
    elif (tabuleiro[0][0] == 'X' and tabuleiro[1][0] == 'X' and tabuleiro[2][0] == 'X'):
        return True
    elif (tabuleiro[0][1] == 'X' and tabuleiro[1][1] == 'X' and tabuleiro[2][1] == 'X'):
        return True
    elif (tabuleiro[0][2] == 'X' and tabuleiro[1][2] == 'X' and tabuleiro[2][2] == 'X'):
        return True
    #Testando diagonais
    elif(tabuleiro[0][0] == 'X' and tabuleiro[1][1] == 'X' and tabuleiro[2][2] == 'X'):
        return True
    elif(tabuleiro[0][2] == 'X' and tabuleiro[1][1] == 'X' and tabuleiro[2][0] == 'X'):
        return True 
    #Condições para O
    #Testando linhas (na horizontal) 
    elif (tabuleiro[0][0] == 'O' and tabuleiro[0][1] == 'O' and tabuleiro[0][2] == 'O'):
        return True
    elif (tabuleiro[1][0] == 'O' and tabuleiro[1][1] == 'O' and tabuleiro[1][2] == 'O'):
        return True
    elif (tabuleiro[2][0] == 'O' and tabuleiro[2][1] == 'O' and tabuleiro[2][2] == 'O'):
        return True
    #Testando linhas (na vertical)
    elif (tabuleiro[0][0] == 'O' and tabuleiro[1][0] == 'O' and tabuleiro[2][0] == 'O'):
        return True
    elif (tabuleiro[0][1] == 'O' and tabuleiro[1][1] == 'O' and tabuleiro[2][1] == 'O'):
        return True
    elif (tabuleiro[0][2] == 'O' and tabuleiro[1][2] == 'O' and tabuleiro[2][2] == 'O'):
        return True
     #Testando diagonais
    elif(tabuleiro[0][0] == 'O' and tabuleiro[1][1] == 'O' and tabuleiro[2][2] == 'O'):
        return True
    elif(tabuleiro[0][2] == 'O' and tabuleiro[1][1] == 'O' and tabuleiro[2][0] == 'O'):
        return True 
    else:
        return False

#Verifica se houve empate no jogo
#TENTAR IMPLEMENTAR MELHOR
def empatou(contador_empate, tabuleiro):
    if (contador_empate == 9 and not(ha_ganhador(tabuleiro))):
        return True
    return False

def jogada(jogador_atual, tabuleiro, contador_empate):
    posicao = 0
    jogada_valida = False
    if (not(ha_ganhador(tabuleiro))):        
        if (jogador_atual == 'X'):
            print("X JOGA\n")
            posicao = int(input("Digite uma posição de 1 a 9 para jogar:"))
            while(posicao<1 or posicao>9):
                print("Posição inválida!\n")
                posicao = int(input("Digite uma posição de 1 a 9 para jogar:"))
            jogada_valida = verifica_jogada(posicao, tabuleiro)
            print(f"Jogada válida:{jogada_valida}\n")
            while(jogada_valida == False):
                print("Posição já ocupada pelo outro jogador, escolha outra")
                posicao = int(input("Digite uma posição de 1 a 9 para jogar:"))
                while(posicao<1 or posicao>9):
                    print("Posição inválida!\n")
                    posicao = int(input("Digite uma posição de 1 a 9 para jogar:"))
                jogada_valida = verifica_jogada(posicao, tabuleiro)
            faz_jogada(posicao, tabuleiro, jogador_atual)
            ha_ganhador(tabuleiro)
        else:
            print("O JOGA\n")
            posicao = int(input("Digite uma posição de 1 a 9 para jogar:"))
            while(posicao<1 or posicao>9):
                print("Posição inválida!\n")
                posicao = int(input("Digite uma posição de 1 a 9 para jogar:"))
            jogada_valida = verifica_jogada(posicao, tabuleiro)
            print(f"Jogada válida:{jogada_valida}\n")
            while(jogada_valida == False):
                print("Posição já ocupada pelo outro jogador, escolha outra")
                posicao = int(input("Digite uma posição de 1 a 9 para jogar:"))
                while(posicao<1 or posicao>9):
                    print("Posição inválida!\n")
                    posicao = int(input("Digite uma posição de 1 a 9 para jogar:"))
                jogada_valida = verifica_jogada(posicao, tabuleiro)
            faz_jogada(posicao, tabuleiro, jogador_atual)
            ha_ganhador(tabuleiro)
        exibe_tabuleiro(tabuleiro)

def main():
    tabuleiro = [[0,0,0],[0,0,0],[0,0,0]]
    jogador_atual = 'X'
    contador = 0
    cria_tabuleiro(tabuleiro)
    print("----------------------------------------------INÍCIO DE JOGO----------------------------------------------\n\n")
    exibe_tabuleiro(tabuleiro)
    while(not(ha_ganhador(tabuleiro))):
        if (jogador_atual == 'X' or jogador_atual == 'x'):
            jogada(jogador_atual, tabuleiro, contador)
            jogador_atual = 'O'
        else:
            jogada(jogador_atual, tabuleiro, contador)
            jogador_atual = 'X'
        contador+=1
        if (empatou(contador, tabuleiro)):
            print("Empate no jogo!")
            break
        
    if (not(empatou(contador, tabuleiro))):
        if(jogador_atual == 'X'):
            print("O venceu o jogo!")
        else:
            print("X venceu o jogo")
#main()
"""
