def areanagrams(word1, word2):
	if len(word1) != len(word2):
		return False 
	else:
		for i in range(len(word1)):
			if word1[i] in word2:
				continue 
			else:
				return False
		return True 
def main():
	string1 = input("Enter a word: ")
	string2 = input("Enter another word: ")
	if areanagrams(string1, string2):
		print("True")
	else:
		print("False")
main()


