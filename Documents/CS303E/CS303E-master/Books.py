#  File: Books.py

#  Description: This program compares the vocabularies displayed by Authors

#  Student Name: Derek Orji

#  Student UT EID: dao584

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 303E

#  Unique Number: 51845

#  Date Created: 5/5/17

#  Date Last Modified: 5/5/17

def()



def main():
  # Create word dictionary from comprehensive word list
  create_word_dict()

  # Enter names of the two books in electronic form
  book1 = input ("Enter name of first book: ")
  book2 = input ("Enter name of second book: ")
  print()

  # Enter names of the two authors
  author1 = input ("Enter last name of first author: ")
  author2 = input ("Enter last name of second author: ")
  print() 
  
  # Get the frequency of words used by the two authors
  wordFreq1 = getWordFreq (book1)
  wordFreq2 = getWordFreq (book2)

  # Compare the relative frequency of uncommon words used
  # by the two authors
  wordComparison (author1, wordFreq1, author2, wordFreq2)

main()




