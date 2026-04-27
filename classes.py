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
    def take_damage(self):
        self.__health = self.__health - 10
        print(self.__name, "takes damage")
    def display_stats(self):
        print("name:", self.__name)
        print("health:", self.__health)
        print("attack:", self.__attack_power)
        print("level:", self.__level)
class Samuri(RPGCharacter):
    def __init__(self, name, health, attack_power, level, armor):
        RPGCharacter.__init__(self, name, health, attack_power, level)
        self.__armor = armor
    def take_damage(self):
        print(self.get_name(), "uses the armor")
    def block(self):
        print(self.get_name(), "blocks the attack")
