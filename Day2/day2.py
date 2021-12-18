file = open("input.txt","r")
depth = 0
hpos = 0
aim = 0

for line in file:
	newline = line.split(' ')
	newline[1] = int(newline[1].strip('\n'))
	
	if newline[0]=="forward":
		hpos+=newline[1]
		depth += aim*newline[1]
	elif newline[0]=="up":
		#depth-=newline[1]
		aim -=newline[1]
	elif newline[0]=="down":
		#depth+=newline[1]
		aim += newline[1]
	print("Hpos:",hpos,"Depth:",depth,"Aim:",aim)

print(depth*hpos)

file.close()