#enable SPI
#sudo apt-get install python-spidev python3-spidev
#cd ~
#git clone https://github.com/lthiery/SPI-Py.git
#cd SPI-Py
#sudo python setup.py install
#sudo python3 setup.py install
#git clone https://github.com/mxgxw/MFRC522-python.git
#cd MFRC522-python

#Hardware Config
#3.3V	Grey	1	3.3V
#RST	White	22	GPIO25
#GND	Black	 6	Ground
#IRQ	–	–	Not connected
#MISO	Purple	21	GPIO9
#MOSI	Blue	19	GPIO10
#SCK	Green	23	GPIO11
#SDA	Yellow	24	GPIO8

import time
import RPi.GPIO as GPIO
import MFRC522
 
# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()
 
# Welcome message
print("Looking for cards")
print("Press Ctrl-C to stop.")
 
# This loop checks for chips. If one is near it will get the UID
try:
   
  while True:
 
    # Scan for cards
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
 
    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()
 
    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:
 
      # Print UID
      print("UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3]))
 
      time.sleep(2)
 
except KeyboardInterrupt:
  GPIO.cleanup()
