import random
import tkinter as tk

# Initialize the Tkinter window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.state("zoomed") # Maximizing the window
root.config(bg= "gray70")

# Instructions text
instructions ="""Welcome to the classic Rock-Paper-Scissors game!

Rules:
-Rock beats Scissors.
-Scissors beat Paper.
-Paper beats Rock.
How to Play:

Enter rock, paper, or scissors when prompted.
The computer will pick randomly.
Results and scores are shown after each round.
Try to outsmart the computer and score the most points. Good luck!"""

# Label for instructions
label1 = tk.Label(root, text=instructions, font=("Arial", 12, "bold"), bg="gray80", justify="center",borderwidth= 1, relief= "solid")
label1.pack(pady=20)

# Score variables
user_score = 0
computer_score = 0

# Display the scores
score_label = tk.Label(root, text=f"Your Score: {user_score}\n Computer Score: {computer_score}",
            font=("Arial", 15) , bg="gray60", borderwidth= 2, relief= "solid")
score_label.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="gray70")
result_label.pack(pady=10)

# Function to update the result and scores
def game_rps(user_choice):
    global user_score,computer_score
    
    all_choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(all_choices)
    
    if user_choice == computer_choice:
        result = "It's a tie!"
        
    elif user_choice == "rock" and computer_choice == "scissors" or \
        user_choice == "paper" and computer_choice == "rock" or \
        user_choice == "scissors" and computer_choice == "paper":
            result = "You win!"
            user_score += 1
    else:
        result = "You lose!"
        computer_score += 1

    # Update the result and score labels
    result_label.config(text= f"You choose: {user_choice.capitalize()}\n Computer choose: {computer_choice.capitalize()}\n {result}",
                        justify= "center", borderwidth= 2, relief= "solid")
    score_label.config(text= f"Your Score: {user_score} \n Computer Score: {computer_score}")
    
# Button functions for rock, paper, scissors
def choose_rock():
    game_rps("rock")
    
def choose_paper():
    game_rps("paper")
    
def choose_scissors():
    game_rps("scissors")
    
# Buttons for user choice
rock_button = tk.Button(root, text= "Rock", font= ( "Arial", 14, "bold"), command= choose_rock)
rock_button.place(x=450, y=450)

paper_button = tk.Button(root, text= "Paper", font= ( "Arial", 14, "bold"), command= choose_paper)
paper_button.place(x=600, y=450)

scissors_button = tk.Button(root, text= "Scissors", font= ( "Arial", 14, "bold"), command= choose_scissors)
scissors_button.place(x=750, y=450)

# Play Again Button
def play_game():
    
    global user_score,computer_score
    user_score = 0 
    computer_score = 0
    score_label.config(text= f"Your Score: {user_score}\nComputer Score: {computer_score}")
    result_label.config(text= "")

# Play Again Button
play_again_button = tk.Button(root, text= "Play Again", font= ( "Arial", 15, "bold"), command= play_game, bg= "dim gray")
play_again_button.place(x= 580, y=530)     
        
# Run the Tkinter event loop
tk.mainloop()
