# https://www.testdome.com/questions/python/boat-movements/135037

def can_travel_to(game_matrix, from_row, from_column, to_row, to_column):

    

    pass

if __name__ == "__main__":
    game_matrix = [
        [False, False, True, True, False],
        [False, False, True, False, False],
        [False, False, True, True, False],
        [False, True, False, True, False],
        [False, False, True, False, False]
    ]

    print(can_travel_to(game_matrix, 2, 2, 0, 2))
    print(can_travel_to(game_matrix, 2, 2, 2, 1))
    print(can_travel_to(game_matrix, 2, 2, 2, 3))
    print(can_travel_to(game_matrix, 2, 2, 4, 2))