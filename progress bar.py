import tkinter as tk
from tkinter import ttk

# Основное окно
root = tk.Tk()
root.geometry("300x120")
root.title("Загрузка")


is_dark_theme = True 


style = ttk.Style()
style.configure("dark.Horizontal.TProgressbar", troughcolor="#4E4E4E", background="#1E90FF")
style.configure("light.Horizontal.TProgressbar", troughcolor="#e0e0e0", background="#0078D7")


def configure_theme():
    if is_dark_theme:
        # Темная тема
        background_color = "#2E2E2E"
        foreground_color = "white"
        theme_button.config(text="🌙")
        progressbar.config(style="dark.Horizontal.TProgressbar")
    else:
        # Светлая тема
        background_color = "white"
        foreground_color = "black"
        theme_button.config(text="☀️")
        progressbar.config(style="light.Horizontal.TProgressbar")

    
    root.config(bg=background_color)
    loading_label.config(bg=background_color, fg=foreground_color)
    percent_label.config(bg=background_color, fg=foreground_color)
    frame.config(bg=background_color)
    theme_button.config(bg=background_color, fg="gray", activebackground="#e0e0e0" if not is_dark_theme else "#4E4E4E")


def toggle_theme():
    global is_dark_theme
    is_dark_theme = not is_dark_theme
    configure_theme()

# Фрейм
frame = tk.Frame(root, bg="white")
frame.pack(expand=True, fill=tk.BOTH)

# Метка для анимации текста
loading_label = tk.Label(frame, text="Загрузка", font=("Helvetica", 12), bg="white", fg="black")
loading_label.pack(pady=5)

# Метка для отображения процентов
percent_label = tk.Label(frame, text="0%", font=("Helvetica", 10), bg="white", fg="black")
percent_label.pack(pady=5)

# Прогресс-бар
progressbar = ttk.Progressbar(frame, orient="horizontal", length=250, mode="determinate", style="dark.Horizontal.TProgressbar")
progressbar.pack(pady=1)
progressbar.start(10)


dots = ["", ".", "..", "..."]
dot_index = 0


def animate_text():
    global dot_index
    loading_label.config(text=f"Загрузка{dots[dot_index]}")
    dot_index = (dot_index + 1) % len(dots)
    root.after(500, animate_text)


def update_progress():
    progress = progressbar["value"]
    if progress < 100:
        progress += 1  # Увеличиваем прогресс на 1%
        progressbar["value"] = progress
        percent_label.config(text=f"{progress}%")
        root.after(200, update_progress)  # Обновляем


def stop_progressbar():
    if root.winfo_exists() and progressbar.winfo_exists():
        progressbar.stop()
        root.quit()

# Кнопка для смены темы
theme_button = tk.Button(frame, command=toggle_theme, font=("Helvetica", 10), width=4)
theme_button.place(relx=1.0, rely=0.0, anchor='ne')  # правый верхний угл

# Автозакрытие 
root.after(10000, stop_progressbar)

# Запуск анимации 
animate_text()

# Запуск обновления
update_progress()


root.protocol("WM_DELETE_WINDOW", stop_progressbar)


configure_theme()  
root.mainloop()
