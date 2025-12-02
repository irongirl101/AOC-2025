f = open("input.txt","r")
data = f.readline() 
data = data.split(",")
sum = 0 

def pattern(x,y): 
    repeat = len(x)//y 
    string = x[0:y] * repeat
    if x == string: 
        return True
    else: 
        return False
    
def checker(x):
    for i in range(1,len(x)//2 +1): 
        if len(x)%i == 0: 
            if pattern(x,i): 
                return x 
            



"""def pattern_candidate(x,y): 
    
def pattern(x):
    ind = x[0] 
    s = x[0]
    for i in range(len(x)): 
        if i == 0:
            continue
        elif x[i] == ind: 
            break 
        else: 
            s+=x[i]
    return s 
    
def checker(x): 
    y = pattern(x) 
    i = 0 
    flag = True
    if y == x: 
        return flag 
   
    while i+len(y)<=len(x):
        if x[i:i+len(y)] == y: 
            i += (len(y))
        else: 
            flag = False
            break
    
    return flag
   """         
        
for i in data: 
    i = i.split("-")
    for i in range(int(i[0]),int(i[1])+1): 
        result = checker(str(i))
        if result:
            sum += int(result)
print(sum)


