#  File: Benford.py

#  Description: This program counts the frequency of the leading digit of a population sample

#  Student Name: Derek Orji

#  Student UT EID: dao584

#  Course Name: CS 303E

#  Unique Number: 51845

#  Date Created: 4/29/2017

#  Date Last Modified: 4/29/2017

def main():
  # create an empty dictionary
  pop_freq = {}

  # initialize the dictionary
  pop_freq['1'] = 0
  pop_freq['2'] = 0
  pop_freq['3'] = 0
  pop_freq['4'] = 0
  pop_freq['5'] = 0
  pop_freq['6'] = 0
  pop_freq['7'] = 0 
  pop_freq['8'] = 0
  pop_freq['9'] = 0

  # open file for reading
  in_file = open ("./Census_2009.txt", "r")

  # read the header and ignore
  header = in_file.readline()

  # read subsequent lines
  for line in in_file:
    line = line.strip()
    pop_data = line.split()
    # get the last element that is the population number
    pop_num = pop_data[-1]
    # make entries in the dictionary
    if pop_num[0] == "1":
      pop_freq['1'] += 1
    if pop_num[0] == "2":
      pop_freq['2'] += 1
    if pop_num[0] == "3":
      pop_freq['3'] += 1
    if pop_num[0] == "4":
      pop_freq['4'] += 1
    if pop_num[0] == "5":
      pop_freq['5'] += 1
    if pop_num[0] == "6":
      pop_freq['6'] += 1
    if pop_num[0] == "7":
      pop_freq['7'] += 1
    if pop_num[0] == "8":
      pop_freq['8'] += 1
    if pop_num[0] == "9":
      pop_freq['9'] += 1


  # close the file
  in_file.close()

  # write out the result
  print("Digit    Count    %")
  sum1 = 0
  for key in pop_freq:
    sum1 += pop_freq[key]
  

  for key in pop_freq:
    #print(str(key)+"        "+str(pop_freq[key])+"    "+str(format(((pop_freq[key]/sum1)*100), '.1f')))
    print(str(key)+"        "+str(pop_freq[key]) +"  "+ (" "*(7 - len(str(pop_freq[key]))))+str(format(((pop_freq[key]/sum1)*100), '.1f')))
  
main()