import tkinter as tk
from tkinter import ttk

if __name__ == '__main__':

    window = tk.Tk()
    window.title("Projeto colaboração")
    window.geometry("700x500")

    label = tk.Label(master = window, text = "Projeto colaboração")
    label.pack(pady = 10)

    text = tk.Text(master = window)
    text.pack()
    
    #modificação feita após fork
    button = tk.Button(master = window, text = "Butão de mod")
    button.pack(pady =10)

    window.mainloop()
