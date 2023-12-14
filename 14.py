with open("input14.txt") as f:
    input_data = f.read().splitlines()

dish_map = []

for x in input_data:
    dish_map.append(list(x))


def north(dish):
    # North
    rock_count = 0
    cou1 = 0
    for x in range(len(dish[0])):
        for y in reversed(range(len(dish))):
            if dish[y][x] == "#" and rock_count > 0:
                dish[y+1][x] = rock_count
                cou1 += sum(range(len(dish)-(y+1)-rock_count+1, len(dish)-(y+1)+1))
                for z in range(rock_count):
                    dish[y + 1 + z][x] = "O"
                rock_count = 0
            elif dish[y][x] == "O":
                rock_count += 1
                dish[y][x] = "."
            if y == 0 and rock_count > 0:
                dish[y][x] = rock_count
                cou1 += sum(range(len(dish)-y-rock_count+1, len(dish)-y+1))
                for z in range(rock_count):
                    dish[y + z][x] = "O"
                rock_count = 0
    return dish, cou1


def west(dish):
    # West
    rock_count = 0
    for y in range(len(dish)):
        for x in reversed(range(len(dish[0]))):
            if dish[y][x] == "#" and rock_count > 0:
                dish[y][x+1] = rock_count
                for z in range(rock_count):
                    dish[y][x + 1 + z] = "O"
                rock_count = 0
            elif dish[y][x] == "O":
                rock_count += 1
                dish[y][x] = "."
            if x == 0 and rock_count > 0:
                dish[y][x] = rock_count
                for z in range(rock_count):
                    dish[y][x + z] = "O"
                rock_count = 0
    return dish


def south(dish):
    # South
    rock_count = 0
    for x in range(len(dish[0])):
        for y in range(len(dish)):
            if dish[y][x] == "#" and rock_count > 0:
                dish[y-1][x] = rock_count
                for z in range(rock_count):
                    dish[y - 1 - z][x] = "O"
                rock_count = 0
            elif dish[y][x] == "O":
                rock_count += 1
                dish[y][x] = "."
            if y == (len(dish)-1) and rock_count > 0:
                dish[y][x] = rock_count
                for z in range(rock_count):
                    dish[y - z][x] = "O"
                rock_count = 0
    return dish


def east(dish):
    # East
    rock_count = 0
    cou1 = 0
    for y in range(len(dish)):
        for x in range(len(dish[0])):
            if dish[y][x] == "#" and rock_count > 0:
                dish[y][x-1] = rock_count
                cou1 += (len(dish)-y) * rock_count
                for z in range(rock_count):
                    dish[y][x - 1 - z] = "O"
                rock_count = 0
            elif dish[y][x] == "O":
                rock_count += 1
                dish[y][x] = "."
            if x == (len(dish[0])-1) and rock_count > 0:
                dish[y][x] = rock_count
                cou1 += (len(dish)-y) * rock_count
                for z in range(rock_count):
                    dish[y][x - z] = "O"
                rock_count = 0
    return dish, cou1


# Part 1
_, part1 = north(dish_map.copy())
print(part1)

# Part 2
part2 = 0
for _ in range(1000):  # 1000 = 1000000000 % 42 + 23 * 42
    dish_map, _ = north(dish_map)
    dish_map = west(dish_map)
    dish_map = south(dish_map)
    dish_map, part2 = east(dish_map)

print(part2)


