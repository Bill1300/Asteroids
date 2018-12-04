#!/usr/bin/env python
# -*- coding: utf-8 -*-

from htdp_pt_br.universe import *
import unittest
import math
import random

''' Game Asteroids '''

'''==================='''
'''# Preparacao da Tela e Constantes: '''

(LARGURA, ALTURA) = (900, 650)
tela = criar_tela_base(LARGURA, ALTURA)

#Criar/carregar imagens:

IMG_CENARIO = carregar_imagem('./imagens/cenario.jpg', LARGURA, ALTURA)
IMG_EXPLOSION = carregar_imagem('./imagens/explosion.png', 100, 100)
IMG_NAVE = carregar_imagem('./imagens/nave.png', 120, 120)
IMG_ET = carregar_imagem('./imagens/ET.png', 80, 70)
IMG_TIRO_NAVE = carregar_imagem('./imagens/tiro_nave.png', 20, 40)
IMG_TIRO_ET = carregar_imagem('./imagens/tiro_et.png', 20, 40)
IMG_ASTEROID_BIG = carregar_imagem('./imagens/asteroid2.png', 70, 70)
IMG_ASTEROID_SMALL = definir_dimensoes(IMG_ASTEROID_BIG, 35, 35)
IMG_FUNDO_GO = carregar_imagem('./imagens/gameOverImage.jpg', LARGURA, ALTURA )

#Constantes secundarias:

TIME_SPAWN = 3
FREQUENCIA = 30
X = LARGURA // 2
Y = ALTURA // 2
Z = (Y // 2) - 50

METADE_A_BIG = altura_imagem(IMG_ASTEROID_BIG) // 2
METADE_A_SMALL = altura_imagem(IMG_ASTEROID_SMALL) // 2

METADE_A_NAVE = altura_imagem(IMG_NAVE) // 2
METADE_L_NAVE = largura_imagem(IMG_NAVE) // 2

METADE_A_ET = altura_imagem(IMG_ET) // 2
METADE_L_ET = largura_imagem(IMG_ET) // 2

METADE_A_TIRO = altura_imagem(IMG_TIRO_ET) // 2
METADE_L_TIRO = largura_imagem(IMG_TIRO_ET) // 2

LIMITE_DIREITA_BIG = LARGURA - METADE_A_BIG
LIMITE_ESQUERDA_BIG = 0 + METADE_A_BIG
LIMITE_CIMA_BIG = 0 + METADE_A_BIG
LIMITE_BAIXO_BIG = ALTURA - METADE_A_BIG

LIMITE_DIREITA_SMALL = LARGURA - METADE_A_SMALL
LIMITE_ESQUERDA_SMALL = 0 + METADE_A_SMALL
LIMITE_CIMA_SMALL = 0 + METADE_A_SMALL
LIMITE_BAIXO_SMALL = ALTURA - METADE_A_SMALL


'''==================='''