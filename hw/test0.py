from machine import Pin,PWM,UART
import utime
from NetworkHelper import NetworkHelper
import time, sys
from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd


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
    ssid = "Sua" #wifi name
    pwd = "00000000" # password
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

def getApi(host, path, param=""):
    print("\r\n\r\n")
    print("Now it's time to start HTTP Get/Post Operation.......\r\n")
    # host = "192.168.1.2"  # host
    # path = "/"  # path  ?? url
    #param = ""
    if param != "":
        path = path + "?" + param
    else:
        path = path
    timeout = 0
    # default delay get api delay 3 sec
    while timeout < 3:
        httpCode, httpRes = con.doHttpGet(host, path,delay=0.5)
        print(
            "-----------------------------------------------------------------------------"
        )
        print("HTTP Code:", httpCode)
        print("HTTP Response:", httpRes)
        print(
            "-----------------------------------------------------------------------------\r\n"
        )
        if httpCode == 200:
            print("Get data successful..\r\n")
            return httpRes
            break
        else:
            print("Error")
            print("Get data fail...")
            print("Please wait to try again....\r\n")
            timeout += 1
            time.sleep(0.5)
        if timeout >= 3:
            return False

con = NetworkHelper()
wifiCon = wifi()

host = "192.168.43.92"

'''
led_green = Pin(0,Pin.OUT)
I2C_ADDR     = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16
i2c = I2C(0, sda=machine.Pin(12), scl=machine.Pin(13), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
'''
DO = Pin(3, Pin.IN)
DO1 = Pin(7, Pin.IN)
DO2 = Pin(11, Pin.IN)

count1 = 1
count2 = 1
count3 = 1

def led_on():
    led_green.high()
    utime.sleep(2)
    led_green.low()

if(wifiCon):
    while(True):
        path = "/get_stack_coin_ID"
        param = "id=1"
    if DO.value() == 0 :
        signaloff = time.sleep(0.1)
    elif DO.value() == 1 :
        print ("1 =", str(count1))
        data = getApi(host, path, param)
    if(data):
        print(data)
        count1 = count1 + 1
        
        
        
        path1 = "/get_stack_coin_ID"
        param1 = "id=2"
    if DO1.value() == 0 :
        
        signaloff = time.sleep(0.1)
    elif DO1.value() == 1 :
        print ("2 =", str(count2*5))
        data = getApi(host, path, param)
    if(data):
        print(data)
        count2 = count2 + 1
        signalon = time.sleep(0.1)
       
        

        path1 = "/get_stack_coin_ID"
        param1 = "id=3"
    if DO2.value() == 0 :
        signaloff = time.sleep(0.1)
    elif DO2.value() == 1 :
        print ("5 =", str(count3*10))
        data = getApi(host, path, param)
    if(data):
        print(data)
        count3 = count3 + 1
        signalon = time.sleep(0.1)
        
        
      
