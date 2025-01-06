import tkinter as tk
import random

root = tk.Tk()
root.title("Love Question")
root.geometry("800x600")  
root.configure(bg="#ffcccc")  

def show_love_message():
    label_question.config(text="I love you too! ", bg="#ffe6e6", fg="#660033") 
    yes_button.pack_forget()  
    no_button.pack_forget()   


def move_button(event):
    new_x = random.randint(0, 700)  
    new_y = random.randint(0, 500)  
    no_button.place(x=new_x, y=new_y) 


label_question = tk.Label(root, text="I love you ", font=("Arial", 48), bg="#ffe6e6", fg="#660033")
label_question.pack(pady=50)


yes_button = tk.Button(root, text="Yes", font=("Arial", 24), command=show_love_message, bg="#ff4d4d", fg="white")
yes_button.pack()


no_button = tk.Button(root, text="No", font=("Arial", 24), bg="#1e90ff", fg="white")
no_button.pack()


no_button.bind("<Enter>", move_button)


root.mainloop()
