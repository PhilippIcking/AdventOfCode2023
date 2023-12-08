from math import lcm
with open("input08.txt") as f:
    data = f.read().splitlines()

instr = data[0]
char_dict = {}

for x in data[2:]:
    a, b = x.split(" = (")
    c, d = b.split(", ")
    char_dict.__setitem__(a, (c, d[:-1]))


# Part 1

curr_char = "AAA"
steps = 0
while curr_char != "ZZZ":
    if instr[steps % len(instr)] == "L":
        d = 0
    else:
        d = 1
    curr_char = char_dict[curr_char][d]
    steps += 1
print(steps)


# Part 2

char_list =[]
for x in char_dict:
    if x[-1] == "A":
        char_list.append(x)

step_list = []
for c in char_list:
    steps = 0
    curr_char = c
    while curr_char[-1] != "Z":
        if instr[steps % len(instr)] == "L":
            d = 0
        else:
            d = 1
        curr_char = char_dict[curr_char][d]
        steps += 1
    step_list.append(steps)
print(lcm(*step_list))
