with open("input15.txt") as f:
    data = f.read().split(",")


# Part 1
cou1 = 0
for x in data:
    curr_val = 0
    for y in x:
        curr_val += ord(y)
        curr_val = (curr_val * 17) % 256
    cou1 += curr_val

print(cou1)


# Part 2
hash_map = {x: {} for x in range(256)}

for x in data:
    ind = 0
    if x.__contains__("="):
        st, num = x.split("=")
        for s in st:
            ind += ord(s)
            ind = (ind * 17) % 256
        hash_map[ind][st] = int(num)

    if x.__contains__("-"):
        st, num = x.split("-")
        for s in st:
            ind += ord(s)
            ind = (ind * 17) % 256
        if st in hash_map[ind]:
            del hash_map[ind][st]

cou2 = 0
for x in range(256):
    for y in range(len(list(hash_map[x]))):
        cou2 += (y+1)*hash_map[x][list(hash_map[x])[y]]*(x+1)

print(cou2)
