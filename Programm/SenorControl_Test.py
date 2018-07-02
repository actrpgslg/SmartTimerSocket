from __future__ import print_function
from grovepi import *
from grove_rgb_lcd import *
import time
import grovepi
import  datetime
import mysql.connector
#----
# Get sensor value
    

       

#----
#---Port Setting Start----------------------------------

#---Connect Analog Port---------------------------------
#Analog Port A0~A2
sound_sensor_Port   = 0   # Connect the Sound sensor  to port A0
Air_Senor_Port      = 1   # Connect the Air sensor    to port A1
Light_Senor_Port    = 2   # Connect the Light sensor  to port A2
#-------------------------------------------------------

#---Connect Digital Port--------------------------------
#Digital Port D2~D8
DHT_Senor_Port      = 2   # Connect the DHT sensor    to port D2
Green_LED_Port      = 3   # Connect the GREEN LED     to port D3
RED_LED_Port    = 4   # Connect the RED LED       to port D4
#-------------------------------------------------------


#---Port Setting End------------------------------------

digitalWrite(Green_LED_Port,1)
#---Programm Start--------------------------------------
try:
    #---init Var-------- 
    sound_sensor=0
    Air_value=0
    Light_value=0
    temp=0
    hum=0
    
    digitalWrite(RED_LED_Port,0)
    
    grovepi.pinMode(sound_sensor_Port,"INPUT")       # Setting Sound Senor pinmode
    grovepi.pinMode(Light_Senor_Port,"INTPUT")      # Setting Light Senor pinmode        
    #---init Var End----
    time.sleep(5)
    while Light_value == 0:      
        Light_value = grovepi.analogRead(Light_Senor_Port)
    
    if    Light_value != 0:
        resistance  = (float)(1023 - Light_value) * 10 / Light_value
    else :
        resistance  = 0

    while sound_sensor == 0:      
        sound_sensor = grovepi.analogRead(sound_sensor)
    while Air_value == 0:      
        Air_value = grovepi.analogRead(Air_Senor_Port)
    
    #Temp and Hum  String
    while temp == 0:      
        [t, h] = grovepi.dht(DHT_Senor_Port,0)
        temp      = str(t)
        hum      = str(h)
    time.sleep(.5)
    light     = str(Light_value)#Light Senor   String
    resistancestr = str(resistance) # Calculate resistance of sensor in light
    Air       = str(Air_value)#Air   Senor   String
    Sound     = float(sound_sensor)#Sound Senor   String
    today     = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))    # DateTime
    
    
    add_test = ("INSERT INTO `dayrecored`"
           "(`id`, `Date`, `device`, `temp`, `hum`, `light`, `dark`,`sound`,air_quality)"
           " VALUES (NULL,%s,'RaspberryPi',%s,%s,%s,%s,%s,%s)")
    data_test = ( today,temp,hum,light,resistance,Sound,Air)
    #---My SQL Start-----------------------------------------------------------------------------------------
    #My SQL Setting
    cnx = mysql.connector.connect(user='abc', password='1234',host='120.110.7.27',database='smarttimersocket')
    cursor = cnx.cursor()
    
    #My SQL Command
    cursor.execute(add_test, data_test)
    cursor.close()
    cnx.close()
    #---My SQL End-------------------------------------------------------------------------------------------
    #---View Print Variors-----------------------------------------------------------------------------------
    print("---------------------------------------------------")
    print("DateTime=%s" %today)
    print("Temp=%s Hum=%s" % (temp,hum) )
    print("light=%s resistancestr=%s" % (light,resistancestr) )
    print("Air Value=%s " % Air)
    print("Sound Value=%d " % Sound)
    print("---------------------------------------------------")
    print("SQL------------------------------------------------")
    print(add_test % data_test)
    print("")
    #---View Print Variors-----------------------------------------------------------------------------------
except (IOError, TypeError) as e:
    print ("IOError TypeError:"+str(e))
    #print (e)
except Exception as e:
    print("Error:"+str(e))
    print("Error:"+str(e))
    f = open('recored.txt','r+')
    a=(add_test % data_test)+'\n'
    print(f.read()+str(a))
    f.write(f.read()+str(a))
    f.close()
finally :
    print ("Finsh")
#---Programm End--------------------------------------
    time.sleep(10)
