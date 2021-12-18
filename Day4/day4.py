import copy
file = open("input.txt","r")


#handles line of bingo numbers
callNumbersStr = (file.readline()).split(",")
callNumbers=[]
for number in callNumbersStr:
	number = number.strip("\n")
	callNumbers.append(int(number))

lines =file.readlines()
print("*"*15+"Start"+"*"*15)
print("Numbers to be called\n"+str(callNumbers),"\n")

listofbingos = []
listofbingoscopy = []
board = []
bingocards =0

def crossout(value,listofbingos):
	for board in range(len(listofbingos)):
		for x in range(5):
			for y in range(5):
				if (listofbingos[board][x][y]==str(value)):
					listofbingos[board][x][y] = "x"
	return listofbingos

def printbingos(listofbingos):
	print("*"*10+"Print Bingo Cards"+"*"*10)
	for x in range(len(listofbingos)):
		print("Bingo card:",x+1)
		for element in listofbingos[x]:
			print(element)

def checkforbingo(listofbingos):
	for bingocard in range(len(listofbingos)):
		#check rows
		for row in range(5):
			if(listofbingos[bingocard][row]==['x', 'x', 'x', 'x', 'x']):
				print("Bingo! at card",bingocard+1)
				return bingocard	

		#check columns
		bingo = False
		for column in range(5):
			for row in range(5):
				if(listofbingos[bingocard][row][column]=='x'):
					bingo = True
					continue
				else:
					bingo = False
					break
			if (bingo):
				print("Bingo! at card",bingocard+1)
				return bingocard

	return -1

for x in range(len(lines)-1):
	if (lines[x]=="\n"):
		print("Bingo Card",bingocards)
		bingocards+=1
		for y in range(1,6):
			board.append(lines[x+y].strip("\n").split())
			
		listofbingos.append(board)
		board = []

listofbingoscopy = copy.deepcopy(listofbingos)

print("There are", bingocards,"bingo cards")


print("\n*****************Processing*****************\n")

crossout(0,listofbingos)
possibleindex=0
lastcalled=-1
for x in range(len(callNumbers)):
	listofbingos=crossout(callNumbers[x],listofbingos)
	possibleindex=checkforbingo(listofbingos)
	if(possibleindex!=-1):
		callNumbers[]
		print("Confirmed, Card",possibleindex+1,"is a bingo")
		break

print("\nEnd card:")
for row in listofbingos[possibleindex]:
	print(row)

print("\nStarting Card")
for row in listofbingoscopy[possibleindex]:
	print(row)



file.close() 