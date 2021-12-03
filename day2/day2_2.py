#f = open("example.txt", "r")
f = open("input.txt", "r")
aim = 0
position = 0
depth = 0
for line in f:
    args = line.strip().split(' ')
    cmd = args[0]
    num = int(args[1])
    if cmd == 'forward':
        position = position + num
        depth = depth + aim * num
    elif cmd == 'down':
        aim = aim + num 
    elif cmd == 'up':
        aim = aim - num 
   
print(position*depth)

