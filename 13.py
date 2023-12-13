with open("input13.txt") as f:
    maps = f.read().split("\n\n")


def mirror_col(m):
    for char_cou in range(1, len(m[0])):
        mir_distance = min(char_cou, len(m[0])-char_cou)
        chars_left = []
        chars_right = []
        for x in range(mir_distance):
            for y in range(len(m)):
                chars_left.append(m[y][char_cou-x-1])
                chars_right.append(m[y][char_cou+x])
        if chars_left == chars_right:
            return char_cou

    return 0


def mirror_row(m):
    for row_cou in range(1, len(m)):
        mir_distance = min(row_cou, len(m)-row_cou)
        if m[row_cou-mir_distance:row_cou] == list(m[row_cou:row_cou+mir_distance].__reversed__()):
            return row_cou*100

    return 0


def mirror_col_modi(m):
    for char_cou in range(1, len(m[0])):
        mir_distance = min(char_cou, len(m[0]) - char_cou)
        equal_count = 0
        chars_left = []
        chars_right = []
        for x in range(mir_distance):
            for y in range(len(m)):
                chars_left.append(m[y][char_cou - x - 1])
                chars_right.append(m[y][char_cou + x])
        for c in range(len(chars_right)):
            if chars_left[c] == chars_right[c]:
                equal_count += 1
        if equal_count == (len(chars_right)-1):
            return char_cou

    return 0


def mirror_row_modi(m):
    for row_cou in range(1, len(m)):
        mir_distance = min(row_cou, len(m) - row_cou)
        a = m[row_cou - mir_distance:row_cou]
        b = list(m[row_cou:row_cou + mir_distance].__reversed__())
        equal_count = 0
        for x in range(len(a)):
            for y in range(len(a[x])):
                if a[x][y] == b[x][y]:
                    equal_count += 1
        if equal_count == (len(a)*len(a[0])-1):
            return row_cou * 100

    return 0


cou1 = 0
cou2 = 0

for m in maps:
    m = m.splitlines()

    # Part 1
    cou1 += mirror_col(m)
    cou1 += mirror_row(m)

    # Part 2
    cou2 += mirror_col_modi(m)
    cou2 += mirror_row_modi(m)

print(cou1)
print(cou2)
