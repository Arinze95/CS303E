#string = input("Enter a string, say whatever you want")
#string = string.strip()
#dict1 = {}
#for i in range(len(string)):
	#dict1[string[i]] = 0
#for i in range(len(string)):
	#for key in dict1:
		#if string[i] == key:
		#	dict1[key] += 1
#print(dict1)


#dict2 = {"1": "pig", "5":"dog", "7": "ostrich", "9": "tiger", "4": "horse"}
#dictnew = {}
#for key in dict2:
#	dictnew[dict2[key]] = key 
#print(dict2)
#print(dictnew)

#dict3 = {"1": "pig", "5":"dog", "7": "ostrich", "9": "tiger", "4": "horse", "11":"ostrich", "89":"pig", "09":"tiger"}
#newdict = {}
#for key in dict3:
#	if dict3[key] not in newdict:
#		newdict[dict3[key]] = key 
#	else:
#		newdict[dict3[key]] += key 
	
#print(newdict)


#def common_string(s1, s2):
#	a = set(s1)
#	b = set(s2)
#	d = a & b
#	return(d)

#def main():
#	string1 = input("Enter a list of strings")
#	string2 = input("Enter a list of strings")
#	string1 = string1.strip()
#	string2 = string2.strip()
#	return(print(common_string(string1, string2)))
#main()
#import random 
#a = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
#for i in range(len(a)):
#	for j in range(0,5):
#		a[i][j] = random.randint(1,100)
#print(a)
def main():
	a = [[1, 2, 3], [4,5,6], [7,8,9]]
	b = [[1,2,3], [4,5,6], [7,8,9]]
	c = True 
	if (len(a) == len(b)) and (len(a[0] == len(b[0]))):
		for i in range(len(b)):
			for j in range(len(b[i])):
				if b[i][j] == a[i][j]:
					continue 
				else:
					c = False
	return(c) 
main()





