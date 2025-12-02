f = open("input.txt","r")
data = f.readline()
# checking for pattern repetition in given 
data = data.split(',')
sum = 0 
def checker(x): 
    if(len(x)%2==0): 
        if x[0:len(x)//2] == x[len(x)//2:len(x)]: 
            return x 
        else: 
            return 0 
    else: 
        return 0 

for i in data:
    r = i.split('-')
    for j in range(int(r[0]),int(r[1])+1): 
        sum += int(checker(str(j)))
print(sum)


