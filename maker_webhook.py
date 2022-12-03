import requests
import time

class MakerTrigger(object):
  def __init__(self,key,trigger):
    self.key = key
    self.trigger = trigger
    self.maker = "https://maker.ifttt.com/trigger/" + self.trigger + "/with/key/" + self.key
  def alert(self,value1=0,value2=0,value3=0):
    self.value1 = value1
    self.value2 = value2
    self.value3 = value3
    self.json = {"value1": self.value1, "value2": self.value2, "value3": self.value3 }
    r = requests.post(self.maker, json=self.json)
    print (self.json)



key = "cb_ErWZeYhdGljfLNidRJi"
trigger = "bri_cu_on"
ifttt = MakerTrigger(key,trigger)
ifttt.alert("alice","bob","carlo")

'''
time.sleep(1)
key = "cb_ErWZeYhdGljfLNidRJi"
trigger = "mastro_ingresso_on"
ifttt = MakerTrigger(key,trigger)
ifttt.alert("alice","bob","carlo")
time.sleep(1)
trigger = "mastro_ingresso_blue"
ifttt = MakerTrigger(key,trigger)
ifttt.alert("alice","bob","carlo")
time.sleep(5)
trigger = "mastro_ingresso_off"
ifttt = MakerTrigger(key,trigger)
ifttt.alert("alice","bob","carlo")

'''
