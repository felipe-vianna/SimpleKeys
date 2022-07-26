import RPi.GPIO as gpio
import time


botoes = []

# gpio.setmode(gpio.BCM)
botoes.append({"codigo": "0", "cor": "preto", "pino": 26})
botoes.append({"codigo": "1", "cor": "verde", "pino": 6})
botoes.append({"codigo": "2", "cor": "vermelho", "pino": 19})
botoes.append({"codigo": "3", "cor": "amarelo", "pino": 13})
botoes.append({"codigo": "4", "cor": "azul", "pino": 5})

# import os
# if os.name == 'nt':
#     from msvcrt import getche
#     def ler_botao():
#         botao = getche().decode('utf-8')
#         return botao
# else:
#     import sys
#     import tty
#     def ler_botao():
#         tty.setcbreak(sys.stdin)
#         return sys.stdin.read(1)

def ler_botao(debounce:float=0):

    while True:
        for botao in botoes:
            if (gpio.input(botao['pino']) == gpio.HIGH):
                time.sleep(debounce)
                while (gpio.input(botao['pino']) == gpio.HIGH):
                    pass
                return botao['codigo']