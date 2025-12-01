pointer = 50
count = 0 

f = open('input.txt','r')
data = f.readlines()

def count_zeroes(pointer,atoi,dir): 
    
    if dir == 'R': 
        return (pointer+atoi)//100 
    else: 
        if pointer == 0: 
            pointer = 100

        if(atoi>=pointer): 
            return 1 + (atoi-pointer) // 100
        else: 
            return 0 

for i in data: 
    atoi = int(i[1:])
    if(i[0]=='R'): 
       count += count_zeroes(pointer,atoi,'R')
       pointer = (pointer + atoi) % 100
       
    else: 
        count += count_zeroes(pointer,atoi,'L')
        pointer = (pointer - atoi) % 100 
    


print(count)


