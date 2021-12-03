def oxygen_rating(arrs, i):
    mc = most_common(arrs, i)
    filtered_arr = [arr for arr in arrs if arr[i] == mc]

    if len(filtered_arr) == 1:
        return filtered_arr[0]

    return oxygen_rating(filtered_arr, i + 1)



def co2_scrubber_rating(arrs, i):
    least_common = 1 if most_common(arrs, i) == 0 else 0
    filtered_arr = [arr for arr in arrs if arr[i] == least_common]

    if len(filtered_arr) == 1:
        return filtered_arr[0]

    return co2_scrubber_rating(filtered_arr, i + 1)



def most_common(arrs, i):
    n_ones = 0
    for arr in arrs:
        n_ones = n_ones + arr[i]

    return 1 if n_ones >= len(arrs) / 2 else 0



arrs = [] 

#f = open("example.txt", "r")
f = open("input.txt", "r")
for line in f:
    line = line.strip()
    if len(line) == 0:
        continue
    inner_arr = []
    for c in line:
        inner_arr.append(1 if c == '1' else 0)
    arrs.append(inner_arr)

oxygen_arr = oxygen_rating(arrs, 0) 
co2_arr = co2_scrubber_rating(arrs, 0)

# Convert binary arrays to numbers
oxygen = 0
for ele in oxygen_arr:
    oxygen = (oxygen << 1) | ele
co2 = 0
for ele in co2_arr:
    co2 = (co2 << 1) | ele

print(oxygen * co2)

