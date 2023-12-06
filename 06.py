with open("input06.txt") as f:
    data = f.read().splitlines()

# Part 1
t = data[0].split(":")[1].split(" ")
d = data[1].split(":")[1].split(" ")

t = [int(x) for x in t if x]
d = [int(x) for x in d if x]

cou1 = 1
for x in range(len(t)):
    time = t[x]
    dist = d[x]
    for y in range(time):
        if y*(time-y) > dist:
            cou1 *= abs((time-y)-y)+1
            break

print(cou1)

# Part 2
t = data[0].replace(" ", "").split(":")[1]
d = data[1].replace(" ", "").split(":")[1]
cou2 = 1
time = int(t)
dist = int(d)
for y in range(time):
    if y*(time-y) > dist:
        cou2 *= abs((time-y)-y)+1
        break

print(cou2)
