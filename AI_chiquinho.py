from math import inf as infinity
from random import choice

HUMAN = -1
COMP = +1

def evaluate(state):
    """
    Funcao para avaliacao heuristica do estado.
    Retorna +1 se a IA vence, -1 se o jogador vence e 0 se empata.
    """
    if wins(state, COMP):
        score = +1
    elif wins(state, HUMAN):
        score = -1
    else:
        score = 0

    return score


def wins(state, player):
    #Testando se o jogador venceu.
    
    win_state = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]],
    ]
    if [player, player, player] in win_state:
        return True
    else:
        return False


def game_over(state):
    """
    This function test if the human or computer wins
    :param state: the state of the current board
    :return: True if the human or computer wins
    """
    return wins(state, HUMAN) or wins(state, COMP) or len(empty_cells(state)) == 0


def empty_cells(state):
    """
    Cada celula vazia sera adcionada na lista de celulas
    Retorna uma lista de celulas vazia
    """
    cells = []
    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])

    return cells


def minimax(state, depth, player):
    """
    Funcao que escolhe a melhor jogada atraves
    do metodo de minimax. Retorna uma lista com 
    [melhor linha, melhor coluna, melhor pontuacao]
    """
    if player == COMP:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if depth == 0 or game_over(state):
        score = evaluate(state)
        return [-1, -1, score]

    for cell in empty_cells(state):
        x, y = cell[0], cell[1]
        state[x][y] = player
        score = minimax(state, depth - 1, -player)
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == COMP:
            if score[2] > best[2]:
                best = score  # max value
        else:
            if score[2] < best[2]:
                best = score  # min value

    return best


def ai_turn(board):
#Se depht < 9 utiliza a funcao minimax. 
#Se nao, escolhe uma posicao aleatoria.
    depth = len(empty_cells(board))
    if depth == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else:
        move = minimax(board, depth, COMP)
        x, y = move[0], move[1]
    board[x][y] = COMP
    
    return (x,y)
    