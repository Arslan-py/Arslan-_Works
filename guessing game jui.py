import tkinter as tk
import random
from tkinter import messagebox

def check_answers():
    list1=[1,2,3,4,5,6,7,8,9,10]
    a=random.choice(list1)
    list2=['a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,u,r,s,t,w,x,y,z,']
    b=random.choice(list2)
    list3=['saad,ali,arslan']
    c=random.choice(list3)
    score = 0
    
    if answer1.get().lower() == a:
        score += 1
    if answer2.get().lower() == b:
        score += 1
    if answer3.get().lower() == c:
        score += 1
    
    total_questions = 3
    percentage = (score / total_questions) * 100
    
    messagebox.showinfo("Result", f"You attempted {score} questions correctly!\nMarks obtained: {percentage:.2f}%")
    window.destroy()

def start_game():
    if messagebox.askyesno("Ready to Play?", "Are you ready to play the guessing game?"):
        label1.config(text="Question 1: Guess a number from 1 to 10:")
        label2.config(text="Question 2: Guess a letter from A to Z:")
        label3.config(text="Question 3: Guess one name from: 1. Ali, 2. Saad, 3. Arslan:")
        button_start.config(state=tk.DISABLED)
        button_submit.config(state=tk.NORMAL)

# Create the main window
window = tk.Tk()
window.title("Guessing Game")

# Create widgets
label_intro = tk.Label(window, text="Welcome to the Guessing Game!", font=("Helvetica", 14))
label1 = tk.Label(window, text="")
label2 = tk.Label(window, text="")
label3 = tk.Label(window, text="")
answer1 = tk.Entry(window)
answer2 = tk.Entry(window)
answer3 = tk.Entry(window)
button_start = tk.Button(window, text="Start Game", command=start_game)
button_submit = tk.Button(window, text="Submit Answers", command=check_answers, state=tk.DISABLED)

# Place widgets using grid layout
label_intro.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
label1.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
answer1.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)
label2.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
answer2.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)
label3.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
answer3.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)
button_start.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
button_submit.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Start the main loop
window.mainloop()
