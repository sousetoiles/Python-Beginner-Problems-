print("Made by Jade Palmer")
print("Version 3.0")
import time
lose = ("The computer wins")
win = ("You win")
lives = 5
score = 0
drew = 0
computer_lives = 7
password_list = []
while True:
    print("To begin, fill in the below information.")
    username = input("please enter your username:  ")
    password = input("please enter your password:  ")
    searchfile = open("accounts.txt","r")
    for line in searchfile:
        password_list.append(line.strip())
        if username and password in password_list:
            print("access granted")
            time.sleep(0.5)
            print("Loading...")
            time.sleep(0.5)
            print("Loading...")
            time.sleep(0.5)
            print("Loading...")
            time.sleep(0.5)
            print("access granted")
            print("Live Rules")
            print("You start with",lives,"lives")
            print("If you win, you get an extra life")
            print("If you lose, you lose a life")
            print("If you draw, the lives stay the same")
            print("------------------------------------")
            
            print("------------------------------------")
            print("To see a list of rules, type rules")
            print("------------------------------------")
            print("At any point, type exit to leave the game")
            print("------------------------------------")
            print("The computer has lives as well")
            print("Can you beat the computer?")
            print("Good luck!")
            print("------------------------------------")
            while True:
                rps = input("Rock, Paper, Scissors?  ")
                rps = rps.title()
                import random
                computer = ("rock", "paper", "scissors")
                computer = random.choice(computer)
                #rock if statements
                if rps == "Rock" and computer == "paper":
                    print("The computer chose",computer)
                    print("")
                    print(lose)
                    print("")
                    print("")
                    lives-=1
                if rps == "Rock" and computer == "scissors":
                    print("The computer chose",computer)
                    print("")
                    print(win)
                    computer_lives-=1
                    print("")
                    print("")
                    score+=1
                #paper if statements
                if rps == "Paper" and computer == "scissors":
                    print("The computer chose",computer)
                    print("")
                    print(lose)
                    print("")
                    print("")
                    lives-=1
                if rps == "Paper" and computer == "rock":
                    print("The computer chose",computer)
                    print("")
                    print(win)
                    computer_lives-=1
                    print("")
                    print("")
                    score+=1
                #scissors if statements
                if rps == "Scissors" and computer == "paper":
                    print("The computer chose",computer)
                    print("")
                    print(win)
                    computer_lives-=1
                    print("")
                    print("")
                    score+=1
                if rps == "Scissors" and computer == "rock":
                    print("The computer chose",computer)
                    print("")
                    print(lose)
                    print("")
                    print("")
                    lives-=1
                #duplicates
                if rps == "Rock" and computer == "rock":
                    print("The computer chose",computer)
                    print("")
                    print("You drew")
                    print("")
                    print("")
                    drew+=1
                if rps == "Paper" and computer == "paper":
                    print("The computer chose",computer)
                    print("")
                    print("You drew")
                    print("")
                    print("")
                    drew+=1
                if rps == "Scissors" and computer == "scissors":
                    print("The computer chose",computer)
                    print("")
                    print("You drew")
                    print("")
                    print("")
                    drew+=1
                #system
                if rps == "rules":
                    print("******************************")
                    print("Rules")
                    print("******************************")
                    print("Rock beats scissors")
                    print("Rock loses against paper")
                    print("Scissors beats paper")
                    print("Scissors loses to rock")
                    print("Paper beats rock")
                    print("Paper loses to scissors")
                    print("******************************")
                if rps == "display lives":
                    print(lives)
                if rps == "display score":
                    print(score)
                if rps == "display drew":
                    print(drew)
                #lives
                if lives == 0 or rps == "test":
                    print("Thanks for playing")
                    print("You have ran out of lives")
                    print("You got",score,"correct")
                    print("You drew",drew,"times")
                    stop = input("press enter to exit")
                    exit()
                if computer_lives == 0:
                    print("Thanks for playing")
                    print("The computer lost all its lives. You win")
                    print("You got",score,"correct")
                    print("You drew",drew,"times")
                    stop = input("press enter to exit")
                    exit()
                #exit
                if rps == "exit":
                    break
        else:
            print("Your username or password is incorrect")
            print("--------------------------------------")
            
