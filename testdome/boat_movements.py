# https://www.testdome.com/questions/python/boat-movements/135037

def can_travel_to(game_matrix, from_row, from_column, to_row, to_column):
    pass

if __name__ == "__main__":
    game_matrix = [
        [False, True,  True,  False, False, False],
        [True,  True,  True,  False, False, False],
        [True,  True,  True,  True,  True,  True],
        [False, True,  True,  False, True,  True],
        [False, True,  True,  True,  False, True],
        [False, False, False, False, False, False],
    ]

    print(can_travel_to(game_matrix, 3, 2, 2, 2)) # True, Valid move
    print(can_travel_to(game_matrix, 3, 2, 3, 4)) # False, Can't travel through land
    print(can_travel_to(game_matrix, 3, 2, 6, 2)) # False, Out of bounds