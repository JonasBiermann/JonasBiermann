if int(input('player number, 1 or 2')) == 1:
    start = False
else:
    start = True

count = int(input('input count'))


def game(start, count):
    while count > 0:
        if start:
            take = count % 4
            if take == 0:
                take = 1
            count -= take
            print('pc takes', str(take))
            start = not start
        else:
            count -= int(input('insert your number, 1-3'))
            start = not start
        print(count)
    return winner(start)


def winner(player):
    if player:
        return 'player 2 is the winner'
    else:
        return 'player 1 ist the winner'


print(game(start, count))
