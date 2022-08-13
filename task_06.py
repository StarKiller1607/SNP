class WrongNumberOfPlayersError(Exception):
    __module__ = Exception.__module__

class NoSuchStrategyError(Exception):
    __module__ = Exception.__module__

def rps_game_winner(game):
    if len(game) != 2:
        raise WrongNumberOfPlayersError
    if game[0][1] not in 'RPS' or game[1][1] not in 'RPS':
        raise NoSuchStrategyError
    win = ''
    if game[0][1] == game[1][1]:
        for i in range(2):
            win += game[0][i]
            win += ' '
        return win
    if game[0][1] == 'R' and game[1][1] == 'P':
        for i in range(2):
            win += game[1][i]
            win += ' '
        return win
    if game[0][1] == 'P' and game[1][1] == 'R':
        for i in range(2):
            win += game[0][i]
            win += ' '
        return win
    if game[0][1] == 'R' and game[1][1] == 'S':
        for i in range(2):
            win += game[0][i]
            win += ' '
        return win
    if game[0][1] == 'S' and game[1][1] == 'R':
        for i in range(2):
            win += game[1][i]
            win += ' '
        return win
    if game[0][1] == 'P' and game[1][1] == 'S':
        for i in range(2):
            win += game[1][i]
            win += ' '
        return win
    if game[0][1] == 'S' and game[1][1] == 'P':
        for i in range(2):
            win += game[0][i]
            win += ' '
        return win