#Codigo paras display LCD

import RPi.GPIO as gpio
import Adafruit_CharLCD as LCD
import time

gpio.setmode(gpio.BCM)
lcd_rs        = 25
lcd_en        = 8
lcd_d4        = 7
lcd_d5        = 12
lcd_d6        = 16
lcd_d7        = 21
lcd_backlight = 4

lcd_colunas = 16
lcd_linhas = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5,
                           lcd_d6, lcd_d7, lcd_colunas, lcd_linhas,
                           lcd_backlight)

lcd.clear()
lcd.show_cursor(True)
lcd.blink(True)
lcd.set_cursor(0,0)