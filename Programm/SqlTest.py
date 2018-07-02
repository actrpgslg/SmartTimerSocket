import mysql.connector
def sqlinsert(command,temp,hum,light):
    try :
        senddevice='RaspberryPi3'
        device='BT_UART_2281'
        macaddress='C1:8F:CC:DC:57:19'
        today=str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        cnx = mysql.connector.connect(user='abc', password='1234',host='120.110.7.25',database='smarttimersocket')
        
        cursor = cnx.cursor()
          
        #My SQL Command
        add_test = ("INSERT INTO `socket`"
                   "(`id`, `Senddevice`, `Device`, `DeviceMacAddress`, `CommandLine`, `Date`, `temp`,`hum`,`light`)"
                   "VALUES"
                   "(NULL, %s, %s, %s,%s, %s,%s,%s,%s);")
        data_test=(senddevice,device,macaddress,command,today,temp,hum,light)
        cursor.execute(add_test, data_test)
        cnx.commit()
        cursor.close()
        cnx.close()
    except (IOError, TypeError) as e:
        print ("IOError TypeError:"+str(e))
    except Exception as e:
        print("Error:"+str(e))
    finally :
        return command
def sqlget():
    try :
        cnx = mysql.connector.connect(user='abc', password='1234',host='120.110.7.25',database='smarttimersocket')
        cursor = cnx.cursor()
        #My SQL Command
        cursor.execute("SELECT * FROM `socket` ORDER BY `socket`.`id` DESC LIMIT 0,1")
        row=cursor.fetchone()
        cursor.close()
        cnx.close()
        return row[4]
    except (IOError, TypeError) as e:
        print ("IOError TypeError:"+str(e))
    except Exception as e:
        print("Error:"+str(e))
def sqlauto(deviceid):
    try :
        deviceid=str(deviceid)
        cnx = mysql.connector.connect(user='abc', password='1234',host='120.110.7.27',database='smarttimersocket')
        cursor = cnx.cursor()
        #My SQL Command
        cursor.execute("SELECT * FROM `device_switch` WHERE `id`="+deviceid)
        row=cursor.fetchone()
        cursor.close()
        cnx.close()
        return int(row[3])
    except (IOError, TypeError) as e:
        print ("IOError TypeError:"+str(e))
    except Exception as e:
        print("Error:"+str(e))
            
try :
    cnx = mysql.connector.connect(user='abc', password='1234',host='120.110.7.25',database='smarttimersocket')
    cursor = cnx.cursor()
       #My SQL Command
    cursor.execute("INSERT INTO `test` (`id`, `device`) VALUES (NULL, '1234');")
    row = cursor.fetchone()
    print (row)
except (IOError, TypeError) as e:
    print ("IOError TypeError:"+str(e))
except Exception as e:
    print("Error:"+str(e))
    f = open('file.txt','w')
    a = input('is python good?')
    f.write('answer:'+str(a))
    f.close()
finally :
    print("Finall")