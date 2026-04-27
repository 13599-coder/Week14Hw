#Evan Machica
#Period 6
#Week 14
#time spent
import classes
player1 = classes.Samuri("Peter", 100, 15, 2, 5)
player2 = classes.Wizard("Emily", 80, 10, 3, 20)
player1.display_stats()
print()
player2.display_stats()
print()
player1.attack()
player2.attack()
print()
player1.take_damage()
player2.take_damage()
print()
player1.block()
player2.heal()
