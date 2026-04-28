from game.logic import get_computer_choice, decide_winner
from game.utils import display_menu, get_player_choice

player_score = 0
computer_score = 0

while True:
    display_menu()
    option = input("Enter your choice: ")

    if option == "1":
        player = get_player_choice()
        computer = get_computer_choice()

        print("Computer chose:", computer)

        result = decide_winner(player, computer)

        if result == "draw":
            print("It's a draw!")
        elif result == "player":
            print("You win!")
            player_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

    elif option == "2":
        print("\nScore:")
        print("You:", player_score)
        print("Computer:", computer_score)

    elif option == "3":
        print("Exiting game...")
        break

    else:
        print("Invalid choice! Try again.")