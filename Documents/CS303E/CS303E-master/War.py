#  File: War.py
#  Description: Program that simulates the game war 
#  Student's Name: Derek Orji
#  Student's UT EID: dao584
#  Course Name: CS 313E 
#  Unique Number: 51465
#
#  Date Created: 10/2/17
#  Date Last Modified: 10/6/17

import random

class Card():													#Class card takes in parameters for suit and rank and creates a card object 
	def __init__(self, Suit, Rank):
		self.Suit = Suit
		self.Rank = Rank
	def __str__(self):
		return(str(self.Rank) + str(self.Suit))

class Ranks():													#Class Ranks defines the "power" of each card
	def __init__(self, string):
		if string == "2":
			self.mag = 1
		if string == "3":
			self.mag = 2
		if string == "4":
			self.mag = 3
		if string == "5":
			self.mag = 4 
		if string == "6":
			self.mag = 5
		if string == "7":
			self.mag = 6
		if string == "8":
			self.mag = 7
		if string == "9":
			self.mag = 8 
		if string == "1":
			self.mag = 9
		if string == "J":
			self.mag = 10
		if string == "Q":
			self.mag = 11
		if string == "K":
			self.mag = 12
		if string == "A":
			self.mag = 13


class Deck():											#Class Deck creates a list of card objects 
	
	def __init__(self):
		Suites = ["C", "D", "H", "S"]
		Ranked = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
		self.cardList = []
		for item in range(0,len(Suites),1):
			for item1 in range(0, len(Ranked), 1):
				(self.cardList).append(Card(Suites[item], Ranked[item1]))
	def __str__(self):
		counter = 0
		cardliststring = "  " 
		for card in self.cardList:
			if len(str(card)) == 3:
				cardliststring += "\b" + Card.__str__(card) + "  "
				counter += 1
			else: 
				cardliststring += Card.__str__(card) + "  "
				counter += 1
			if counter % 13 == 0:
				cardliststring += "\n  "
		return(cardliststring)
	def shuffle(self):
		random.shuffle(self.cardList)
	def dealOne(self, player):									#dealone function deals 52 cards equally between two players 
		self.deal = (self.cardList).pop(0)
		player.hand.append(self.deal)


class Player():											#class players holds the hand of each player, prints it out in format, and holds the count of each players hand 

	def __init__(self):
		self.hand = []
		self.handTotal = 0
	def __str__(self):
		counter = 0
		cardliststring1 = "  " 
		for card in self.hand:
			if len(str(card)) == 3:
				cardliststring1 += "\b" + Card.__str__(card) + "  "
				counter += 1
				self.handTotal += 1
			else: 
				cardliststring1 += Card.__str__(card) + "  "
				counter += 1
				self.handTotal += 1
			if counter % 13 == 0:
				cardliststring1 += "\n  "
		return(cardliststring1)

def WARR():										#class war does a war between the two players in the event that their cards match
	for n in range(1,5,1):
		if len(player1.hand) == 0:				#declares winner, prints hands if a player loses all their cards 
			Gameon = False
			for x in range(0, len(repository1)):
				player2.hand.append(repository1[x])
			for y in range(0, len(repository2)):
				player2.hand.append(repository2[y])
					
			print("\n" + "Player 1 now has " + str(len(player1.hand)) + " card(s) in hand:" + "\n" + str(player1))
			print("Player 2 now has " + str(len(player2.hand)) + " card(s) in hand:" + "\n" + str(player2) + "\n" + "\n")
			print("\b" + "\b" + "Game over.  Player 2 wins!" + "\n" + "\n")

		if len(player2.hand) == 0:				#declares winner, prints hands if a player loses all their cards 
			Gameon = False 
			for x in range(0, len(repository1)):
				player1.hand.append(repository1[x])
			for y in range(0, len(repository2)):
				player1.hand.append(repository2[y])
					
			print("\n" + "Player 1 now has " + str(len(player1.hand)) + " card(s) in hand:" + "\n" + str(player1))
			print("Player 2 now has " + str(len(player2.hand)) + " card(s) in hand:" + "\n" + str(player2) + "\n" + "\n")
			print("\b" + "\b" + "Game over.  Player 1 wins!" + "\n" + "\n")

		if Gameon == False:  
			return(print("Final hands:" + "\n" + "Player 1:" + "\n" + str(player1) + "\n" + "\n" + "Player 2:" + "\n" + str(player2)))

		if n != 4: #If not the fourth card in a war, pop and append to a list of waiting cards
			warcard1 = player1.hand.pop(0)
			warcard2 = player2.hand.pop(0)
			repository1.append(warcard1)
			repository2.append(warcard2)
			print("Player 1 puts " + str(warcard1) + " face down")
			print("Player 2 puts " + str(warcard2) + " face down")

				
		else: #If the fourth card, compares the fourth card to see who wins war 
			warcard1 = player1.hand.pop(0)
			warcard2 = player2.hand.pop(0)
			repository1.append(warcard1)
			repository2.append(warcard2)
			print("Player 1 puts " + str(warcard1) + " face up")
			print("Player 2 puts " + str(warcard2) + " face up")
					
			if Ranks(str(warcard1)[0]).mag > Ranks(str(warcard2)[0]).mag:
				for x in range(0, len(repository1)):
					player1.hand.append(repository1[x])
				for y in range(0, len(repository2)):
					player1.hand.append(repository2[y])
				print("\n" + "Player 1 wins round " + str(Round) + ": " + str(warcard1) + " >  " + str(warcard2))
				print("\n" + "Player 1 now has " + str(len(player1.hand)) + " card(s) in hand:" + "\n" + str(player1))
				print("Player 2 now has " + str(len(player2.hand)) + " card(s) in hand:" + "\n" + str(player2) + "\n" + "\n")
						
					
						
						
						
			if Ranks(str(warcard1)[0]).mag < Ranks(str(warcard2)[0]).mag:
				for x in range(0, len(repository1)):
					player2.hand.append(repository1[x])
				for y in range(0, len(repository2)):
					player2.hand.append(repository2[y])
				print("\n" + "Player 2 wins round " + str(Round) + ": " + str(warcard2) + " >  " + str(warcard1))
				print("\n" + "Player 1 now has " + str(len(player1.hand)) + " card(s) in hand:" + "\n" + str(player1))
				print("Player 2 now has " + str(len(player2.hand)) + " card(s) in hand:" + "\n" + str(player2) + "\n" + "\n")

			if Ranks(str(warcard1)[0]).mag == Ranks(str(warcard2)[0]).mag: #Calls Warr function if war occurs within a war
				return(WARR())
	


def playGame(player1, player2): #function actually facilates the war between the two players 


	print("\n" + "\n" + "Initial hands:")
	print("Player 1: " + "\n" + str(player1) + "\n")
	print("Player 2: " + "\n" + str(player2) + "\n" + "\n")

	Round = 0
	
	while len(player1.hand) > 0 and len(player2.hand) > 0: #Keeps function going as long as both players have atleast 1 card in hand 
		Gameon = True 
		repository1 = []
		repository2 = []
		Round += 1
		warcard1 = player1.hand.pop(0)
		warcard2 = player2.hand.pop(0)
		repository1.append(warcard1)
		repository2.append(warcard2)



		
		print("ROUND " + str(Round) + ":" + "\n" + "Player 1 plays:  " + str(warcard1) + "\n" + "Player 2 plays:  " + str(warcard2))

		if Ranks(str(warcard1)[0]).mag > Ranks(str(warcard2)[0]).mag: #player one wins if his card is of greater rank
			player1.hand.append(warcard1)
			player1.hand.append(warcard2)
			print("\n" + "Player 1 wins round " + str(Round) + ": " + str(warcard1) + " >  " + str(warcard2))
			print("\n" + "Player 1 now has " + str(len(player1.hand)) + " card(s) in hand:" + "\n" + str(player1))
			print("Player 2 now has " + str(len(player2.hand)) + " card(s) in hand:" + "\n" + str(player2) + "\n" + "\n")


			
			if len(player1.hand) == 0:
				Gameon = False
				
				
				print("\b" + "\b" + "Game over.  Player 2 wins!" + "\n" + "\n")

			if len(player2.hand) == 0:
				Gameon = False 
				
				
				print("\b" + "\b" + "Game over.  Player 1 wins!" + "\n" + "\n")

			if Gameon == False:
				return(print("Final hands:" + "\n" + "Player 1:" + "\n" + str(player1) + "\n" + "\n" + "Player 2:" + "\n" + str(player2)))


		if Ranks(str(warcard1)[0]).mag < Ranks(str(warcard2)[0]).mag: #player 2 wins if her card is of greater rank
			player2.hand.append(warcard1)
			player2.hand.append(warcard2)
			print("\n" + "Player 2 wins round " + str(Round) + ": " + str(warcard2) + " >  " + str(warcard1))
			print("\n" + "Player 1 now has " + str(len(player1.hand)) + " card(s) in hand:" + "\n" + str(player1))
			print("Player 2 now has " + str(len(player2.hand)) + " card(s) in hand:" + "\n" + str(player2) + "\n" + "\n")

			
			if len(player1.hand) == 0:
				Gameon = False
				
				
				print("\b" + "\b" + "Game over.  Player 2 wins!" + "\n" + "\n")

			if len(player2.hand) == 0:
				Gameon = False 
				
				
				print("\b" + "\b" + "Game over.  Player 1 wins!" + "\n" + "\n")

			if Gameon == False:
				return(print("Final hands:" + "\n" + "Player 1:" + "\n" + str(player1) + "\n" + "\n" + "Player 2:" + "\n" + str(player2)))



		if str(warcard1)[0] == str(warcard2)[0]: #War is declared if the ranks of both cards are equal Everything else in this if statement is just like that in the war funtion 
			print("\n" + "War starts:  " + str(warcard1) + " =  " + str(warcard2))
			for n in range(1,5,1):
				if len(player1.hand) == 0:
					Gameon = False
					for x in range(0, len(repository1)):
						player2.hand.append(repository1[x])
					for y in range(0, len(repository2)):
						player2.hand.append(repository2[y])
					
					print("\n" + "Player 1 now has " + str(len(player1.hand)) + " card(s) in hand:" + "\n" + str(player1))
					print("Player 2 now has " + str(len(player2.hand)) + " card(s) in hand:" + "\n" + str(player2) + "\n" + "\n")
					print("\b" + "\b" + "Game over.  Player 2 wins!" + "\n" + "\n")

				if len(player2.hand) == 0:
					Gameon = False 
					for x in range(0, len(repository1)):
						player1.hand.append(repository1[x])
					for y in range(0, len(repository2)):
						player1.hand.append(repository2[y])
					
					print("\n" + "Player 1 now has " + str(len(player1.hand)) + " card(s) in hand:" + "\n" + str(player1))
					print("Player 2 now has " + str(len(player2.hand)) + " card(s) in hand:" + "\n" + str(player2) + "\n" + "\n")
					print("\b" + "\b" + "Game over.  Player 1 wins!" + "\n" + "\n")

				if Gameon == False:
					return(print("Final hands:" + "\n" + "Player 1:" + "\n" + str(player1) + "\n" + "\n" + "Player 2:" + "\n" + str(player2)))

				if n != 4:
					warcard1 = player1.hand.pop(0)
					warcard2 = player2.hand.pop(0)
					repository1.append(warcard1)
					repository2.append(warcard2)
					print("Player 1 puts " + str(warcard1) + " face down")
					print("Player 2 puts " + str(warcard2) + " face down")

				
				else:
					warcard1 = player1.hand.pop(0)
					warcard2 = player2.hand.pop(0)
					repository1.append(warcard1)
					repository2.append(warcard2)
					print("Player 1 puts " + str(warcard1) + " face up")
					print("Player 2 puts " + str(warcard2) + " face up")
					
					if Ranks(str(warcard1)[0]).mag > Ranks(str(warcard2)[0]).mag:
						for x in range(0, len(repository1)):
							player1.hand.append(repository1[x])
						for y in range(0, len(repository2)):
							player1.hand.append(repository2[y])
						print("\n" + "Player 1 wins round " + str(Round) + ": " + str(warcard1) + " >  " + str(warcard2))
						print("\n" + "Player 1 now has " + str(len(player1.hand)) + " card(s) in hand:" + "\n" + str(player1))
						print("Player 2 now has " + str(len(player2.hand)) + " card(s) in hand:" + "\n" + str(player2) + "\n" + "\n")
						
					
						
						
						
					if Ranks(str(warcard1)[0]).mag < Ranks(str(warcard2)[0]).mag:
						for x in range(0, len(repository1)):
							player2.hand.append(repository1[x])
						for y in range(0, len(repository2)):
							player2.hand.append(repository2[y])
						print("\n" + "Player 2 wins round " + str(Round) + ": " + str(warcard2) + " >  " + str(warcard1))
						print("\n" + "Player 1 now has " + str(len(player1.hand)) + " card(s) in hand:" + "\n" + str(player1))
						print("Player 2 now has " + str(len(player2.hand)) + " card(s) in hand:" + "\n" + str(player2) + "\n" + "\n")
	

						

					if Ranks(str(warcard1)[0]).mag == Ranks(str(warcard2)[0]).mag:
						return(WARR())
						

						





		 



def main():

    cardDeck = Deck()               # create a deck of 52 cards called "cardDeck"
    print("Initial deck:")
    print(cardDeck)                 # print the deck so we can see that you built it correctly
    
    random.seed(15)                 # leave this in for grading purposes
    cardDeck.shuffle()              # shuffle the deck
    print("Shuffled deck:")
    print(cardDeck)                 # print the deck so we can see that your shuffle worked
    
    player1 = Player()              # create a player
    player2 = Player()              # create another player
    for i in range(26):             # deal 26 cards to each player, one at 
       cardDeck.dealOne(player1)    #   a time, alternating between players
       cardDeck.dealOne(player2)
    playGame(player1, player2)

main()


#243424
