import tkinter as tk

def press(key):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + key)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

window = tk.Tk()
