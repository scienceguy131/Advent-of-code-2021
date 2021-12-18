file = open("input.txt","r")
linematrix = []
linecounter = 0
for line in file:
	code = (line.strip("\n"))
	linematrix.append(list(code))

adds=[]
print(len(linematrix))
for x in range(0,len(linematrix[0])):
	tempsum = 0
	for i in range(0,len(linematrix)):
		tempsum += int(linematrix[i][x])
	adds.append(tempsum)

finalbinary = []

for element in adds:
	if(element>(len(linematrix)/2)):
		finalbinary.append(1)
	elif element==(len(linematrix)/2):
		finalbinary.append(1)
		print("there are an equal number of 0s and 1s at index:", len(finalbinary))
	else:
		finalbinary.append(0)

#print(linematrix)
print(adds)
print(finalbinary)

finaldecimal = 0
stringBinary = ""
for element in finalbinary:
	stringBinary +=str(element)

finaldecimalG=int(stringBinary,2)
print(finaldecimalG)
finaldecimalE = (2**len(linematrix[0]))-1-finaldecimalG
print(finaldecimalE)
print("Final power consumption:", finaldecimalG*finaldecimalE)