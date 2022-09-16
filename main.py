from genericpath import isfile
import tkinter as tk
from tkinter import Canvas, filedialog, Text
import os

root = tk.Tk()
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        temp_apps = f.read()
        temp_apps = temp_apps.split(',')
        apps = [x for x in temp_apps if x.strip()]


def add_app():

    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                          filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    print(filename)

    for app in apps:
        label = tk.Label(frame, text=app, bg="grey")
        label.pack()


def run_apps():
    for app in apps:
        os.startfile(app)


# Box size and color
canvas = tk.Canvas(root, height=400, width=400, bg="#263D42")
canvas.pack()

# 2nd box size and color
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

# Buttons
open_file = tk.Button(root, text="Open File", padx=10,
                      pady=5, fg="white", bg="#263D42", command=add_app)

# Showing the button
open_file.pack()

run_apps = tk.Button(root, text="Run Apps", padx=10,
                     pady=5, fg="white", bg="#263D42", command=run_apps)

# Showing the button
run_apps.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

# Saving the selected apps
with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')
