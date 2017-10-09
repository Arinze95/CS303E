class LivingThing:
   can_walk = True

class Plant(LivingThing):
   can_walk = False

class Animal(LivingThing):

   can_fly = False
   legs = 4

class Dog(Animal):

   def __init__(self):
      self.name = "Fido"


class Cat(Animal):

   name = "Meredith"

   def changeAllNames(self,newName):
      Cat.name = newName

class Bird(Animal):

   can_fly = True

   def __init__(self,name):
      self.name = name
      self.legs = 2
      self.wings = 2

class Fish(Animal):

   can_walk = False
   legs = 0

   def __init__(self,name):
      self.name = name

def main():

   dog1 = Dog()
   dog2 = Dog()
   print(dog1.name)
   print(dog2.name)
   
   dog2.name = "Spot"
   print(dog1.name)
   print(dog2.name)
   print("\n")

   cat1 = Cat()
   cat2 = Cat()
   print(cat1.name)
   print(cat2.name)

   cat2.name = "Sylvester"
   print(cat1.name)
   print(cat2.name)

   Cat.name = "Garfield"
   print(cat1.name)
   print(cat2.name)
   print("\n")

   cat1.changeAllNames("Puddy Tat")
   print(cat1.name)
   print(cat2.name)
   print("\n")

   #print(cat2.can_fly)
   #print(dog1.can_fly)
   #print("\n")

   bird1 = Bird("Tweety")
   #print(bird1.name)
   #print(bird1.can_fly)
   #print(bird1.wings)

   bird2 = Bird("Opus")
   bird2.can_fly = False
   #print(bird2.name)
   #print(bird2.can_fly)
   #print(bird2.wings)

   print(dog1.can_walk)
   print(cat1.can_walk)
   print(bird1.can_walk)

   fish1 = Fish("Nemo")
   print(fish1.name)
   print(fish1.can_walk)

main()