f = open("input.txt")
data = f.readlines()

def mergeOverlap(arr):
    n = len(arr)

    arr.sort()
    res = []

    # Checking for all possible overlaps
    for i in range(n):
        start = arr[i][0]
        end = arr[i][1]

        # Skipping already merged intervals
        if res and res[-1][1] >= end:
            continue

        # Find the end of the merged range
        for j in range(i + 1, n):
            if arr[j][0] <= end:
                end = max(end, arr[j][1])
        res.append([start, end])
    
    return res

ranges = [] 
for i in data: 
    i = i.split('-')
    ranges.append([int(i[0]), int(i[1])])

merged = mergeOverlap(ranges)
count = 0 

for i in merged: 
    count += (i[1]-i[0])+1

print(count)