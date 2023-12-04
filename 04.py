with open("input04.txt") as f:
    data = f.read().replace("  ", " ").splitlines()


cou1 = 0

cards = [1 for _ in range(len(data))]

for counter, d in enumerate(data):
    _, game = d.split(": ")
    num, wins = game.split(" | ")
    num_list = [int(x) for x in num.split(" ")]
    wins_list = [int(x) for x in wins.split(" ")]
    inter = set(wins_list).intersection(set(num_list))
    if len(inter) > 0:
        cou1 += 2**(len(inter)-1)

    for x in range(1, len(inter)+1):
        cards[counter + x] = cards[counter] + cards[counter + x]

print(cou1)
print(sum(cards))
