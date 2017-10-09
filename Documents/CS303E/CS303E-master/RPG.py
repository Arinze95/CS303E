#  File: RPG.py
#  Description: RPG in which a wizard and fighter battle. Not as thorough/comprehensive as a real RPG game.
#  Student's Name: Derek Orji
#  Student's UT EID: dao584
#  Course Name: CS 313E 
#  Unique Number: 51465
#
#  Date Created: 9/19/17
#  Date Last Modified: 9/24/17

class Weapon():                              #Class Weapon includes daggers, axes, staffs, swords, and "none". Used by characters to attack their opponents 
	def __init__(self, weapontype):  
		if weapontype == "dagger":
			self.weaponname = weapontype      #self.name is the attribute for the weapons name 
			self.damage = 4                   #self.damage is the attribute for the weapons effect
		if weapontype == "axe":
			self.weaponname = weapontype 
			self.damage = 6
		if weapontype == "staff":
			self.weaponname = weapontype 
			self.damage = 6
		if weapontype == "sword":
			self.weaponname = weapontype 
			self.damage = 10
		if weapontype == "none":
			self.weaponname = weapontype
			self.damage = 1

class Armor():                          # Class Armor includes plate, chain, leather, and "none". Used to protect characters against attack
	def __init__(self, armortype):
		if armortype == "plate":
			self.armor = armortype     #self.armor is the attribute for the armors name
			self.AC = 2                #self.AC is the attribute for the "class" or quality of the armor 
		if armortype == "chain":
			self.armor = armortype
			self.AC = 5
		if armortype == "leather":
			self.armor = armortype
			self.AC = 8
		if armortype == "none":
			self.armor = armortype
			self.AC = 10



class Spell():                       # Class Spell includes Fireball, lightning bolt, and heal. Used by wizards only to attack their opponents
	def __init__(self, spellname):
		if spellname == "Fireball": 
			self.spell = "Fireball"   #self.spell is the attribute for the spells name 
			self.cost = 3			  #self.cost is the attribute for the price of the spell
			self.effect = 5           # self.affect denotes how much damage the spell actually does
		if spellname == "Lightning Bolt":
			self.spell = "Lightning Bolt"
			self.cost = 10
			self.effect = 10
		if spellname == "Heal":
			self.spell = "Heal"
			self.cost = 6
			self.effect = -6        # The Heal spell does negative damage because it is meant to raise the health of whoever it affects



class RPGCharacter():          #RPGCharacter class has two subclasses, Fighter and Wizard
	def __init__(self, name):     #initializer for  the identity of the RPG character, creates an attribute name 
		self.name = name
		
	def __str__(self):       # this __str__ method is meant to return the status of the character, from its name, armor class, weapon, armor, health, and spell points
		return("\n" + str(self.name) + "\n" + "   Current Health: " + str(self.Health) + "\n" + "   Current Spell Points: " + str(self.SP) + "\n" + "   Wielding: " + str(self.weaponname) + "\n" + "   Wearing: " + str(self.armor) + "\n" + "   Armor class: " + str(Armor(self.armor).AC) + "\n")
	

class Fighter(RPGCharacter):    #Fighter characters can use all weapons, all armors, but have do not have the ability to cast spells 
	def __init__(self, name):
		self.name = name
		self.armor = "none"
		self.weaponname = "none"			
		self.Health = 40
		self.SP = 0
	def wield(self, weapon):    #Checks is fighter is eligible to wield weapon, and if so prints their weapon of choice
		if weapon.weaponname == "staff" or weapon.weaponname == "dagger" or weapon.weaponname == "axe" or weapon.weaponname == "sword" or weapon.weaponname == "none":
			print(str(self.name) + " is now wielding a(n) " + weapon.weaponname)
			self.weaponname = weapon.weaponname
		else:                   #If fighter is not eligibe for weapon it lets it be known
			print("Weapon not allowed for this character class")
	def unwield(self):        # set fighter weapon back to type none, so the damage they can do is minimal
		self.weaponname = "none"
		print(str(self.name) + " is no longer wielding anything")
	def putOnArmor(self, armor): #lets he fighter put on the armor of their choice 
		if armor.armor == "plate" or armor.armor == "chain" or armor.armor == "leather" or armor.armor == "none":
			print(str(self.name) + " is now wearing " + armor.armor)
			self.armor = armor.armor 
		else:
			print("Armor not allowed for this character class")
	def takeOffArmor(self):   # Lets the fighter take off their armor 
		self.armor = "none"
		print(str(self.name) + " is no longer wearing anything")
	def checkForDefeat(opponent):  #checks the fighters health to see if its still greater than 0
		if opponent.Health <= 0:
			print(str(opponent.name) + " has been defeated!")
	def fight(self, opponent):  #Fight method allows the fighter to inflict damage on their opponent and also deducts from opponents health
		print(str(self.name) + " attacks " + str(opponent.name) + " with a(n) " + str(self.weaponname)) 
		opponent.Health -= Weapon(self.weaponname).damage
		print(str(self.name) + " does " + str(Weapon(self.weaponname).damage) + " damage to " + str(opponent.name))
		print(str(opponent.name) + " is now down to " + str(opponent.Health) + " health")
		opponent.checkForDefeat() #calling method checkForDefeat to see if opponent has been defeated yet
	
		 

class Wizard(RPGCharacter): #wizard characters can only use daggers, and staffs, and are not able to employ armor 
	def __init__(self, name):
		self.name = name
		self.armor = "none"
		self.weaponname = "none"
		self.Health = 16
		self.SP = 20
	def wield(self, weapon): #checks to see if weapon is eligible under wizard class
		if weapon.weaponname == "staff" or weapon.weaponname == "dagger" or weapon.weaponname == "none":
			print(str(self.name) + " is now wielding a(n) " + weapon.weaponname)
			self.weaponname = weapon.weaponname
		else:
			print("Weapon not allowed for this character class") #lets it be known if weapon is not eligible 
	def unwield(self): #sets weapon type to none 
		self.weaponname = "none"
		print(str(self.name) + " is no longer wielding anything")
	def putOnArmor(self, armor): #basically lets it be known that wizard cant use armor
		if armor.armor == "plate" or armor.armor == "chain" or armor.armor == "leather":
			print("Armor not allowed for this character class")
		elif armor.armor == "none":
			print("Armor not allowed for this character class")
		else:
			print("Armor not allowed for this character class")
	def takeOffArmor(self): # sets armor type to none 
		self.armor = "none"
		print(str(self.name) + " is no longer wearing anything")
	def fight(self, opponent): # allows wizard to fight using weapons staff and dagger and none 
		print(str(self.name) + " attacks " + str(opponent.name) + " with a(n) " + str(self.weaponname)) 
		opponent.Health -= Weapon(self.weaponname).damage
		print(str(self.name) + " does " + str(Weapon(self.weaponname).damage) + " damage to " + str(opponent.name))
		print(str(opponent.name) + " is now down to " + str(opponent.Health) + " health")
		opponent.checkForDefeat()
	def castSpell(self, spell, opponent): # allows wizrd to cast spells during conflicts with opponents 
		if Spell(spell).spell != "Fireball" and Spell(spell).spell != "Lightning Bolt" and Spell(spell).spell != "Heal": #checks legitimacy of spell
			print("Unknown spell name. Spell failed.")
		if self.SP < Spell(spell).cost:  # checks to see if wizard has sufficent SP to cast spell
			print("Insufficient spell points")
		else:
			opponent.Health -= Spell(spell).effect #deducting from opponents health based on the effect of the spell
			self.SP -= Spell(spell).cost # deducting from the wizards SP based on the cost of the spell
			print(str(self.name) + " casts " + str(Spell(spell).spell) + " at " + str(opponent.name))
			if type(self) is Wizard and self.Health > 16: #makes sure that wizrds health doesnt go above its max value
				self.Health = 20
			if type(opponent) is Fighter and opponent.Health > 40: #makes sure fighters health doesnt go above its max value 
				opponent.Health = 40
			if Spell(spell).spell == "Heal": #heals or daamges opponent depending on the spell
				print(str(self.name) + " heals " + str(opponent.name) + " for " + str(-(Spell(spell).effect)) + " health points.")
				print(str(opponent.name) + " is now at " + str(opponent.Health) + " health")
			if Spell(spell).spell == "Fireball" or Spell(spell).spell == "Lightning Bolt":
				print(str(self.name) + " does " + str(Spell(spell).effect) + " damage to " + str(opponent.name))
				print(str(opponent.name) + " is now down to " + str(opponent.Health) + " health")
		opponent.checkForDefeat()

	def checkForDefeat(opponent): #checks to see if the oppoents health has fallen to or below 0
		if opponent.Health <= 0:
			print(str(opponent.name) + " has been defeated!")



def main():   #main program

    plateMail = Armor("plate")
    chainMail = Armor("chain")
    sword = Weapon("sword")
    staff = Weapon("staff")
    axe = Weapon("axe")
   

    gandalf = Wizard("Gandalf the Grey")
    gandalf.wield(staff)

    aragorn = Fighter("Aragorn")
    aragorn.putOnArmor(plateMail)
    aragorn.wield(axe)

    print(gandalf)
    print(aragorn)

    gandalf.castSpell("Fireball",aragorn)
    aragorn.fight(gandalf)

    print(gandalf)
    print(aragorn)
    
    gandalf.castSpell("Lightning Bolt",aragorn)
    aragorn.wield(sword)

    print(gandalf)
    print(aragorn)

    gandalf.castSpell("Heal",gandalf)
    aragorn.fight(gandalf)

    gandalf.fight(aragorn)
    aragorn.fight(gandalf)

    print(gandalf)
    print(aragorn)

psql \
   --host=pgrds.cdfu369kxyjr.us-east-2.rds.amazonaws.com \
   --port=5432 \
   --username=master \
   --password \
   --dbname=imdb





main()