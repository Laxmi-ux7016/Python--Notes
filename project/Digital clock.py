import tkinter as tk
from time import strftime

root =tk.Tk()
root.title("Digital clock")

def time():
    string =strftime("%H:%M%S %P \n")