def get_next_move():
    try:
        while True:
            yield input()
    except:
        pass

deck = [x for x in range(10007)]
for move in get_next_move():
    if move.startswith('deal into'):
        deck.reverse()
    elif move.startswith('cut'):
        n = int(move.split()[-1])
        deck = deck[n:] + deck[:n]
    elif move.startswith('deal with'):
        n = int(move.split()[-1])
        tmp = deck[:]
        idx = 0
        for i in deck:
           tmp[idx] = i
           idx = (idx + n) % len(deck)
        deck = tmp

print(deck.index(2019))

