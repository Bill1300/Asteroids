import unittest
from Main import *

class Test(unittest.TestCase):

    def test_angulo_tiro_nave(self):
        self.assertEqual(angulo_tiro_nave(13), Tiro_Nave(X, Y, 0, -9, 13))
        self.assertEqual(angulo_tiro_nave(-60), Tiro_Nave(X, Y, 6, -6, -60))
        self.assertEqual(angulo_tiro_nave(30), Tiro_Nave(X, Y, -6, -6, 30))
        self.assertEqual(angulo_tiro_nave(110), Tiro_Nave(X, Y, 9, 0, 110))
        self.assertEqual(angulo_tiro_nave(120), Tiro_Nave(X, Y, -6, 6, 120))
        self.assertEqual(angulo_tiro_nave(200), Tiro_Nave(X, Y, 0, 9, 200))
        self.assertEqual(angulo_tiro_nave(240), Tiro_Nave(X, Y, 6, 6, 240))
        self.assertEqual(angulo_tiro_nave(247), Tiro_Nave(X, Y, 9, 0, 247))

    def test_trata_tecla(self):
        self.assertEqual(trata_tecla(game, pg.K_RETURN), criar_jogo_inicial())
        self.assertEqual(trata_tecla(game, pg.K_SPACE), game)

    def test_cria_jogo_inicial(self):
        self.assertEqual(criar_jogo_inicial(),Game(Nave(0, 1), ET_INICIAL, VAZIA, TIRO_ET_INICIAL, VAZIA, 0, 0, False))

    def test_mexe_et(self):
        self.assertEqual(mexe_et(True), ET(et.x, et.y, et.angulo, True))
        self.assertEqual(mexe_et(False), ET(novo_x // 1, novo_y // 1, et.angulo + 0.04, False))

    def test_mexe_asteroid(self):
        self.assertEqual(mexe_asteroid(asteroid(5, 5, 5, 5, type)),Asteroid(5, 5, 5, -5, asteroid.type))
        self.assertEqual(mexe_asteroid(asteroid(900, 900, 900, 900, type)), Asteroid(900, 900, -900, 900, asteroid.type))

    def test_move_tiro_nave(self):
        self.assertEqual(move_tiro_nave(tiro(10, 10, 10, 10, type)),Tiro_Nave(20, 20, 10, 10, tiro.angulo))

    def test_calcula_angulo(self):
        self.assertEqual(calcular_angulo(50, 125),2.0018275505)

    def test_gera_tiro_nave(self):
        self.assertEqual(gera_tiro_nave(game, 50, 400),Game(game.nave, game.et, -8.05239667779, game.tiro_et,\
                                                            game.asteroid, game.score, game.time_spawn, game.game_over))

        self.assertEqual(gera_tiro_nave(game, 50, 125),Game(game.nave, game.et, 182.0018275505, game.tiro_et,\
                                                            game.asteroid, game.score, game.time_spawn, game.game_over))

    def test_trata_mouse(self):
        self.assertEqual(trata_mouse(game, 50, 400, 4), Game(Nave(novo_angulo // 1 + 180, game.nave.life), game.et,\
                                                             game.tiro_nave, game.tiro_et, game.asteroid, game.score,\
                                                             game.time_spawn, game.game_over))

        self.assertEqual(trata_tecla(game, 50, 125, 4), Game(Nave(novo_angulo // 1, game.nave.life), game.et,\
                                                          game.tiro_nave, game.tiro_et,game.asteroid, game.score,\
                                                          game.time_spawn, game.game_over))

        self.assertEqual(trata_tecla(game, 450, 325, 4),Game(Nave(game.nave.angulo // 1, game.nave.life), game.et,\
                                                          game.tiro_nave, game.tiro_et, game.asteroid, game.score,\
                                                          game.time_spawn, game.game_over))

        self.assertEqual(trata_tecla(game, 50, 125, 5),2.0018275505)
        self.assertEqual(trata_tecla(game,x, y, 1),Game(game.nave, game.et, game.tiro_nave, game.tiro_et, game.asteroid, game.score, game.time_spawn, game.game_over))

    def test_colide_asteroid(self):
        self.assertEqual(colide_asteroid(asteroid1(70, 70, dx, dy, type), asteroid2(70, 70, dx, dy, type)), \
                         direita_asteroid1 >= esquerda_asteroid2 and \
                         esquerda_asteroid1 <= direita_asteroid2 and \
                         baixo_asteroid1 >= cima_asteroid2 and \
                         cima_asteroid1 <= baixo_asteroid2
                         )
    def test_colide_tiro_nave_asteroid(self):#HELP
        self.assertEqual(colide_tiro_nave_asteroid(tiro(x, y, dx, dy, type), asteroid(x, y, dx, dy, type)),\
                         )

    def test_colide_nave_ET(self):
        self.assertEqual((tiro(50, 50, dx, dy, type), et(50, 50, dx, dy, type)),direita_tiro >= esquerda_et and \
                         esquerda_tiro <= direita_et and baixo_tiro >= cima_et and cima_tiro <= baixo_et)

    def test_colide_tiro_et(self):#HELP
        self.assertEqual(colide_tiros_nave_et(tiro(x, y, dx, dy, type),et(x, y, dx, dy, type)),False)



