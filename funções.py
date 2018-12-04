#!/usr/bin/env python
# -*- coding: utf-8 -*-

from htdp_pt_br.universe import *
from Constantes import *
from Definição_dados import *
import unittest
import math
import random

''' Game Asteroids '''

'''==================='''


''' Funções: '''

'''
criar_jogo_inicial: -> game
Cria um jogo novo.
'''
def criar_jogo_inicial():
    return Game(Nave(0, 1), ET_INICIAL, VAZIA, TIRO_ET_INICIAL,
                    VAZIA, 0, 0, False)


'''
trata_tecla: game, tecla -> game
Altera o game de acordo com a tecla usada.
'''
##
def trata_tecla(game, tecla):
    if (not game.game_over):
        return game
    elif tecla == pg.K_RETURN:
        return criar_jogo_inicial()
    else:
        return game

'''
mexe_et: et -> et
Recebe os dados do et e retorna sua nova instancia.
'''
##
def mexe_et(et):
    if (not et.dead):
        novo_x = X + math.cos(et.angulo)* 290
        novo_y = Y + math.sin(et.angulo)* 290
        return ET(novo_x // 1, novo_y // 1, et.angulo + 0.04, False)
    return ET(et.x, et.y, et.angulo, True)


''' 
mexe_asteroid: asteroid -> asteroid
Recebe os dados do asteroid e o posiciona na nova instancia.
'''
##
def mexe_asteroid(asteroid):
    posicao_x_futura = asteroid.x + asteroid.dx
    posicao_y_futura = asteroid.y + asteroid.dy

    if posicao_x_futura > LIMITE_DIREITA_BIG or posicao_x_futura < LIMITE_ESQUERDA_BIG:
        return Asteroid(asteroid.x, asteroid.y, -asteroid.dx, asteroid.dy, asteroid.type)

    elif posicao_y_futura > LIMITE_BAIXO_BIG or posicao_y_futura < LIMITE_CIMA_BIG:
        return Asteroid(asteroid.x, asteroid.y, asteroid.dx, -asteroid.dy, asteroid.type)

    return Asteroid(posicao_x_futura, posicao_y_futura, asteroid.dx, asteroid.dy, asteroid.type)


'''
move_tiro_nave: tiro_nave -> tiro_nave
Recebe um tiro e o move.
'''
##
def move_tiro_nave(tiro):
    futuro_x = tiro.x + tiro.dx
    futuro_y = tiro.y + tiro.dy
    return Tiro_Nave(futuro_x, futuro_y, tiro.dx, tiro.dy, tiro.angulo)


'''
move_tiros_nave: ListaDeTiro -> ListaDeTiro
Recebe uma lista de tiro e os faz mover
'''
##
def move_tiros_nave(tiros):
    return criar_lista([move_tiro_nave(tiro) for tiro in tiros])


'''
angulo_tiro_nave: angulo -> Tiro_nave
recebe o angulo da nave e devolve a trajetoria q tiro vai percorrer
'''
def angulo_tiro_nave(angulo):
    if angulo < 22 and angulo > -22:
        return Tiro_Nave(X, Y, 0, -9, angulo)
    elif angulo > -67 and angulo < -22:
        return Tiro_Nave(X, Y, 6, -6, angulo)
    elif angulo > 22 and angulo < 57:
        return Tiro_Nave(X, Y, -6, -6, angulo)
    elif angulo > 57 and angulo < 113:
        return Tiro_Nave(X, Y, -9, 0, angulo)
    elif angulo > 113 and angulo < 157:
        return Tiro_Nave(X, Y, -6, 6, angulo)
    elif angulo > 157 and angulo < 203:
        return Tiro_Nave(X, Y, 0, 9, angulo)
    elif angulo > 203 and angulo < 247:
        return Tiro_Nave(X, Y, 6, 6, angulo)
    elif angulo <= -67 or angulo >= 247:
        return Tiro_Nave(X, Y, 9, 0, angulo)


'''
calcula_angulo: x, y -> angulo
Recebe um valor x e um y e calcula o angulo em relação a posição
'''
##
def calcula_angulo(x, y):
    calc = (X - x) / (Y - y)#450 325
    novo_angulo = (180 * math.atan(calc)) / 3.1415926535
    return novo_angulo


'''
gera_tiro_nave: game, x, y -> game
Recebe o jogo e a cordenadas do mouse para direcionar o tiro.
'''
##
def gera_tiro_nave(game, x, y):
    if y > Y:
        novo_angulo = calcula_angulo(x, y) + 180
        novo_tiro = angulo_tiro_nave(novo_angulo)
        tiro_final = juntar(novo_tiro, game.tiro_nave)
        return Game(game.nave, game.et, tiro_final, game.tiro_et, game.asteroid,
                    game.score, game.time_spawn, game.game_over)
    novo_angulo = calcula_angulo(x, y)
    novo_tiro = angulo_tiro_nave(novo_angulo)
    tiro_final = juntar(novo_tiro, game.tiro_nave)
    return Game(game.nave, game.et, tiro_final, game.tiro_et, game.asteroid,
                game.score, game.time_spawn, game.game_over)


'''
trata_mouse: game, x, y, ev -> game
Recebe as posições e um evento do mouse e retorna um novo mundo com um angulo alterado.
'''
##
def trata_mouse(game, x, y, ev):
    if ev == pg.MOUSEMOTION:
        if x != X and y != Y:
            if y > Y:
                novo_angulo = calcula_angulo(x, y)
                return Game(Nave(novo_angulo // 1 + 180, game.nave.life), game.et, game.tiro_nave, game.tiro_et,
                            game.asteroid, game.score, game.time_spawn, game.game_over)
            novo_angulo = calcula_angulo(x, y)
            return Game(Nave(novo_angulo // 1, game.nave.life), game.et, game.tiro_nave, game.tiro_et,
                            game.asteroid, game.score, game.time_spawn, game.game_over)
        return Game(Nave(game.nave.angulo // 1, game.nave.life), game.et, game.tiro_nave, game.tiro_et, game.asteroid,
                    game.score, game.time_spawn, game.game_over)
    if ev == pg.MOUSEBUTTONDOWN:
        game_com_tiro = gera_tiro_nave(game, x, y)
        return game_com_tiro
    return Game(game.nave, game.et, game.tiro_nave, game.tiro_et, game.asteroid,
                game.score, game.time_spawn, game.game_over)


'''
mover_asteroids: ListaDeAsteroids -> ListaDeAsteroids
Recebe uma lista de asteroids e retorna uma nova.
'''
##
def mover_asteroids(asteroids):
    return criar_lista([mexe_asteroid(asteroid) for asteroid in asteroids])


'''
next_asteroid: -> ListaDeAsteroids
Retorna um novo asteroid aleatorio de uma lista pré definida.
'''
def next_asteroid():
    return L_ASTEROID_INICIAL[random.randrange(0,4)]


'''
vira_asteroid: asteroid1, asteroid2 -> 
Muda a trajetoria de dois asteroids
'''
def vira_asteroid(asteroid1, asteroid2):
    if asteroid1.dx >= 0:
        asteroid1.dx = -asteroid1.dx
        asteroid1.x -= 1
    else:
        asteroid1.dx = +asteroid1.dx
        asteroid1.x += 1
    if asteroid1.dy >= 0:
        asteroid1.dy = -asteroid1.dy
        asteroid1.y -= 1
    else:
        asteroid1.dy = +asteroid1.dy
        asteroid1.y += 1
    if asteroid2.dx >= 0:
        asteroid2.dx = -asteroid2.dx
        asteroid2.x -= 1
    else:
        asteroid2.dx = +asteroid2.dy
        asteroid2.x += 1
    if asteroid2.dy >= 0:
        asteroid2.dy = -asteroid2.dy
        asteroid2.y -= 1
    else:
        asteroid2.dy = +asteroid2.dy
        asteroid2.y += 1


'''
colide_asteroid: asteroid, asteroid -> Boolean
Checka se algum asteroid colidiu com um outro.
'''
##
def colide_asteroid(asteroid1, asteroid2):
    esquerda_asteroid1 = asteroid1.x - (METADE_A_BIG - 10)
    direita_asteroid1 = asteroid1.x + (METADE_A_BIG - 10)
    cima_asteroid1 = asteroid1.y - (METADE_A_BIG - 10)
    baixo_asteroid1 = asteroid1.y + (METADE_A_BIG - 10)

    esquerda_asteroid2 = asteroid2.x - (METADE_A_BIG - 10)
    direita_asteroid2 = asteroid2.x + (METADE_A_BIG - 10)
    cima_asteroid2 = asteroid2.y - (METADE_A_BIG - 10)
    baixo_asteroid2 = asteroid2.y + (METADE_A_BIG - 10)

    return direita_asteroid1 >= esquerda_asteroid2 and \
           esquerda_asteroid1 <= direita_asteroid2 and \
           baixo_asteroid1 >= cima_asteroid2 and \
           cima_asteroid1 <= baixo_asteroid2


'''
colide_asteroid_asteroid: ListaDeAsteroid -> 
Testa se algum a
def next_asteroid():steroid bateu sem sim eles mudam de trajetoria.
'''
##
def colide_asteroid_asteroid(asteroids):
    for asteroid1 in asteroids:
        for asteroid2 in asteroids:
            if asteroid1 != asteroid2 and colide_asteroid(asteroid1, asteroid2):
                vira_asteroid(asteroid1,asteroid2)



'''
colide_nave: asteroid -> Boolean
Checka se algum asteroid bateu na nave.
'''
##
def colide_nave(asteroid):
    esquerda_nave = X - (METADE_L_NAVE - 15)
    direita_nave = X + (METADE_L_NAVE - 15)
    cima_nave = Y - (METADE_A_NAVE - 15)
    baixo_nave = Y + (METADE_A_NAVE - 15)

    esquerda_asteroid = asteroid.x - (METADE_A_BIG - 15)
    direita_asteroid = asteroid.x + (METADE_A_BIG - 15)
    cima_asteroid = asteroid.y - (METADE_A_BIG - 15)
    baixo_asteroid = asteroid.y + (METADE_A_BIG - 15)

    return direita_nave >= esquerda_asteroid and \
        esquerda_nave <= direita_asteroid and \
        baixo_nave >= cima_asteroid and \
        cima_nave <= baixo_asteroid

'''
colide_nave_asteroid: nave, ListaDeAsteroid -> Boolean
Checka se algum asteroid colidiu com a nave.
'''
##
def colide_nave_asteroid(asteroids):
    for asteroid in asteroids:
        if colide_nave(asteroid):
            return True
    return False


'''
colide_tiro_nave_asteroid: tiro_nave -> Boolean
Check se um tiro bate em um asteroid.
'''
##
def colide_tiro_nave_asteroid(tiro, asteroid):
    esquerda_tiro = tiro.x - METADE_L_TIRO
    direita_tiro = tiro.x + METADE_L_TIRO
    cima_tiro = tiro.y - METADE_A_TIRO
    baixo_tiro = tiro.y + METADE_A_TIRO

    esquerda_asteroid = asteroid.x - METADE_A_BIG
    direita_asteroid = asteroid.x + METADE_A_BIG
    cima_asteroid = asteroid.y - METADE_A_BIG
    baixo_asteroid = asteroid.y + METADE_A_BIG

    if direita_tiro >= esquerda_asteroid and esquerda_tiro <= direita_asteroid and \
            baixo_tiro >= cima_asteroid and cima_tiro <= baixo_asteroid:
        return asteroid
    return False


'''
colisao_asteroid_score: game ->
Check se ocorreu alguma colisão com asteroid para contabilizar.
'''
##
def colisao_asteroid_score(game):
    for asteroid in game.asteroid:
        for tiro in game.tiro_nave:
            if colide_tiro_nave_asteroid(tiro,asteroid):
                game.score += 10


'''
colisao_et_score: game ->
Checka se ocorreu alguma colisão com um Et e contabiliza
'''
def colisao_et_score(game):
    for tiro in game.tiro_nave:
        if colide_tiro_nave_ET(tiro, game.et):
            game.score += 25
        pass

'''
colide_tiros_nave_asteroids: ListaDeTirosNave, ListaDeAsteroids -> 
Checka se algum tiro acertou e remove o asteroid da lista.
'''
##
def colide_tiros_nave_asteroids(tiros, asteroids):
    for asteroid in asteroids:
        for tiro in tiros:
            if colide_tiro_nave_asteroid(tiro,asteroid):
                asteroid_destruido = colide_tiro_nave_asteroid(tiro, asteroid)
                lista_sem_1_asteroid = asteroids.remove(asteroid_destruido)
                return lista_sem_1_asteroid
    return asteroids


'''
colide_tiro_nave_ET: tiro, et -> Boolean
Ckeck se um tiro bate no ET e retorna um boolean.
'''
##
def colide_tiro_nave_ET(tiro, et):#20
    esquerda_tiro = tiro.x - METADE_L_TIRO
    direita_tiro = tiro.x + METADE_L_TIRO
    cima_tiro = tiro.y - METADE_A_TIRO
    baixo_tiro = tiro.y + METADE_A_TIRO

    esquerda_et = et.x - METADE_A_ET
    direita_et = et.x + METADE_A_ET
    cima_et = et.y - METADE_A_ET
    baixo_et = et.y + METADE_A_ET

    return direita_tiro >= esquerda_et and \
           esquerda_tiro <= direita_et and \
           baixo_tiro >= cima_et and \
           cima_tiro <= baixo_et


'''
colide_tiros_nave_et: ListaDeTirosNave, ET -> ET
Checka se algum tiro acertou o ET e o destruiu.
'''
##
def colide_tiros_nave_et(tiros, et):
    for tiro in tiros:
        if colide_tiro_nave_ET(tiro, et):
            return ET(et.x, et.y, et.angulo, True)
    return et

'''
mover_game: game -> game
Recebe o jogo e cria seu proximo estado.
'''
def mover_game(game):
    if (colide_nave_asteroid(game.asteroid)):
         game.nave.life -= 1
    if game.nave.life > 0:
        colisao_asteroid_score(game)
        colisao_et_score(game)
        asteroid_possivel = colide_tiros_nave_asteroids(game.tiro_nave, game.asteroid)
        colide_asteroid_asteroid(asteroid_possivel)
        if (not game.et.dead):
            possivel_et = colide_tiros_nave_et(game.tiro_nave, game.et)
            novo_et = mexe_et(possivel_et)
        else:
            novo_et = game.et
        novo_tiro_nave = move_tiros_nave(game.tiro_nave)
        # novo_tiro_et = et_atira(game)
        # tiro_et_final = move_tiro_et(novo_tiro_et)
        novo_asteroid = mover_asteroids(asteroid_possivel)
        novo_time_spawn = game.time_spawn +1
        if novo_time_spawn >= TIME_SPAWN * FREQUENCIA:
            if game.et.dead:
                novo_et = ET_INICIAL
            else:
                novo_et = game.et
            asteroids_final = juntar(next_asteroid(),novo_asteroid)
            novo_time_spawn = 0
            return Game(game.nave, novo_et, novo_tiro_nave, game.tiro_et, asteroids_final,
                        game.score, novo_time_spawn, False)
        return Game(game.nave, novo_et, novo_tiro_nave, game.tiro_et,
                    novo_asteroid, game.score, novo_time_spawn, False)
    return Game(game.nave, game.et, game.tiro_nave, game.tiro_et,
                    game.asteroid, game.score, game.time_spawn, True)

'''
desenha_et: et -> imagem
Recebe a posição do et e o desenha na tela.
'''
def desenha_et(et):
    colocar_imagem(IMG_ET, tela, et.x, et.y)


'''
desenha_posicao: nave -> imagem
Recebe o angulo da nave e gira a imagem 
'''
def desenha_posicao(nave):
    colocar_imagem(girar(IMG_NAVE, nave.angulo), tela, X, Y)


'''
desenha_asteroid_big: asteroid_big -> imagem
Recebe a posição do asteroid grande e o desenha na tela.
'''
def desenha_asteroid_big(asteroid):
    colocar_imagem(IMG_ASTEROID_BIG, tela, asteroid.x, asteroid.y)


'''
desenha_asteroid_big: asteroid_small -> imagem
Recebe a posição do asteroid pequeno e o desenha na tela.
'''
def desenha_asteroid_small(asteroid):
    colocar_imagem(IMG_ASTEROID_SMALL, tela, asteroid.x, asteroid.y)


'''
desenha_asteroids_big: ListaAsteroids -> imagem
Desenha todos os asteroids.
'''
def desenha_asteroids_big(asteroids):
    for asteroid in asteroids:
        desenha_asteroid_big(asteroid)


'''
desenha_tiro_et: tiro_et -> imagem
Recebe os dados do tiro do et e o desenha.
'''
def desenha_tiro_et(tiro):
    colocar_imagem(girar(IMG_TIRO_ET, tiro.trajeto), tela, tiro.x, tiro.y)


'''
desenha_tiro_nave: tiro_nave -> imagem
Recebe os dados do tiro da nave e o desenha.
'''
def desenha_tiro_nave(tiro):
    colocar_imagem(girar(IMG_TIRO_NAVE, tiro.angulo), tela, tiro.x, tiro.y)


'''
desenha_tiros_nave: ListaDeTiros -> imagem
'''
def desenha_tiros_nave(tiros):
    for tiro in tiros:
        desenha_tiro_nave(tiro)

'''
desenha_game_over: -> Imagem
Desenha a tela do game over.
'''
def desenha_game_over():
    texto_game_over = texto("GAME OVER", Fonte("impact", 50), Cor("black"))
    colocar_imagem(texto_game_over, tela, LARGURA//2, ALTURA//2)

'''
desenha_restart: -> Imagem
Desenha a tela do game over.
'''
def desenha_restart():
    texto_restart = texto("CLIQUE ENTER PARA RECOMEÇAR", Fonte("impact", 25), Cor("black"))
    colocar_imagem(texto_restart, tela, X, Y + 60)

'''
desenha_score_game_over: game -> Imagem
Desenha o score da sessão.
'''
def desenha_score_game_over(game):
    str_score = "SCORE {0}".format(game.score)
    texto_score = texto(str_score, Fonte("impact", 50), Cor("black"))
    colocar_imagem(texto_score, tela, LARGURA//2, ALTURA//2 +30)

'''
desenha_restart_game_over: game -> Imagem
Desenha o mensagem.
'''
def desenha_score_game_over(game):
    str_score = "SCORE {0}".format(game.score)
    texto_score = texto(str_score, Fonte("impact", 50), Cor("black"))
    colocar_imagem(texto_score, tela, LARGURA//2, ALTURA//2 +30)

'''
desenha_score: score -> imagem
Desenha o score na tela.
'''
def desenha_score(score):
    str_score = "SCORE {0}".format(score)
    texto_score = texto(str_score, Fonte("impact", 30), Cor("white"))
    colocar_imagem(texto_score, tela, 800, 40)


'''
desenha_explosão: x, y -> imagem
Desenha a explosão dos inimigos.
'''
def desenha_explosao(x, y):
    colocar_imagem(IMG_EXPLOSION, tela, x, y)


'''
explosão_asteroid: 
'''
def explosao_asteroid(tiros, asteroids):
    for asteroid in asteroids:
        for tiro in tiros:
            if colide_tiro_nave_asteroid(tiro,asteroid):
                desenha_explosao(asteroid.x,asteroid.y)


'''
desenhq_cenario_game_over: -> imagem
Desenha  o fundo do game over
'''
def desenha_cenario_game_over():
    colocar_imagem(IMG_FUNDO_GO, tela, X, Y)


'''
desenha_cenario: -> imagem
Desenha o cenario de fundo
'''
def desenha_cenario():
    colocar_imagem(IMG_CENARIO, tela, X, Y)

'''
desenha_game: game -> imagens
Recebe as informações do game e retorna todas as imagena.
'''
def desenha_game(game):
    if (not game.game_over):
        desenha_cenario()
        desenha_posicao(game.nave)
        # desenha_tiro_et(game.tiro_et)
        desenha_asteroids_big(game.asteroid)
        desenha_tiros_nave(game.tiro_nave)
        explosao_asteroid(game.tiro_nave, game.asteroid)
        desenha_score(game.score)
        if (not game.et.dead):
            desenha_et(game.et)
    else:
        desenha_cenario_game_over()
        desenha_game_over()
        desenha_restart()
        desenha_score_game_over(game)

''' ================= '''


