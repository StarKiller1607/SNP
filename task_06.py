class WrongNumberOfPlayersError(Exception):
    __module__ = Exception.__module__

class NoSuchStrategyError(Exception):
    __module__ = Exception.__module__

def rps_game_winner(game):
    if len(game) != 2:
        raise WrongNumberOfPlayersError
    if game[0][1] not in 'RPS' or game[1][1] not in 'RPS':
        raise NoSuchStrategyError
    if game[0][1] == game[1][1]:
        return game[0][0] + ' ' + game[0][1]
    if game[0][1] == 'R' and game[1][1] == 'P':
        return game[1][0] + ' ' + game[1][1]
    if game[0][1] == 'P' and game[1][1] == 'R':
        return game[0][0] + ' ' + game[0][1]
    if game[0][1] == 'R' and game[1][1] == 'S':
        return game[0][0] + ' ' + game[0][1]
    if game[0][1] == 'S' and game[1][1] == 'R':
        return game[1][0] + ' ' + game[1][1]
    if game[0][1] == 'P' and game[1][1] == 'S':
        return game[1][0] + ' ' + game[1][1]
    if game[0][1] == 'S' and game[1][1] == 'P':
        return game[0][0] + ' ' + game[0][1]