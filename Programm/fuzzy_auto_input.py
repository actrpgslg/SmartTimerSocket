import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import time
import  datetime
import mysql.connector

def sqlupdate(Id,command,ouput):
    try :
        cnx = mysql.connector.connect(user='abc', password='1234',host='120.110.7.27',database='smarttimersocket')        
        cursor = cnx.cursor()
        #My SQL Command
        add_test = ("UPDATE `socket` SET `output` = '%s',`CommandLine`=%s WHERE `socket`.`id` = %s;")
        data_test=(output,command,Id)
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

##----------------Fuzzy Setting-----------------------------#
temp =ctrl.Antecedent(np.arange(10, 41, 1), 'temp')
light =ctrl.Antecedent(np.arange(0, 11, 1), 'light')
hum =ctrl.Antecedent(np.arange(20, 81, 1), 'hum')
switch_power = ctrl.Consequent(np.arange(0, 11, 1), 'switch_power')
temp.automf(3)
light.automf(3)
hum.automf(3)
#switch_power.automf(3)
switch_power['low'] = fuzz.trimf(switch_power.universe, [0, 0, 5])
switch_power['medium'] = fuzz.trimf(switch_power.universe, [0, 5, 10])
switch_power['high'] = fuzz.trimf(switch_power.universe, [5, 10, 10])

rule1 = ctrl.Rule(temp['good'],switch_power['high'])
rule2 = ctrl.Rule(temp['average'] | hum['good'] ,switch_power['high'])
rule3 = ctrl.Rule(temp['poor'], switch_power['low'])
rule4 = ctrl.Rule(light['poor'], switch_power['low'])
tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3,rule4])
tipping = ctrl.ControlSystemSimulation(tipping_ctrl)


#temp['average'].view()
#light['average'].view()
#hum['average'].view()
#switch_power.view()
##----------------Fuzzy End-----------------------------#

cnx = mysql.connector.connect(user='abc', password='1234',host='120.110.7.27',database='smarttimersocket')
cursor = cnx.cursor()
#My SQL Command
cursor.execute("SELECT * FROM `socket` ")
row = cursor.fetchone()
while row is not None:
    Id=row[0]
    tipping.input['temp'] = row[5]
    tipping.input['hum'] =  row[6]
    tipping.input['light'] =row[7]
    tipping.compute()
    output=float(tipping.output['switch_power'])
    print (output)
    if output >=5 :
        command='on'
        sqlupdate(Id,command,output)
    elif output<5:
        command="off"
        sqlupdate(Id,command,output)
    row = cursor.fetchone()
    
cursor.close()
cnx.close()










