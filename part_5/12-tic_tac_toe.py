# Write your solution here
def play_turn(game_board: list, x: int, y: int, piece: str):
    if -1 < x < 3 and -1 < y < 3:
        if game_board[y][x] == "":
            game_board[y][x] = piece
            return True
    return False



if __name__ == "__main__":
#failed below test case
    game_board = [['', 'O', ''], ['', '', ''], ['', 'X', 'O']]
    print(play_turn(game_board, -1, 1, "X"))
    print(game_board)