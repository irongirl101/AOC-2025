f = open("input.txt")
data = f.readlines()

ops = data.pop().strip()
ops = ops.split()
result = 0 

data = [line.replace('\n', '') for line in data]
max_len = max(len(line) for line in data) if data else 0
data = [line.ljust(max_len) for line in data]
values = []
for i in range(max_len): 
    num = [] 
    for j in range(len(data)): 
        num.append(data[j][i])
    
    number = ""
    for k in num:
        number+=k 
    values.append(number)

l = [] 
matrix = [] 
for i in values: 
    if i.strip() == "": 
        if l:
            matrix.append(l)
            l = [] 
    else: 
        l.append(i)
if l: 
    matrix.append(l)

'''def extract(l): 
    # lets say my l = ['123','45','6']
    helper = [] 
    pointer = -1 
    limit = len(max(l,key=len))
    while abs(pointer)<=limit:
        s=''
        for i in range(len(l)): 
            if len(l[i])>=abs(pointer):
                s+=l[i][pointer]

        pointer-=1
        helper.append(s)

    return helper'''


for i in range(len(matrix)): 
    if i>=len(ops): 
        break
    op = ops[i]
    nums = [] 

    for j in matrix[i]: 
        if j.strip(): 
            nums.append(int(j)) 

    if op == '+': 
        s = 0 
        for k in nums: 
            s+=k 
        result+=s

    if op == '*': 
        prod = 1 
        for k in nums:
            prod *= k
        result += prod


print(result)
        
