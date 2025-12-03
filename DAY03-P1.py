f = open("input.txt",'r')
data = f.readlines()
s = 0 

for i in data: 
    greatest = 0
    i = i.strip()
    j = 0
    while j<len(i):
        for k in range(j+1,len(i)): 
            if greatest==0: 
                greatest = int(i[j])*10 + int(i[k])
            elif greatest< int(i[j])*10 + int(i[k]): 
                greatest = int(i[j])*10 + int(i[k]) 
        j+=1
    s+=greatest
print(s)
