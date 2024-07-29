import random
def get_user_choice():
    user_choice= input("Enter your choice(rock,paper,or scissors): ").strip().lower()
    while user_choice not in ['rock','paper','scissors']:
        print("Invalid choice.please enter rock ,paper,or scissors.")
        user_choice = input("Enter your choice(rock,paper,or scissors.").strip().lower()
    return user_choice
def get_computer_choice():
    choice= ['rock','paper','scissors']
    return random.choice(choice)
def determine_winner(user_choice,computer_choice):
    if user_choice==computer_choice:
        return "It is a tie!"
    elif(user_choice=='rock' and computer_choice=='scissors')or \
         (user_choice=='paper' and computer_choice=='rock')or \
         (user_choice=='scissors' and computer_choice=='paper'):
        return "You win!"
    else:
        return"Computer wins!"

def play_game():
    user_choice=get_user_choice()
    computer_choice=get_computer_choice()
    print("\nYour choice: ",user_choice)
    print("Computer's choice: ",computer_choice)

    result= determine_winner(user_choice,computer_choice)
    print(result)
    return(result)
def main():
    user_score=0
    computer_score=0  
    play_again = True


    print("WELCOME TO ROCK-PAPER-SCISSORS!")     

    while play_again:
        result= play_game()
        if "win" in result.lower():
            user_score +=1
        elif "tie" not in result.lower():
            computer_score+=1
        print("\nScore -your: ",user_score," computer: ",computer_score)
        choice = input("\nDo you want to play again??? (yes/no):  ").strip().lower()
        while choice not in ['yes','no']:
            choice = input("wrong  input..please enter yes or no: ").strip().lower()
        if choice=='no':
            play_again=False

    print("\nThankyou for playing")
if _name=="main_":
    main()