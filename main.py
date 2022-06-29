import telegram_send
from arvore import arvore

import os
if os.name == 'nt':
    from msvcrt import getche
    def ler_botao():
        botao = getche().decode('utf-8')
        return botao
else:
    import sys
    import tty
    def ler_botao():
        tty.setcbreak(sys.stdin)
        return sys.stdin.read(1)

comandos = ['del', 'snd', 'rst', 'spc']

def enviar(msg):
    telegram_send.send(messages=[msg])
    print("Mensagem enviada!")

# def ler_botao():
#     return input()

def ler_comando(cmd, msg):
    if cmd == 'del':
        return msg[:-1]

    if cmd == 'snd':
        enviar(msg)
        return ""

    if cmd == 'rst':
        return ""
    
    if cmd == 'spc':
        return msg + ' '

msg = ""
# botoes = ''
subset = arvore
while True:
    print(f'msg: {msg}')
    print('> ', end='', flush=True)
    while not isinstance(subset, str):
        botao = ler_botao()
        subset = subset[botao]
    print()
    if subset in comandos:
        msg = ler_comando(cmd=subset, msg=msg)
        print('-', subset)
    else:
        msg += subset
    print()
    subset = arvore
    