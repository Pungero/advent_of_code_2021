gamma_arr = None
epsilon_arr = None
n_lines = 0

#f = open("example.txt", "r")
f = open("input.txt", "r")
for line in f:
    if len(line) == 0:
        continue
    line = line.strip()
    if gamma_arr == None:
        gamma_arr = [0] * len(line)
        epsilon_arr = [0] * len(line)
    print(line)
    n_lines = n_lines + 1
    for i in range (0, len(line) - 1):
        c = line[i]
        if c == '1':
            gamma_arr[i] += 1
    

# Convert to binary arrays
for i in range (0, len(gamma_arr)):
    one_sum = gamma_arr[i]
    gamma_arr[i] = one_sum >= n_lines / 2
    epsilon_arr[i] = one_sum < n_lines / 2

# Convert binary arrays to numbers

gamma = 0
for ele in gamma_arr:
    gamma = (gamma << 1) | ele

epsilon = 0
for ele in epsilon_arr:
    epsilon = (epsilon << 1) | ele
# Multiply

print(gamma_arr)
print(epsilon_arr)
print(gamma)
print(epsilon)
print(gamma * epsilon)

