import tkinter as tk 
from tkinter import messagebox
import sys

def check_winner():
    global winner
    
    for combo in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            winner = True
            
            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="green")
            buttons[combo[2]].config(bg="green")
            
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text'].upper()} wins!")
            root.destroy()
            return

    if all(button["text"] != "" for button in buttons) and not winner:
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "It's a Tie!")
        root.destroy()
        return

def button_click(index):
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player.upper()
        check_winner()
        
        if not winner:
            toggle_player()
        
def toggle_player():
    global current_player
    current_player = "o" if current_player == "x" else "x"
    label.config(text=f"Player {current_player.upper()}'s turn")

root = tk.Tk()
root.title("Tic-Tac-Toe") 

buttons = [tk.Button(root, text="", font=("Helvetica", 25, "bold"), width=6, height=2, 
                     command=lambda i=i: button_click(i)) 
           for i in range(9)]

for i, button in enumerate(buttons):
    button.grid(row=i // 3, column=i % 3)

current_player = "x" 
winner = False 

label = tk.Label(root, text=f"Player {current_player.upper()}'s turn", font=("Helvetica", 16))
label.grid(row=3, column=0, columnspan=3, pady=10)

root.mainloop()  

