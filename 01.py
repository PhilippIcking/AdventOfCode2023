with open("input01.txt") as f:
    data = f.read().splitlines()

data_parsed = []
for x in data:
    data_parsed.append("".join([i for i in x if i.isdigit()]))

# Part 1
cou1 = 0
for x in data_parsed:
    cou1 += int(f"{x[0]}" + f"{x[-1]}")
print(cou1)

# Part 2
cou2 = 0
digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
dict_digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}
for x in data:
    first_d = 0
    found = False
    while not found:
        for y in range(len(x)):
            if x[y].isdigit():
                first_d = int(x[y])
                found = True
                break
            else:
                try:
                    if x[y:y + 3] in digits:
                        first_d = dict_digits[x[y:y + 3]]
                        found = True
                        break

                    elif x[y:y + 4] in digits:
                        first_d = dict_digits[x[y:y + 4]]
                        found = True
                        break

                    elif x[y:y + 5] in digits:
                        first_d = dict_digits[x[y:y + 5]]
                        found = True
                        break
                finally:
                    pass

    else:
        pass

    second_d = 0
    found = False
    while not found:
        for y in range(len(x)):
            if x[y].isdigit():
                second_d = int(x[y])
                found = True

            else:
                try:
                    if x[y:y + 3] in digits:
                        second_d = dict_digits[x[y:y + 3]]
                        found = True

                    elif x[y:y + 4] in digits:
                        second_d = dict_digits[x[y:y + 4]]
                        found = True

                    elif x[y:y + 5] in digits:
                        second_d = dict_digits[x[y:y + 5]]
                        found = True

                finally:
                    pass
    else:
        pass

    cou2 += first_d * 10 + second_d
print(cou2)
