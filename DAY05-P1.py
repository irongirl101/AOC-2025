f = open("input.txt",'r')
data = f.readlines()

ranges = [] 
values = [] 

count = 0 

# extracting my data into ranges and values 
for i in data: 
    if i == "\n":
        pass
    elif '-' in i: 
        ranges.append(i)
    elif '-' not in i: 
        values.append(i)


# checking if values are in that range 
i = 0 
while i<len(values): 
    for j in ranges: 
        j = j.split('-')
        if int(j[0])<=int(values[i])<=int(j[1]): 
            count+=1 
            break
    i+=1

print(count)




