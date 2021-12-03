#f = open("example.txt", "r")
f = open("input.txt", "r")
prev = None
increases = 0
arr = []
for line in f:
    arr.append(int(line))
   
for i in range(0, len(arr)-2):
    current = 0
    for j in range(i, i+3):
        current = current + arr[j]
    if (prev != None and prev < current):
        increases = increases + 1
    prev = current
    print(current)

print(increases)

