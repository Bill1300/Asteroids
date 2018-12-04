#!/usr/bin/env python
# -*- coding: utf-8 -*-

from htdp_pt_br.universe import *
from Constantes import *

'''# Definições de dados: '''


Nave = definir_estrutura("Nave", "angulo, life", mutavel= True)

'''
    Nave é: Nave(Int 0~360, 0~1) 
    Representa um angulo referente a frente da nave.
'''
#EXEMPLO

NAVE_INICIAL = Nave(0, 1)
NAVE_DIREITA = Nave(90, 1)
NAVE_BAIXO = Nave(180, 1)
NAVE_ESQUERDA = Nave(270, 1)
NAVE_MORTA = Nave(123, 1)

#TEMPLATE

'''
def fn_para_nave(nave):
    ...nave.angulo
       nave.life
    return
'''

'''==================='''

ET = definir_estrutura("ET", "x, y, angulo, dead")

'''
    ET é: ET(Int, Int, Int, Boolean)
    Representa a posição do ET no eixo X, Y e seu angulo referente ao centro e se está vivo.    
'''
#EXEMPLO

ET_INICIAL = ET(LARGURA - Z, Y, 0.1, False)
ET_MORTO = ET(675, 325, 2, True)

#TEMPLATE

'''
def fn_para_et(et):
    ...et
    return
'''

'''==================='''

Tiro_Nave = definir_estrutura("Tiro_Nave", "x, y, dx, dy, angulo")

'''
    Tiro_Nave é: Tiro_Nave(Int 0 ~ 800, Int 0 ~ 600, Int, Int)
    Representa a posição do tiro da nave e sua trajetoria.
'''
#EXEMPLO

TIRO_CIMA = Tiro_Nave(X, Y, 0, -3, 360)
TIRO_DIREITA = Tiro_Nave(X, Y, +3, 0, 90)
TIRO_BAIXO = Tiro_Nave(X, Y, 0, +3, 180)
TIRO_ESQUERDA = Tiro_Nave(X, Y, -3, 0, 270)

#TEMPLATE

'''
def fn_para_tiro_nave(tiro_nave):
    ...tiro_nave.x
    ...tiro_nave.y
    ...tiro_nave.dx
    ...tiro_nave.dy
    return
'''

'''
ListaTiroNave é um desses:
    - VAZIA
    - junta(Tiro_Nave, ListaTiroNave)
'''
#EXEMPLO

# L_TIRO_NAVE_INICIAL = criar_lista(
#     Tiro_Nave()
# )


'''===================='''

Tiro_ET = definir_estrutura("Tiro_ET", "x, y, dx, dy, trajeto")

'''
    Tiro_ET é: Tiro_ET(Int X_ET ~ X_NAVE, Int Y_ET ~ Y_NAVE, Int, Int)
    Representa a posição do tiro do ET e sua trajetoria
'''
#EXEMPLO

TIRO_ET_INICIAL = Tiro_ET(LARGURA - Z , Y, -2, 0, 270)
TIRO_ET_N = Tiro_ET(X, 100, 0, 3, 90)
TIRO_ET_O = Tiro_ET(120, Y, 3, 0, 180)
TIRO_ET_S = Tiro_ET(X, ALTURA - 100, 0, -3, 270)
Tiro_ET_L = Tiro_ET(LARGURA-120, ALTURA, -3, 0, 360)


#TEMPLATE

'''
def fn_para_tiro_et(tiro_et):
    ...tiro_et.x
    ...tiro_et.y
    ...tiro_et.dx
    ...tiro_et.dy
    return
'''

'''===================='''

Asteroid = definir_estrutura("Asteroid", "x, y, dx, dy, type", mutavel=True)

'''
    Asteroid é: Asteroid_Big(Int LIMITE_ESQUERDA_BIG ~ LIMITE_DIREITA_BIG, Int LIMITE_CIMA_BIG ~ 
                                  LIMITE_BAIXO_BIG, Int, Int, Int 0~2)
    Representa a posição do Asteroid e sua deslocação.
'''
#EXEMPLO

ASTEROID_INICIAl_RIGHT = Asteroid(LARGURA - METADE_A_BIG, random.randrange(METADE_A_BIG, ALTURA - METADE_A_BIG),
                                  random.randrange(-6, 7, 2), random.randrange(-6, 7, 2), 2)
ASTEROID_INICIAl_LEFT = Asteroid(METADE_A_BIG, random.randrange(METADE_A_BIG, ALTURA - METADE_A_BIG),
                                 random.randrange(-6, 7, 2), random.randrange(-6, 7, 2), 2)
ASTEROID_INICIAl_TOP = Asteroid(random.randrange(METADE_A_BIG, LARGURA - METADE_A_BIG), METADE_A_BIG,
                                random.randrange(-6, 7, 2), random.randrange(-6, 7, 2), 2)
ASTEROID_INICIAl_DOWN = Asteroid(random.randrange(METADE_A_BIG, LARGURA - METADE_A_BIG), ALTURA - METADE_A_BIG,
                                 random.randrange(-6, 7, 2), random.randrange(-6, 7, 2), 2)

#TEMPLATE

'''
def fn_para_asteroid_big(asteroid_big):
    ...asteroid.x
    ...asteroid.y
    ...asteroid.dx
    ...asteroid.dy
    return
'''

'''
ListaAsteroid é um desses:
    - VAZIA
    - junta(Asteroid, ListaAsteroid)
'''
#EXEMPLO
L_ASTEROID_INICIAL = [
    ASTEROID_INICIAl_TOP,
    ASTEROID_INICIAl_RIGHT,
    ASTEROID_INICIAl_DOWN,
    ASTEROID_INICIAl_LEFT
]

'''===================='''


Game = definir_estrutura("Game", "nave, et, tiro_nave, tiro_et, asteroid, score, time_spawn, game_over", mutavel=True)

'''
    Game é: Game(Nave, ET, ListaTiroNave, TiroET, ListaAsteroid, Int+, Int+, Boolean)
    Representa o todo o jogo e todas as suas ações.
'''
#EXEMPLO

GAME_INICIAL = Game(NAVE_INICIAL, ET_INICIAL, VAZIA, TIRO_ET_INICIAL,
                    VAZIA, 0, 0, False)

#TEMPLATE

'''
fn_para_game(game):
    ...game.nave
    ...game.et
    ...game.tiro...
'''

'''===================='''