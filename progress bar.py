import tkinter as tk
from tkinter import ttk

# Основное окно
root = tk.Tk()
root.geometry("260x75")
# Оставляю пустым ибо не хочу название
root.title("")

frame = tk.Frame(root)
frame.pack(expand=True)

# Метка для анимации текста (значок загрузки)
loading_label = tk.Label(frame, text="Загрузка", font=("Helvetica", 12))
loading_label.pack(pady=5)  # Расстояние между элементами

# Прогресс-бар
progressbar = ttk.Progressbar(frame, orient="horizontal", length=250, mode="determinate")
progressbar.pack(pady=1)  # Расстояние

# Иконка
icon_label = tk.Label(frame, text="$", font=("Helvetica", 20))
icon_label.pack(pady=1)  # Расстояние

# Старт прогресс-бара
progressbar.start(10)

# Переменные
dots = ["%", "#", "$", "/", "*", "&"] # <- где-то проебался
rotation = ["%", "#", "$", "/", "*", "&"]

# Аним текста
def animate_text():
    global dots
    dots = dots + "." if len(dots) < 3 else ""
    loading_label.config(text=f"Загрузка{dots}")
    root.after(500, animate_text)

# Функция аним
def animate_icon():
    current_icon = rotation.pop(0)
    rotation.append(current_icon)
    icon_label.config(text=current_icon)
    root.after(80, animate_icon)

# Функция для остановки бара
def stop_progressbar():
    if root.winfo_exists() and progressbar.winfo_exists():
        progressbar.stop()
        progressbar["value"] = 0
        root.quit()
        root.destroy()

# Автозакрытие
if root.winfo_exists() and progressbar.winfo_exists():
    root.after(500000, stop_progressbar)

# Запуск анимаций
animate_text()
animate_icon()

# Избавляемся от багов
def exit_app():
    stop_progressbar()

# Что бы прогресс бар не втыкал хули
root.protocol("WM_DELETE_WINDOW", exit_app)

#  Ну это база емае
root.mainloop()
