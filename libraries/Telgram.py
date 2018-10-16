sudo apt-get install python-pip3
sudo pip3 install telepot




import time, datetime
import RPi.GPIO as GPIO
import telepot
from telepot.loop import MessageLoop

white = 15
yellow = 11
red = 12
green = 13

now = datetime.datetime.now()
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
 
 
#LED White
GPIO.setup(white, GPIO.OUT)
GPIO.output(white, 0) #Off initially
#LED Yellow
GPIO.setup(yellow, GPIO.OUT)
GPIO.output(yellow, 0) #Off initially
 #LED Red
GPIO.setup(red, GPIO.OUT)
GPIO.output(red, 0) #Off initially
#LED green
GPIO.setup(green, GPIO.OUT)
GPIO.output(green, 0) #Off initially

def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print ('Received: %s' % command)

    if 'on' in command:
        message = "Turned on "
        if 'white' in command:
            message = message + "white "
            GPIO.output(white, 1)
        if 'yellow' in command:
            message = message + "yellow "
            GPIO.output(yellow, 1)
        if 'red' in command:
            message = message + "red "
            GPIO.output(red, 1)
        if 'green' in command:
            message = message + "green "
            GPIO.output(green, 1)
        if 'all' in command:
            message = message + "all "
            GPIO.output(white, 1)
            GPIO.output(yellow, 1)
            GPIO.output(red, 1)
            GPIO.output(green, 1)
        message = message + "light(s)"
        telegram_bot.sendMessage (chat_id, message)

    if 'off' in command:
        message = "Turned off "
        if 'white' in command:
            message = message + "white "
            GPIO.output(white, 0)
        if 'yellow' in command:
            message = message + "yellow "
            GPIO.output(yellow, 0)
        if 'red' in command:
            message = message + "red "
            GPIO.output(red, 0)
        if 'green' in command:
            message = message + "green "
            GPIO.output(green, 0)
        if 'all' in command:
            message = message + "all "
            GPIO.output(white, 0)
            GPIO.output(yellow, 0)
            GPIO.output(red, 0)
            GPIO.output(green, 0)
        message = message + "light(s)"
        telegram_bot.sendMessage (chat_id, message)

 

telegram_bot = telepot.Bot('tokenid')
print (telegram_bot.getMe())

MessageLoop(telegram_bot, action).run_as_thread()
print ('Up and Running....')

while 1:
    time.sleep(10)