def ispal(word):
	for i in range(len(word) // 2):
		if word[i] == word[len(word) - i - 1]:
			return True 
		else:
			return False 
def main():
	checker = input("Enter a word: ")
	if ispal(checker):
		print("True") 
	else:
		print("False") 
main()




