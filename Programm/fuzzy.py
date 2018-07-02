import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import time
import  datetime
import matplotlib.pyplot as plt

        
##----------------Fuzzy Setting-----------------------------#
# New Antecedent/Consequent objects hold universe variables and membership
# functions
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


'''
temp['average'].view()
light['average'].view()
hum['average'].view()
switch_power.view()
tipping_ctrl.view()
#rule1.view()
#rule2.view()
#rule3.view()
#rule4.view()
'''
temp=[26,26,14,14,36,30,31,28,10,10]	
hum=[78,65,20,40,78,65,80,65,40,20]	
light=[0.2,0.2,7.46,7.01,0.7,0.7,7.5,7.2,0.2,0.2]
for i in range(0, 10):
    
    tipping.input['temp'] = temp[i]
    tipping.input['hum'] =  hum[i]
    tipping.input['light'] =light[i]
    #print (light[i])
    tipping.compute()
    output=float(tipping.output['switch_power'])
    #print ("temp= %d hum= %d light= %0.2f ouput= %0.2f" % temp[i],hum[i],light[i],output)
    print(output)


#print (tipping.output['switch_power'])
#time.sleep(400)







