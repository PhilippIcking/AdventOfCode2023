import itertools

with open("input11.txt") as f:
    input_data = f.read().splitlines()


def cosmic_path(data, ex_faktor):

    # Find Galaxies
    gal_positions = []
    for y, a in enumerate(data):
        for x, b in enumerate(a):
            if b == "#":
                gal_positions.append([y, x])

    # Correct positions with empty lines
    expand_faktor = ex_faktor - 1
    dif_cou = 0
    for y_cou, a in enumerate(data):
        if "#" not in a:
            for pos in range(len(gal_positions)):
                y, x = gal_positions[pos]
                if y > y_cou + dif_cou:
                    gal_positions[pos] = [y + expand_faktor, x]
            dif_cou += expand_faktor

    # Correct postions with empty rows
    dif_cou = 0
    for x_cou, _ in enumerate(data[0]):
        gal_cou = 0
        for a in data:
            if a[x_cou] == "#":
                gal_cou += 1
        if gal_cou == 0:
            for pos in range(len(gal_positions)):
                y, x = gal_positions[pos]
                if x > x_cou + dif_cou:
                    gal_positions[pos] = [y, x + expand_faktor]
            dif_cou += expand_faktor

    cou1 = 0

    def get_distance(pair):
        pos1 = pair[0]
        pos2 = pair[1]
        y1, x1 = pos1
        y2, x2 = pos2
        return abs(y2 - y1) + abs(x2 - x1)

    # Get distances
    for pair in list(itertools.combinations(gal_positions, 2)):
        cou1 += get_distance(pair)

    return cou1


print(cosmic_path(input_data, 2))  # Part 1
print(cosmic_path(input_data, 1000000))  # Part 2
