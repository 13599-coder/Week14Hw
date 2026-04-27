#Evan Machica
#Period 6
#Week 14Hw
#time spent 
class RPGCharacter:
    def __init__(self, name, health, attack_power, level):
      self.__name = name
      self.__health = health
      self.__attack_power = attack_power
      self.__level = level
    def get_name(self):
      return self.__name
    def attack(self):
      print(self.__name, "attacks using", self.__attack_power)
