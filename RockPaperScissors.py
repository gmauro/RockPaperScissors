import random
def initial():
    answer= input('''What would you like to do
            1.Play Rock Paper Scissors
            2. Quit
            ''')
    if answer == "1" :
        print("you will now start to play a game against a computer player")
        rock_paper_scissors()
    elif answer == "2":
        print("OK, ")
    elif answer == str:
        print("please enter a number")
        initial()
    else:
        print("The answer wasn't acceptable please try again")
        initial()
def rock_paper_scissors():
    opponentsList = ['Rock','Paper','Scissors'];
    myChoice = input('Please enter a choice Rock, Paper, Scissors');
    opponentsRandomChoice =random.choice(opponentsList);
    print(opponentsRandomChoice)
    print("You have chosen",myChoice)
    print("Your opponent has choosen",opponentsRandomChoice)
    print("")
    if (opponentsRandomChoice == 'Rock' and myChoice == 'Paper'):
        print("You win")
        initial()
    elif(opponentsRandomChoice == 'Rock' and myChoice == 'Scissors'):
        print("You lose")
        initial()
    elif(opponentsRandomChoice == 'Rock' and myChoice == 'Rock'):
        print("You draw")
        initial()
    elif(opponentsRandomChoice == 'Paper' and myChoice == 'Scissors'):
        print("You win")
        initial()
    elif(opponentsRandomChoice == 'Paper' and myChoice == 'Rock'):
        print("You lose")
        initial()
    elif(opponentsRandomChoice == 'Paper' and myChoice == 'Paper'):
        print("You draw")
        initial()
    elif(opponentsRandomChoice == 'Scissors' and myChoice == 'Rock'):
        print("You win")
        initial()
    elif(opponentsRandomChoice == 'Scissors' and myChoice == 'Paper'):
        print("You lose")
        initial()
    elif(opponentsRandomChoice == 'Scissorss' and myChoice == 'Scissors'):
        print("You draw")
        initial()
    else:
        print("Didn't enter a valid value, please ensure that you spelled everything correctly")
        rock_paper_scissors()

initial()


    
