f = open("data.txt","r")
data = f.readline() 
data = data.split(",")

for i in data: 
    i = i.split("-")
    
