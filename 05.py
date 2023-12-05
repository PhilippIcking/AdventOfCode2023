with open("input05.txt") as f:
    data = f.read().split("\n\n")

# Part 1

_, s = data[0].split(": ")
seeds = [int(x) for x in s.split(" ")]

maps = []
for x in data[1:]:
    maps.append(x.split(":\n")[1].split("\n"))

seeds_history = [seeds, ]

for curr_map in maps:
    curr_seed = seeds_history.__getitem__(-1)
    for s_cou, seed in enumerate(curr_seed):
        for line in curr_map:
            dest, source, ran = [int(x) for x in line.split(" ")]
            if seed in range(source, source + ran):
                curr_seed[s_cou] = seed + (dest - source)
    seeds_history.append(curr_seed)

print(min(seeds_history[-1]))


# Part 2

_, s = data[0].split(": ")
seeds = [int(x) for x in s.split(" ")]

i = 0
found = False
while not found:
    s = i
    for curr_map in list(maps.__reversed__()):
        for line in list(curr_map.__reversed__()):
            dest, source, ran = [int(x) for x in line.split(" ")]
            if s in range(dest, dest + ran):
                s = s + (source - dest)
                break

    for x in range(int(len(seeds) / 2)):
        if (seeds[2 * x]) <= s < (seeds[2 * x] + seeds[2 * x + 1]):
            found = True
            print(f"Found: {i}")
    i += 1
    if i % 1000000 == 0:
        print(f"{i / 1000000} Mio")
