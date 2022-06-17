from machine import Pin,PWM,UART
import utime
from NetworkHelper import NetworkHelper
import time, sys
from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

'''I2C_ADDR     = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

i2c = I2C(0, sda=machine.Pin(12), scl=machine.Pin(13), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)'''

DO = Pin(3, Pin.IN)
DO2 = Pin(7, Pin.IN)
DO1 = Pin(11, Pin.IN)

pwm = PWM(Pin(15))
buzzer = PWM(Pin(0))
led = Pin(9, Pin.OUT)
'''tones = {
"A2": 110,
"G5": 784,
"B6": 1976
}'''
count1 = 1
count2 = 1
count3 = 1


'''while True:
    buzzer.duty_u16(0)
    utime.sleep(0.5)
    buzzer.duty_u16(900000)
    utime.sleep(0.5)
    buzzer.duty_u16(0)
    
    pwm.duty_ns(MIN)
    utime.sleep(1)
    pwm.duty_ns(MID)
    utime.sleep(1.5)
    pwm.duty_ns(MAX)
    utime.sleep(1)
    
    AO.low()
    utime.sleep_us(1)
    AO.high()
    utime.sleep_us(1)
    AO.low()'''

     
while True :  
    if DO.value() == 0 :
        signaloff = time.sleep(0.1)
    elif DO.value() == 1 :
        print ("1 =", str(count1))
        count1 = count1 + 1
        led.high()
        utime.sleep(2)
        led.low()
        signalon = time.sleep(0.1)
    if DO1.value() == 0 :
        
        signaloff = time.sleep(0.1)
    elif DO1.value() == 1 :
        print ("5 =", str(count2*5))
        count2 = count2 + 1
        signalon = time.sleep(0.1)
        
    if DO2.value() == 0 :
        signaloff = time.sleep(0.1)
    elif DO2.value() == 1 :
        print ("10 =", str(count3*10))
        count3 = count3 + 1
        signalon = time.sleep(0.1)
        
def playtone(frequency):
    buzzer.duty_u16(10000)
    buzzer.freq(frequency)

def bequiet():
    buzzer.duty_u16(10)
'''
song=["B6","G5","A2"]

def playsong(mysong):
    for i in range(len(mysong)):
        if (mysong[i] == "P"):
            bequiet()
        else:
            playtone(tones[mysong[i]])
        sleep(0.3)
    bequiet()
playsong(song)
'''

def wifi():
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # print("RPi-Pico MicroPython Ver:", sys.version)
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    esp8266_at_ver = None
    print("StartUP", con.startUP())
    # print("ReStart",con.reStart())
    print("StartUP", con.startUP())
    print("Echo-Off", con.echoING())
    print("\r\n\r\n")
    esp8266_at_ver = con.getVersion()
    if esp8266_at_ver != None:
        print(esp8266_at_ver)
    con.setCurrentWiFiMode()
    print("\r\n\r\n")
    """
    Connect with the WiFi
    """
    ssid = "NFCCccc" #wifi name
    pwd = "33333333" # password
    print("Try to connect with the WiFi..")
    timeout = 0
    # default delay wifi delay 5 sec
    while timeout < 6:
        if "WIFI CONNECTED" in con.connectWiFi(ssid, pwd,delay=3):
            print("ESP8266 connect with the WiFi..")
            return True
            break
        else:
            print(".")
            timeout += 1
            time.sleep(0.5)
    if timeout >= 6:
        print("Timeout connect with the WiFi")
        return False

con = NetworkHelper()
wifiCon = wifi()

host = "192.168.236.61"
#path = "/get_stack_coin_ID_1"
#param = "stack_coin"

I2C_ADDR     = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16
i2c = I2C(0, sda=machine.Pin(12), scl=machine.Pin(13), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)


if(wifiCon):
    while(True):
        path = "/get_stack_coin_ID"
        param = "id=1"
        data = getApi(host, path, param)
        if(data):
            print(data)
        
