f = open("input.txt")
data = f.readlines()
s = 0 
for i in data: 
    i = i.strip()
    greatest = []
    pops = len(i) - 12
    for j in i:
        while greatest and greatest[-1]<j and pops>0: 
            greatest.pop()
            pops-=1
        greatest.append(j)
    if pops>0: 
        greatest = greatest[:-pops]
    greatest = "".join(greatest)
    s+=int(greatest)
print(s)
