import telegram_send
from arvore import arvore
from display import lcd
from botoes import botoes, ler_botao
import time
import RPi.GPIO as gpio 


gpio.setmode(gpio.BCM)

debounce_delay = 0.15 # delay em segundos

for botao in botoes:
    gpio.setup(botao['pino'], gpio.IN, gpio.PUD_DOWN)


comandos = ['del', 'snd', 'rst', 'spc']

def enviar(msg):
    try:
        telegram_send.send(messages=[msg])
        print("Mensagem enviada!")
    except:
        print("Aviso: nao foi possivel se comunicar com o Telegram")


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
seq_botoes = ""
subset = arvore
while True:
    print(f'msg: {msg}')
    print('> ', end='', flush=True)
    while not isinstance(subset, str):
        lcd.set_cursor(0,1)
        lcd.message(f">{seq_botoes}")
        botao = ler_botao(debounce=debounce_delay)
        print(botao, end='', flush=True)
        subset = subset[str(botao)]
        seq_botoes += str(botao)
    print()
    if subset in comandos:
        print('-', subset)
        msg = ler_comando(cmd=subset, msg=msg)
    else:
        msg += subset
    lcd.clear()
    lcd.set_cursor(0,0)
    if len(msg) > 16:
        lcd.message(msg[-16:])
    else:
        lcd.message(msg)
    print()
    subset = arvore
    seq_botoes = ""
    