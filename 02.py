with open("input02.txt") as f:
    games = f.read().splitlines()


# Part 1&2

rules = {
    "red": 12,
    "green": 13,
    "blue": 14
}

all_ids = []
not_pos = []

counter = 0

for game in games:
    max_values = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    a, b = game.split(":")
    _, g_nr = a.split(" ")
    sets = b.split(";")
    for s in sets:
        colors = s.split(",")
        for color in colors:
            num, col = color[1:].split(" ")
            if int(num) > rules[col]:
                not_pos.append(int(g_nr))

            if int(num) > max_values[col]:
                max_values[col] = int(num)
    all_ids.append(int(g_nr))
    counter += max_values["blue"]*max_values["green"]*max_values["red"]


print(f"Part 1: {sum(set(all_ids)) - sum(set(not_pos))}")
print(f"Part 2: {counter}")
