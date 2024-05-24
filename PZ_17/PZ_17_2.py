from tkinter import *
from tkinter import messagebox

def check_triangle():
    try:
        a = int(entry_a.get())
        b = int(entry_b.get())
        c = int(entry_c.get())

        if a < 0 or b < 0 or c < 0:
            messagebox.showerror("Ошибка", "Введите положительные числа")
            return

        if a == b and b == c:
            messagebox.showinfo("Результат", "Треугольник со сторонами a, b, c является равносторонним")
        else:
            messagebox.showinfo("Результат", "Треугольник со сторонами a, b, c не является равносторонним")
    except ValueError:
        messagebox.showerror("Ошибка", "Введены некорректные данные")


root = Tk()
root.title("Проверка треугольника")
root.geometry("300x200")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = 300
window_height = 180

position_top = int(screen_height/2 - window_height/2)
position_right = int(screen_width/2 - window_width/2)

root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

# Task
frame = Frame(root)
frame.pack(anchor='center')

label_a = Label(frame, text="a:", font='arial 14')
label_a.grid(row=0, column=0, padx=5, pady=5)
entry_a = Entry(frame)
entry_a.grid(row=0, column=1, padx=5, pady=5)

label_b = Label(frame, text="b:", font='arial 14')
label_b.grid(row=1, column=0, padx=5, pady=5)
entry_b = Entry(frame)
entry_b.grid(row=1, column=1, padx=5, pady=5)

label_c = Label(frame, text="c:", font='arial 14')
label_c.grid(row=2, column=0, padx=5, pady=5)
entry_c = Entry(frame)
entry_c.grid(row=2, column=1, padx=5, pady=5)

check_button = Button(frame, text="Проверить", command=check_triangle)
check_button.grid(row=3, columnspan=2, padx=5, pady=5)

root.mainloop()