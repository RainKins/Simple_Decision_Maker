# Needed to randomize choices
import random


# Define the restart program option
def restart():
    restart_choice = input("\nRestart (Y/N): ")
    restart_choice = restart_choice.upper()

    if restart_choice == "Y":
        print("\n" * 10)
        main()
    elif restart_choice == "N":
        print("\nOkay. Good luck with your decision!")
    else:
        print("Invalid key. Try again")
        restart()


# The program must be ran in main
def main():
    # declare choices as a list
    choices = []

    # Ask user for the amount of choices they have for their decision
    option_count = input("How many options are you debating? ")
    print("\n")

    # Check for any keys that can't be changed into an integer
    if option_count.isnumeric():

      # Check for multiple choices
      if int(option_count) > 1:
          # Take the user's option_count input to create a for loop to add their options to the choices list
          for i in range(int(option_count)):
              option = input('Option: ')
              choices.append(option)

          # Shuffle choices list in order to get a randomized result multiple times, rather than the same random choice from the first run
          for i in range(len(choices) + 1):
              random.shuffle(choices)

          decision = choices[0]

          # Display user's decision
          print('\nYour randomized decision is ' + '"' + decision + '"' + '.')

          # Ask user if they want to  restart the program
          restart()

      else:
        # If there isn't enough choices, restart the program
        print("Not enough choices to choose from. Try again.")
        print("\n" * 9)
        main()

    # If key can't be changed into an integer, restart program
    else:
        print("Invalid Key. Try again.")
        print("\n" * 9)
        main()


main()
