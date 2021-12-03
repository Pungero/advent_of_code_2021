#f = open("example.txt", "r")
f = open("input.txt", "r")
prev = None
increases = 0
for line in f:
    current = int(line)
    if (prev != None and prev < current):
        increases = increases + 1
    prev = current

print(increases)

