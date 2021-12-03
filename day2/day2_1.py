#f = open("example.txt", "r")
f = open("input.txt", "r")
position = 0
depth = 0
for line in f:
    args = line.strip().split(' ')
    cmd = args[0]
    if cmd == 'forward':
        position = position + int(args[1])
    elif cmd == 'down':
        depth = depth + int(args[1])
    elif cmd == 'up':
        depth = depth - int(args[1])
   
print(position*depth)

