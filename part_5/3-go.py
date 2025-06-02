# Write your solution here
#game board takes 2-D array which consists of int values
# ''' 0: empty square
#     1: player 1 game piece
#     2: player 2 game piece'''
# '''imagine [[---], <-row 
#             [---], in each row is square
#             [---]]'''
            
def who_won(game_board: list):
    player1_count = 0
    player2_count = 0
    for row in game_board:
        for square in row:
            if square == 2:
                player2_count += 1
            elif square == 1:
                player1_count += 1
    if player1_count > player2_count:
        return 1
    elif player2_count > player1_count:
        return 2
    else:
        return 0

if __name__ == "__main__":
#testing a testcase
    print(who_won([[1]]))