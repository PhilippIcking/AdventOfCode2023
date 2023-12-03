with open("input03.txt") as f:
    engine_map = f.read().splitlines()

new_engine_map = []
for line in engine_map:
    new_l = "." + line + "."
    new_engine_map.append(new_l)
new_engine_map.append("." * len(new_engine_map[1]))
new_engine_map.insert(0, "." * len(new_engine_map[1]))


def adj_sym(y_koor, x_koor, k):
    adj_char = []
    for char in new_engine_map[y_koor - 1][x_koor - k:x_koor + 2]:
        adj_char.append(char)
    adj_char.append(new_engine_map[y_koor][x_koor - k])
    adj_char.append(new_engine_map[y_koor][x_koor + 1])
    for char in new_engine_map[y_koor + 1][x_koor - k:x_koor + 2]:
        adj_char.append(char)
    for c in adj_char:
        if not c.isdigit() and c != ".":
            return True
    return False


# Part 1

numbers = []

for y in range(1, len(new_engine_map)):
    x = 1
    while x < len(new_engine_map[y]):
        curr_num = ""
        if new_engine_map[y][x].isdigit():
            curr_num = curr_num.__add__(new_engine_map[y][x])
            while new_engine_map[y][x + 1].isdigit():
                curr_num = curr_num.__add__(new_engine_map[y][x + 1])
                x += 1
            if adj_sym(y, x, len(curr_num)):
                numbers.append(int(curr_num))
            x += 1
        else:
            x += 1

print(sum(numbers))


# Part 2

gears = []


def get_num(y_koor, x_koor):
    num = new_engine_map[y_koor][x_koor]
    k = 1
    while new_engine_map[y_koor][x_koor - k].isdigit():
        num = new_engine_map[y_koor][x_koor - k] + num
        k += 1

    k = 1
    while new_engine_map[y_koor][x_koor + k].isdigit():
        num = num + new_engine_map[y_koor][x_koor + k]
        k += 1

    return num


for y in range(1, len(new_engine_map)):
    for x in range(1, len(new_engine_map[y])):
        if new_engine_map[y][x] == "*":
            gears_curr = []
            for dif in [-1, 0, 1]:
                if new_engine_map[y - 1][x + dif].isdigit():
                    gears_curr.append(get_num(y-1, x + dif))
                    if new_engine_map[y - 1][x + dif + 1] == "." and new_engine_map[y - 1][x + dif + 2].isdigit():
                        continue
                    else:
                        break
            if new_engine_map[y][x - 1].isdigit():
                gears_curr.append(get_num(y, x - 1))
            if new_engine_map[y][x + 1].isdigit():
                gears_curr.append(get_num(y, x + 1))
            for dif in [-1, 0, 1]:
                if new_engine_map[y + 1][x + dif].isdigit():
                    gears_curr.append(get_num(y+1, x + dif))
                    if new_engine_map[y + 1][x + dif + 1] == "." and new_engine_map[y + 1][x + dif + 2].isdigit():
                        continue
                    else:
                        break
            if len(gears_curr) == 2:
                gears.append(int(gears_curr[0]) * int(gears_curr[1]))

print(sum(gears))
