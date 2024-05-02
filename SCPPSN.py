import random

print("Welcome to Scissors, Paper, Stone game.")
print("To continue, enter 'Yes', to quit enter 'No': ")

answer = input()
answers = answer.title()
if answers == "No":
    print("Goodbye!")
elif answers == 'Yes':
    win = 0
    lose = 0 
    draw = 0 
    while True:
        options = ['scissors','paper','stone']
        computer = random.choice(options)
        player = input("Enter scissors/paper/stone OR 'q' to quit: ")
        
        if player == 'q':
            print("Goodbye!")
            break
        if player not in options:
            print("Please enter a valid option")
            continue
        
        print("Computer: ",computer)
        
        if computer == player:
            draw +=1
            print("DRAW")
        else:
            if (computer == "scissors" and player == 'stone') or (computer == 'paper' and player == 'scissors')or (computer == 'stone' and player == 'paper'):
                win+=1
                print("WIN")
            else:
                lose +=1
                print("LOSE")
        print(f"{win}: {lose}: {draw}")
        print("-" *30)
else:
    print("Invalid option, please try again!")
        
        
            
        
        
            