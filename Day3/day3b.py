file = open("input.txt","r")
linematrix = []

linecounter = 0

for line in file:
	code = (line.strip("\n"))
	linematrix.append(list(code))

linematrix2 =linematrix.copy()

def find_most_common(columnIndex,ox=True):
	tempsum = 0
	for i in range(0,len(linematrix)):
			tempsum += int(linematrix[i][columnIndex])
	
	if(tempsum==(len(linematrix)/2)):
		print("there are an equal number of 0s and 1s at index:", columnIndex)
		if(ox):
			return 1
		else:
			return 0
	elif(ox):
		if tempsum>(len(linematrix)/2):
			print("There are more 1s in column", columnIndex)
			return 1
		else:
			print("There are more 0s in column", columnIndex)
			return 0
	else:
		if tempsum>(len(linematrix)/2):
			print("There are less 0s in column", columnIndex)
			return 0
		else:
			print("There are less 1s in column", columnIndex)
			return 1

def remove(matrix,columnIndex, value):
	x=0
	while(x<len(matrix)):
		if int(matrix[x][columnIndex])!=value:
			del matrix[x]
		else:
			x+=1
	return matrix


oxygenrat=0
co2rating=0

print("Now finding the oxygen generator rating:")

for x in range(len(linematrix[0])):
	print("Now scanning column", x)
	allow = find_most_common(x)
	print(len(linematrix))
	linematrix = remove(linematrix,x,allow)
	print(len(linematrix))
	if(len(linematrix)==1):
		break
print(linematrix)

stringbinary=""

for element in linematrix[0]:
	stringbinary +=str(element)

oxygenrat = int(stringbinary,2)
print(oxygenrat)

#reset linematrix
#print("before repopulation",len(linematrix))
linematrix = linematrix2.copy()
#print("after repopulation",len(linematrix))

print("\n**********Now finding the co2 generator rating:**************")

for x in range(len(linematrix[0])):
	print("Now scanning column", x)
	allow = find_most_common(x,False)
	print(len(linematrix))
	linematrix = remove(linematrix,x,allow)
	print(len(linematrix))
	if(len(linematrix)==1):
		break

print(linematrix)

stringbinary=""

for element in linematrix[0]:
	stringbinary +=str(element)

co2rat = int(stringbinary,2)
print(co2rat)


print("FINAL answer:\n"+"oxygen thing:",oxygenrat,"\tco2 thing:",co2rat)
print("Overall thing", oxygenrat*co2rat)



#


#
#for entry in linematrix:
#	print(entry)


file.close()




"""
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
"""