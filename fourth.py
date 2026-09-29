import tkinter as tk
from tkinter import filedialog
def open_letter():
    filename = filedialog.askopenfilename()
    if filename:
        file = open(filename, "r")
        letter = file.read()
        file.close()
        text.delete("1.0", tk.END)
        text.insert("1.0", letter)
def save_letter():
    filename = filedialog.asksaveasfilename()
    if filename:
        letter = text.get("1.0", tk.END)
        file = open(filename, "w")
        file.write(letter)
        file.close()
window = tk.Tk()
window.title("Letter Writer")
text = tk.Text(window, width=70, height=25)
text.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
open_button = tk.Button(window,text="Open Old Letter",command=open_letter)
open_button.grid(row=1, column=0, padx=10, pady=10)
save_button = tk.Button(window,text="Save Letter As",command=save_letter)
save_button.grid(row=1, column=1, padx=10, pady=10)
window.mainloop()