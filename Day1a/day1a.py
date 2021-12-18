file = open("input.txt","r")
counter = 0
array=[]

#a = file.readline()
for line in file:
    num = line.strip('\n')
    if line != '':
        array.append(num)
    #b = int(file.readline())
    #if(b-a)>0:
    #    counter +=1
    #a = b

a=int(array[0])

intarray =[int(i)for i in array]
#intarray = [199,200,208,210,200,207,240,269,260,263]
newarray=[]
j=0   
for i in range(0,len(intarray)-3):
    #print(intarray[i])
    j+=1 
    newarray.append(intarray[i]+intarray[i+1]+intarray[i+2])
print(j)

for x in range(1,len(newarray)):
    b = int(newarray[x])
    if(b-a)>0:
        counter +=1
    a = b
print(counter)
file.close
