import pygame, sys, math
from pygame.locals import *

TELA_LARGURA = 800
TELA_ALTURA = 600
FPS = 60

ORIGEM_X = 60
ORIGEM_Y = TELA_ALTURA - 150
PASSARO_RAIO = 10

BRANCO = (255, 255, 255)
VERMELHO = (192, 0, 0)
VERMELHO_ESCURO = (64, 0, 0)
AZUL_CLARO = (176, 224, 250)
VERDE_ESCURO = (34, 139, 34)
VERDE_CLARO = (50, 205, 50)

G = 9.81
FATOR_ESCALA = 20

ESTADO_ESPERA = 0
ESTADO_MOVIMENTO = 1
ESTADO_PAUSA = 2
ESTADO_FIM = 9
PASSARO_CENTRO_X = 60
PASSARO_CENTRO_Y = 450


def main():
    v_zero = float(input("Informe a velocidade inicial (m/s) : "))
    angulo_graus = float(input("Informe o ângulo do lançamento (graus): "))

    global TELA

    pygame.init()
    fps_relogio = pygame.time.Clock()
    TELA = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA), 0, 32)

    pygame.display.set_caption("Angry Ballistics : Red Bird")

    estado = ESTADO_ESPERA

    while True:

        estado = verificar_entradas(estado)

        if estado == ESTADO_ESPERA:
            x, x_zero, y, v, t = (0.0, 0.0, 0.0, v_zero, 0.0)
            x_tela, y_tela = (PASSARO_CENTRO_X, PASSARO_CENTRO_Y)
        elif estado == ESTADO_MOVIMENTO:
            x, x_zero, y, v, t = calcular_movimento(x, x_zero, y, v, t, angulo_graus)
            x_tela, y_tela = cartesiano_para_tela(x, y)
            if v <= 0.5:
                estado = ESTADO_FIM

        desenhar_cenario()
        desenhar_passaro(x_tela, y_tela)

        pygame.display.update()
        fps_relogio.tick(FPS)


def verificar_entradas(estado):
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONUP or (event.type == KEYUP and (event.key == K_SPACE or event.key == K_RETURN)):
            if estado == ESTADO_ESPERA or estado == ESTADO_PAUSA:
                estado = ESTADO_MOVIMENTO
            elif estado == ESTADO_MOVIMENTO:
                estado = ESTADO_PAUSA
            elif estado == ESTADO_FIM:
                estado = ESTADO_ESPERA
    return estado


def calcular_movimento(x, x_zero, y, v, t, angulo_graus):
    angulo_rad = angulo_graus * (math.pi / 180)
    t += (1 / float(FPS))
    x = x_zero + v * math.cos(angulo_rad) * t
    y = v * math.sin(angulo_rad) * t - (G * t ** 2) / 2
    if y <= 0.0 and t > 0.0:
        v *= 0.6
        x_zero = x
        y, t = (0.0, 0.0)
    return (x, x_zero, y, v, t)


def cartesiano_para_tela(x, y):
    x_tela = int(ORIGEM_X + FATOR_ESCALA * x)
    y_tela = int(ORIGEM_Y - FATOR_ESCALA * y)
    return (x_tela, y_tela)


def desenhar_cenario():
    TELA.fill(AZUL_CLARO)
    pygame.draw.rect(TELA, VERDE_CLARO, (0, ORIGEM_Y + PASSARO_RAIO, TELA_LARGURA, ORIGEM_Y + PASSARO_RAIO + 6), 0)
    pygame.draw.rect(TELA, VERDE_ESCURO, (0, ORIGEM_Y + PASSARO_RAIO + 6, TELA_LARGURA, TELA_ALTURA), 0)


def desenhar_passaro(x, y):
    pygame.draw.circle(TELA, VERMELHO_ESCURO, (x, y), PASSARO_RAIO)
    pygame.draw.circle(TELA, VERMELHO, (x, y), PASSARO_RAIO - 2)
    pygame.draw.circle(TELA, BRANCO, (x, y), 2)


if __name__ == '__main__':
    main()
    verificar_entradas(estado)
    calcular_movimento(x, x_zero, y, v, t, angulo_graus)
    cartesiano_para_tela(x, y)
    desenhar_cenario()