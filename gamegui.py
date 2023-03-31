import tkinter as tk
import hangman

def on_guess_click():
    user_input = input_entry.get()
    result = hangman.play_game(user_input)
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, result)

root = tk.Tk()

input_entry = tk.Entry(root)
input_entry.pack()

guess_button = tk.Button(root, text="Guess", command=on_guess_click)
guess_button.pack()

output_text = tk.Text(root)
output_text.pack()

root.mainloop()