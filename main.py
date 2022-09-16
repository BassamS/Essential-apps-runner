import tkinter as tk
from tkinter import Canvas, filedialog, Text
import os
from turtle import pd

root = tk.Tk()

# Box size and color
canvas = tk.Canvas(root, height=400, width=400, bg="#263D42")
canvas.pack()

# 2nd box size and color
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

# Buttons
open_file = tk.Button(root, text="Open File", padx=10,
                      pady=5, fg="white", bg="#263D42")

# Showing the button
open_file.pack()

run_apps = tk.Button(root, text="Run Apps", padx=10,
                     pady=5, fg="white", bg="#263D42")

# Showing the button
run_apps.pack()

root.mainloop()
