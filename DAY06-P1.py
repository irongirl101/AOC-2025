f = open("input.txt")
data = f.readlines()

values = []
result = 0 
for i in data: 
    values.append(i.split())

for i in range(len(values[0])): #goes thru columns 
    s = 0 
    prod = 1 
    if values[len(values)-1][i] == '+': 
        for j in range(len(values)-1): #goes through rows 
            s+=int(values[j][i] )
        result+=s
    if values[len(values)-1][i] == '*': 
            for j in range(len(values)-1): #goes through rows 
                prod*=int(values[j][i])
            result+=prod

print(result)
        
