if int(input('What player do you want to be?')) == 1:
    start = False
else:
    start = True

count = int(input('What is the count for the game?'))


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
            count -= int(input('How many do you want to take away between 1 and 3?'))
            start = not start
        print(count)
    print(winner(start))


def winner(player):
    if player:
        return 'Spieler 1'
    else:
        return 'Spieler 2'


game(start, count)
