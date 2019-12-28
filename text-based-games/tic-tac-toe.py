# Tic tac toe
# Author: Matthews Ma


def draw(state):
    """Function that draws out the game board given the state."""

    print(" " + state[0] + " | " + state[1] + " | " + state[2])

    print("___________")

    print(" " + state[3] + " | " + state[4] + " | " + state[5])

    print("___________")

    print(" " + state[6] + " | " + state[7] + " | " + state[8])


def check_win(state, player):
    """Check whether the specified player has won."""

    if state[0] == state[1] == state[2] == player or \
            state[3] == state[4] == state[5] == player or \
            state[6] == state[7] == state[8] == player or \
            state[0] == state[3] == state[6] == player or \
            state[1] == state[4] == state[7] == player or \
            state[2] == state[5] == state[8] == player or \
            state[0] == state[4] == state[8] == player or \
            state[2] == state[4] == state[6] == player:
        return True


def main():
    """Main game loop."""

    # Draw board with this state so the square names are clear.
    helper_state = ["1", "2", "3",
                    "4", "5", "6",
                    "7", "8", "9"]

    draw(helper_state)

    # Return state to starting position.
    state = [" ", " ", " ",
             " ", " ", " ",
             " ", " ", " "]

    # When finished is true, the game loop ends.
    finished = False

    while not finished:

        # Alternate through players
        for player in ["X", "O"]:

            # Make sure the move is not valid so the while loop will run.
            move = -1

            # If the move is not valid, keep asking the player for a move.
            while move not in [0, 1, 2, 3, 4, 5, 6, 7, 8] or state[move] != " ":
                print()

                # The user inputs a move from 1-9 but this number is one more
                # than the index in the state list.
                # .format() is a special command that makes putting variables
                # into strings cleaner.
                move = int(
                    input("Player {}'s move (1 - 9): ".format(player))) - 1

            # Change the state list to reflect the player's move.
            state[move] = player

            # Draw the game board.
            draw(state)

            # Check if the current player won from that move.
            if check_win(state, player):
                # If so, announce the winner and end the game by setting
                # finished to True.
                print()
                print("Player {} wins!".format(player))
                finished = True
                break
            # Check if there are no more empty spaces and no player has won -
            # in other words, a tie.
            elif " " not in state:
                # If so, end the game by setting finished to True.
                print()
                print("It's a tie.")
                finished = True
                break


# Some fancy code that runs the main game loop.
if __name__ == "__main__":
    main()
