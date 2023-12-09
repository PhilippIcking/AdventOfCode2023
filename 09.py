with open("input09.txt") as f:
    data = f.read().splitlines()

cou1 = 0
cou2 = 0

for line in data:
    curr_map = [[int(x) for x in line.split(" ")]]
    while len(set(curr_map[-1])) != 1:
        curr_line = []
        for x in range(len(curr_map[-1]) - 1):
            curr_line.append(curr_map[-1][x + 1] - curr_map[-1][x])
        curr_map.append(curr_line)
    cou = 0
    for x in curr_map:
        cou += x[-1]
    cou1 += cou

    cou = curr_map[-1][0]
    for x in range(2, len(curr_map)+1):
        cou = curr_map[-x][0] - cou
    cou2 += cou

print(cou1)
print(cou2)
