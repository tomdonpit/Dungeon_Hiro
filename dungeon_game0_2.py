import random
import math

#Parent class initialization: "Character"
class Character:
    def __init__(self, name, health_points, damage, x_pos, y_pos):
        self.name = name
        self.health_points = health_points
        self.damage = damage
        self.x_pos = x_pos
        self.y_pos = y_pos

#spawn() method to generate random (x, y) coordinates for characters and items
    def spawn(self):
        self.x_pos = math.ceil(random.random() * 10)
        self.y_pos = math.ceil(random.random() * 10)
        print(self.name , "spawned at: (", self.x_pos, ",", self.y_pos, ").")

#battle() method to have two characters (self/player vs. enemy) fight to 0HP. 
#Random damage within range determined by random(); modifies .health_points value.
    def battle(self, enemy):
        self.enemy = enemy
        while True:
            self.damage = 10 + (math.ceil(random.random() * self.damage))
            enemy.damage = 10 + (math.ceil(random.random() * enemy.damage))
            enemy.health_points = enemy.health_points - self.damage
            print(self.name, "attacks the", enemy.name, "for", self.damage, "damage point(s)!")
            print(enemy.name, "has", enemy.health_points, "health point(s) left.")
            if enemy.health_points <= 0:
                print("You have defeated the", enemy.name + "!")
                break
            self.health_points = self.health_points - enemy.damage
            print(enemy.name, "attacks the", self.name, "for", enemy.damage, "damage point(s)!")
            print(self.name, "has", self.health_points, "health point(s) left.")
            if self.health_points <= 0:
                print(self.name, "has been defeated by the", enemy.name)
                break

#item() child of Character; for health potions and weapons (with location on map)
class Item(Character):
    def __init__(self, name, health_points, damage, x_pos, y_pos):
        self.name = name
        self.health_points = health_points
        self.damage = damage
        self.x_pos = x_pos
        self.y_pos = y_pos

#hero() child of Character; has same attributes and methods of Character, but with new methods.
class Hero(Character):
    def __init__(self, name, health_points, damage, x_pos, y_pos):
        self.name = name
        self.health_points = health_points
        self.damage = damage
        self.x_pos = x_pos
        self.y_pos = y_pos

#move() method to change player's location by x1 square in any direction (with barriers at perimeter)
    def move(self):
        while True:
            print(self.name , "is at: (", self.x_pos, ",", self.y_pos, ").")
            direction = input("What direction would you like to travel? N, S, E, or W?: ")
            if direction.upper() == "N" and self.y_pos < 10:
                self.y_pos += 1
                print(self.name + "'s position is (", self.x_pos, ",", self.y_pos, ").")
                break
            elif direction.upper() == "S" and self.y_pos > 0:
                self.y_pos -= 1
                print(self.name + "'s position is (", self.x_pos, ",", self.y_pos, ").")
                break
            elif direction.upper() == "E" and self.x_pos < 10:
                self.x_pos += 1
                print(self.name + "'s position is (", self.x_pos, ",", self.y_pos, ").")
                break
            elif direction.upper() == "W" and self.x_pos > 0:
                self.x_pos -= 1
                print(self.name + "'s position is (", self.x_pos, ",", self.y_pos, ").")
                break
            else:
                print(self.name + "'s position is (", self.x_pos, ",", self.y_pos, "). Please select a valid direction.")

#equip() method to use weapon to add weapon's damage to player's damage points. 
    def equip(self, weapon):
        self.weapon = weapon
        self.damage += weapon.damage
#drink() method to consume a potion to add potion's health points to that of the player.
    def drink(self, potion):
        self.potion = potion
        self.health_points += potion.health_points       

#   Game While Loop   #
while True:
    game_start = input("Would you like to play 'Dungeon Hiro'? Enter '1' to continue or '2' to exit: ")
#Player selects option 1 to start a new game.
    if game_start == "1":
        player_name = input("What is your hero's name?: ")
        player = Hero(player_name, 200, 20, 0, 0)
        print('''
            In this game, you are an adventurer exploring a dark dungeon.
            The dungeon is a 10ft x 10ft square map.
            You can see your location with 'x' and 'y' coordinates.
            ''')
        #spawns player with random (x, y) coordinates and modifiable health/ damage.
        player.spawn()
        print('''
            You can move North (y+1), South (y-1), 
            East (x+1), and West (x-1) within the map. 
            But, you must move 1 square at a time.
            You will encounter several enemies in this dungeon, some stronger than others.
            Along the way, you may find health potions that restore your health points,
            and different weapons that will increase your damage.
            ''')
        #spawns enemies and items at random (x, y) coordinates with hard coded health/ damage
        enemy1 = Character("Vampire Bat", 75, 5, 0, 0)
        enemy1.spawn()
        enemy2 = Character("Skeleton Warrior", 125, 15, 0, 0)
        enemy2.spawn()
        enemy3 = Character("Troll", 225, 25, 0, 0)
        enemy3.spawn()
        enemy4 = Character("Dragon", 350, 40, 0, 0)
        enemy4.spawn()
        item1 = Item("Major Health Potion", 200, 0, 0, 0)
        item1.spawn()
        item2 = Item("Health Potion", 100, 0, 0, 0)
        item2.spawn()
        item3 = Item("Minor Health Potion", 50, 0, 0, 0)
        item3.spawn()
        weapon1 = Item("Dagger", 0, 10, 0, 0)
        weapon1.spawn()
        weapon2 = Item("Short Sword", 0, 20, 0, 0)
        weapon2.spawn()
        weapon3 = Item("Long Sword", 0, 40, 0, 0)
        weapon3.spawn()
        #Nested Game While Loop #
        while True:
            #If statements to prompt and end game in scenario where player dies or defeats dragon!
            if player.health_points <= 0:
                print(player.name, "has been killed: Game Over!")
                break
            elif enemy4.health_points <= 0:
                print(player.name, "killed the", enemy4.name + "!", player.name, "has won the game!")
                break
            #Display player location and any enemies/ items that appear at the same location
            print(player.name, "is at: (", player.x_pos, ",", player.y_pos, ").")
            if player.x_pos == enemy1.x_pos and player.y_pos == enemy1.y_pos:
                print(player.name, "is next to", enemy1.name)
            elif player.x_pos == enemy2.x_pos and player.y_pos == enemy2.y_pos:
                print(player.name, "is next to", enemy2.name)
            elif player.x_pos == enemy3.x_pos and player.y_pos == enemy3.y_pos:
                print(player.name, "is next to", enemy3.name)
            elif player.x_pos == enemy4.x_pos and player.y_pos == enemy4.y_pos:
                print(player.name, "is next to", enemy4.name)
            elif player.x_pos == item1.x_pos and player.y_pos == item1.y_pos:
                print(player.name, "is next to", item1.name)
            elif player.x_pos == item2.x_pos and player.y_pos == item2.y_pos:
                print(player.name, "is next to", item2.name)
            elif player.x_pos == item3.x_pos and player.y_pos == item3.y_pos:
                print(player.name, "is next to", item3.name)
            elif player.x_pos == weapon1.x_pos and player.y_pos == weapon1.y_pos:
                print(player.name, "is next to", weapon1.name)
            elif player.x_pos == weapon2.x_pos and player.y_pos == weapon2.y_pos:
                print(player.name, "is next to", weapon2.name)
            elif player.x_pos == weapon3.x_pos and player.y_pos == weapon3.y_pos:
                print(player.name, "is next to", weapon3.name)
            #player decision time, this is the main space of the actual game
            player_decision = input('''
            What will you do?
            '1': Move the player x1 square in any direction.
            '2': Use item at your location.
            '3': Attack an enemy at your location.
            '4': Display player health and damage
            '5': Show the map with locations of enemies and items.
            '6': Exit the game.
            ''')
            #Player wants to move location
            if player_decision == "1":
                player.move()
                continue
            #Player wants to drink(potion) or equip(weapon)
            elif player_decision == "2":
                if player.x_pos == item1.x_pos and player.y_pos == item1.y_pos:
                    player.drink(item1)
                    print(player.name, "just drank", item1.name + "!")
                    print(player.name + "'s health points are now: " + str(player.health_points))
                    continue
                elif player.x_pos == item2.x_pos and player.y_pos == item2.y_pos:
                    player.drink(item2)
                    print(player.name, "just drank", item2.name + "!")
                    print(player.name + "'s health points are now: " + str(player.health_points))
                    continue
                elif player.x_pos == item3.x_pos and player.y_pos == item3.y_pos:
                    player.drink(item3)
                    print(player.name, "just drank", item3.name + "!")
                    print(player.name + "'s health points are now: " + str(player.health_points))
                    continue
                elif player.x_pos == weapon1.x_pos and player.y_pos == weapon1.y_pos:
                    player.equip(weapon1)
                    print(player.name, "just equipped", weapon1.name + "!")
                    print(player.name + "'s damage is now: " + str(player.damage))
                    continue
                elif player.x_pos == weapon2.x_pos and player.y_pos == weapon2.y_pos:
                    player.equip(weapon2)
                    print(player.name, "just equipped", weapon2.name + "!")
                    print(player.name + "'s damage is now: " + str(player.damage))
                    continue
                elif player.x_pos == weapon3.x_pos and player.y_pos == weapon3.y_pos:
                    player.equip(weapon3)
                    print(player.name, "just equipped", weapon3.name + "!")
                    print(player.name + "'s damage is now: " + str(player.damage))
                    continue
                else:
                    print("Please select a valid option.")
                    continue
            #Player wants to battle(enemy) at same location
            elif player_decision == "3":
                if player.x_pos == enemy1.x_pos and player.y_pos == enemy1.y_pos:
                    player.battle(enemy1)
                    continue
                elif player.x_pos == enemy2.x_pos and player.y_pos == enemy2.y_pos:
                    player.battle(enemy2)
                    continue
                elif player.x_pos == enemy3.x_pos and player.y_pos == enemy3.y_pos:
                    player.battle(enemy3)
                    continue
                elif player.x_pos == enemy4.x_pos and player.y_pos == enemy4.y_pos:
                    player.battle(enemy4)
                    continue
                else:
                    print("Please select a valid option.")
                    continue
            #Player wants to display their health and damage points
            elif player_decision == "4":
                print(player.name, "has", str(player.health_points), "health points and", str(player.damage), "damage.")
                continue
            #Player wants to look at the coordinates of enemies/ items in the game map.
            elif player_decision == "5":
                print(enemy1.name , "spawned at: (", enemy1.x_pos, ",", enemy1.y_pos, ").")
                print(enemy2.name , "spawned at: (", enemy2.x_pos, ",", enemy2.y_pos, ").")
                print(enemy3.name , "spawned at: (", enemy3.x_pos, ",", enemy3.y_pos, ").")
                print(enemy4.name , "spawned at: (", enemy4.x_pos, ",", enemy4.y_pos, ").")
                print(item1.name , "spawned at: (", item1.x_pos, ",", item1.y_pos, ").")
                print(item2.name , "spawned at: (", item2.x_pos, ",", item2.y_pos, ").")
                print(item3.name , "spawned at: (", item3.x_pos, ",", item3.y_pos, ").")
                print(weapon1.name , "spawned at: (", weapon1.x_pos, ",", weapon1.y_pos, ").")
                print(weapon2.name , "spawned at: (", weapon2.x_pos, ",", weapon2.y_pos, ").")
                print(weapon3.name , "spawned at: (", weapon3.x_pos, ",", weapon3.y_pos, ").")
                continue
            #Player exits game to break out of loops
            elif player_decision == "6":
                print("You have exited the game. Goodbye!")
                break

            else:
                continue
            break
        break
    #Player has decided to exit game on startup.
    elif game_start == "2":
        print("You have exited the game. Goodbye!")
        break
    else:
        print("Please enter a valid selection: '1' to continue or '2' to exit. ")





#   Driver 1  Spawn + Move  #
#print(math.ceil(random.random() * 10))
#charz = Character("Character", 100, 10, 1, 1)
#charz.spawn("Char", 0, 0)
#charz.attack(10)

#hero = Hero("Hiro", 200, 20, 0, 0)
#hero.spawn()
#print(hero.x_pos)
#print(hero.y_pos)
#hero.move()

#print(hero.health_points)
#troll = Character("Troll", 300, 10, 0, 0)
#hero.battle(troll)
#print(hero.health_points)
#troll.spawn()
#print(troll.x_pos, troll.y_pos)

"""     def attack(self, enemy):
        self.enemy = enemy
        self.damage = math.ceil(random.random() * self.damage)
        print("Attack for", self.damage, "damage point(s)!") """

#Driver 2 Battle Func#
""" hero = Hero("Hiro", 200, 10, 0, 0)
hero.spawn()
troll = Character("Troll", 300, 20, 0, 0)
troll.spawn()
sword = item("sword", 100, 20, 2, 2)
minor_health_potion = item("minor health potion", 15, 0, 3, 3)
hero.equip(sword)
print(hero.damage)
#hero.drink(minor_health_potion)
print(hero.health_points)
hero.battle(troll) """
