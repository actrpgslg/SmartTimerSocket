import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import time
import  datetime
import matplotlib.pyplot as plt

        
##----------------Fuzzy Setting-----------------------------#
# New Antecedent/Consequent objects hold universe variables and membership
# functions
sound =ctrl.Antecedent(np.arange(0, 11, 1), 'sound')
air =ctrl.Antecedent(np.arange(0, 11, 1), 'air')
#light =ctrl.Antecedent(np.arange(0, 11, 1), 'temp')
switch_power = ctrl.Consequent(np.arange(0, 11, 1), 'switch_power')
sound.automf(3)
air.automf(3)
#light.automf(3)
#switch_power.automf(3)
switch_power['low'] = fuzz.trimf(switch_power.universe, [0, 0, 5])
switch_power['medium'] = fuzz.trimf(switch_power.universe, [0, 5, 10])
switch_power['high'] = fuzz.trimf(switch_power.universe, [5, 10, 10])

rule1 = ctrl.Rule(air['good'], switch_power['high'])
rule2 = ctrl.Rule(air['average'] & sound['average'], switch_power['low'])
rule3 = ctrl.Rule(air['average'] & sound['poor']  ,switch_power['high'])
rule4 = ctrl.Rule(air['poor']  | sound['good'], switch_power['low'])
tipping_ctrl = ctrl.ControlSystem([rule1,rule2,rule3,rule4])
tipping = ctrl.ControlSystemSimulation(tipping_ctrl)
#sound['average'].view()
#air['average'].view()
#light['average'].view()
#switch_power.view()
#tipping_ctrl.view()
#rule1.view()
#rule2.view()
#rule3.view()
#rule4.view()

light=[7,2,4,6,6,2,1,8,1,1,11]	
air=  [9,6,1,4,6,9,4,1,5,5,12,10,-1,0]	
sound=[9,6,1,4,1,4,9,6,5,5,12,10,-1 ,0]
for i in range(0, 14):
    
    #tipping.input['temp'] = temp[i]
    tipping.input['air'] =  air[i]
    tipping.input['sound'] =sound[i]
    #print (light[i])
    tipping.compute()
    output=float(tipping.output['switch_power'])
    print ("air= %s sound= %s ouput= %s " % (str(air[i]),str(sound[i]),str(output)) )
    #print(output)
    #print(air[i])
    #print(sound[i])

#print (tipping.output['switch_power'])
#time.sleep(400)







