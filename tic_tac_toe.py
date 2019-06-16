def game():
    game_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    end = False
    win_possibilities = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    def draw():
        print(game_board[0], game_board[1], game_board[2])
        print(game_board[3], game_board[4], game_board[5])
        print(game_board[6], game_board[7], game_board[8])
        print()

    def player1():
        n = choose_number()
        if game_board[n] == "X" or game_board[n] == "O":
            print("\nYou can't go there. Try again")
            player1()
        else:
            game_board[n] = "X"

    def player2():
        n = choose_number()
        if game_board[n] == "X" or game_board[n] == "O":
            print("\nYou can't go there. Try again")
            player2()
        else:
            game_board[n] = "O"

    def choose_number():
        while True:
            while True:
                a = input()
                try:
                    a  = int(a)
                    a -= 1
                    if a in range(0, 9):
                        return a
                    else:
                        print("\nThat's not on the game_board. Try again")
                        continue
                except ValueError:
                   print("\nThat's not a number. Try again")
                   continue

    def check_game_board():
        count = 0
        for a in win_possibilities:
            if game_board[a[0]] == game_board[a[1]] == game_board[a[2]] == "X":
                print("Player 1 Wins!\n")
                print("Congratulations!\n")
                return True

            if game_board[a[0]] == game_board[a[1]] == game_board[a[2]] == "O":
                print("Player 2 Wins!\n")
                print("Congratulations!\n")
                return True
        for a in range(9):
            if game_board[a] == "X" or game_board[a] == "O":
                count += 1
            if count == 9:
                print("The game ends in a Tie\n")
                return True

    while not end:
        draw()
        end = check_game_board()
        if end == True:
            break
        print("Player 1 choose where to place a X")
        player1()
        print()
        draw()
        end = check_game_board()
        if end == True:
            break
        print("Player 2 choose where to place a O")
        player2()
        print()

    if input("Play again (y/n)\n") == "y":
        print()
        game()

game()