with open("input07.txt") as f:
    data = f.read().splitlines()

# Part 1

rules = {"A": 1, "K": 2, "Q": 3, "J": 4, "T": 5, "9": 6, "8": 7, "7": 8, "6": 9, "5": 10, "4": 11, "3": 12, "2": 13}


def hand_value(hand):
    return [rules[card[0]] for card in hand]


five = []
four = []
full_house = []
three = []
two_two = []
two_one = []
high_card = []

for x in data:
    hand, bid = x.split(" ")
    hand_values = hand_value(hand)

    amount = []
    for card in hand:
        amount.append(hand.count(card))
    amount = sorted(list(amount))

    if amount[-1] == 5:
        five.append((x, hand_values))
    elif amount[-1] == 4:
        four.append((x, hand_values))
    elif amount[-1] == 3:
        if amount[-4] == 2:
            full_house.append((x, hand_values))
        else:
            three.append((x, hand_values))
    elif amount[-1] == 2:
        if amount[-3] == 2:
            two_two.append((x, hand_values))
        else:
            two_one.append((x, hand_values))
    elif amount[-1] == 1:
        high_card.append((x, hand_values))

five.sort(key=lambda x: x[1])
four.sort(key=lambda x: x[1])
full_house.sort(key=lambda x: x[1])
three.sort(key=lambda x: x[1])
two_two.sort(key=lambda x: x[1])
two_one.sort(key=lambda x: x[1])
high_card.sort(key=lambda x: x[1])

cou1 = 0
for counter, x in enumerate(list(reversed([*five, *four, *full_house, *three, *two_two, *two_one, *high_card]))):
    _, bid = x[0].split(" ")
    cou1 += (counter + 1) * int(bid)
print(cou1)


# Part 2

rules = {"A": 1, "K": 2, "Q": 3, "T": 4, "9": 5, "8": 6, "7": 7, "6": 8, "5": 9, "4": 10, "3": 11, "2": 12, "J": 13}

five = []
four = []
full_house = []
three = []
two_two = []
two_one = []
high_card = []

for x in data:
    hand, bid = x.split(" ")
    hand_values = hand_value(hand)

    amount = []
    for card in hand:
        amount.append(hand.count(card))
    amount = sorted(list(amount))
    for _ in range(hand.count("J")):
        if hand.count("J") is amount[-1] and hand.count("J") != 5:
            amount[-hand.count("J")-1] += 1
        else:
            amount[-1] += 1
    amount = sorted(list(amount))

    if amount[-1] >= 5:
        five.append((x, hand_values))
    elif amount[-1] == 4:
        four.append((x, hand_values))
    elif amount[-1] == 3:
        if amount[-4] == 2:
            full_house.append((x, hand_values))
        else:
            three.append((x, hand_values))
    elif amount[-1] == 2:
        if amount[-3] == 2:
            two_two.append((x, hand_values))
        else:
            two_one.append((x, hand_values))
    elif amount[-1] == 1:
        high_card.append((x, hand_values))

five.sort(key=lambda x: x[1])
four.sort(key=lambda x: x[1])
full_house.sort(key=lambda x: x[1])
three.sort(key=lambda x: x[1])
two_two.sort(key=lambda x: x[1])
two_one.sort(key=lambda x: x[1])
high_card.sort(key=lambda x: x[1])

cou2 = 0
for counter, x in enumerate(list(reversed([*five, *four, *full_house, *three, *two_two, *two_one, *high_card]))):
    _, bid = x[0].split(" ")
    cou2 += (counter + 1) * int(bid)
print(cou2)
