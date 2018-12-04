from funções import *

def main(inic):
    big_bang(inic,  # Jogo
             tela=tela, frequencia=FREQUENCIA,
             quando_tick=mover_game,  # Jogo -> Jogo
             desenhar=desenha_game,  # Jogo -> Imagem
             quando_tecla= trata_tecla,
             quando_mouse=trata_mouse,  # Jogo Tecla -> Jogo
             modo_debug=False
)

main(GAME_INICIAL)