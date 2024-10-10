import tkinter as tk
from tkinter import ttk
root = tk.Tk()

progressbar = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")

progressbar.start()

def stop_progressbar():
    if root.winfo_exists() and progressbar.winfo_exists():
        progressbar.stop()
        progressbar["value"] = 0
        root.quit()
        root.destroy()

if root.winfo_exists() and progressbar.winfo_exists():
    root.after(5000, stop_progressbar)

progressbar.pack()

def exit_app():
    stop_progressbar()

root.protocol("WM_DELETE_WINDOW", exit_app)

root.mainloop()