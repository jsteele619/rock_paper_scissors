import random
    
def time_to_play():
    
    game = True

    computer_wins = 0
    player_wins = 0

    while game == True:
        print("Let's play a game of Rock, Paper, Scissors")
        print("    ")
        choices = ["rock", "paper", "scissors"]
        print(f"Choose your weapon: {choices[0]}, {choices[1]}, or {choices[2]}")

        player_choice = input().lower()
        computer_choice = random.choice(choices)
        print("   ")
        if player_choice == "rock":
            if computer_choice == "paper":
                print(f"Player: {player_choice}, Computer: {computer_choice}")
                print("The computer won!")
                computer_wins += 1
            elif computer_choice == "scissors":
                print(f"Player: {player_choice}, Computer: {computer_choice}")
                print("You won!")
                player_wins += 1
            elif computer_choice == "rock":
                print(f"Player: {player_choice}, Computer: {computer_choice}")
                print("It's a tie!")
        
        elif player_choice == "paper":
            if computer_choice == "scissors":
                print(f"Player: {player_choice}, Computer: {computer_choice}")
                print("The computer won!")
                computer_wins += 1

            elif computer_choice == "rock":
                print(f"Player: {player_choice}, Computer: {computer_choice}")
                print("You won!")
                player_wins += 1
            elif computer_choice == "paper":
                print(f"Player: {player_choice}, Computer: {computer_choice}")
                print("It's a tie!")

        elif player_choice == "scissors":
            if computer_choice == "rock":
                print(f"Player: {player_choice}, Computer: {computer_choice}")
                print("The computer won!")
                computer_wins += 1
            elif computer_choice == "paper":
                print(f"Player: {player_choice}, Computer: {computer_choice}")
                print("You won!")
                player_wins += 1
            elif computer_choice == "scissors":
                print(f"Player: {player_choice}, Computer: {computer_choice}")
                print("It's a tie!")

        print(f"Player Wins: {player_wins}, Computer Wins: {computer_wins}")
        print("  ")
        print("Would you like to play again? yes or no?")
        answer = input().lower()

        if answer == "yes":
            game == True
        else:
            if player_wins > computer_wins:
                print(f"The player won with {player_wins} wins")
            elif player_wins == computer_wins:
                print(f"It was a tie with {player_wins} apiece")
            elif player_wins < computer_wins:
                print(f"The computer won with {computer_wins}")
            game = False


time_to_play()
