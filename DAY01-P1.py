pointer = 50
count = 0 

f = open('input.txt','r')
data = f.readlines()

for i in data: 
    atoi = int(i[1:])
    if(i[0]=='R'): 
       pointer = (pointer + atoi) % 100
    else: 
        if(atoi>pointer):
            pointer = (100-(abs(atoi - pointer) % 100 ))%100
        else: 
            pointer = (abs(atoi - pointer) % 100 )
    if(pointer == 0): 
        count+=1


print(count)


