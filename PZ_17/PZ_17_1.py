from tkinter import *
from tkinter import ttk


def ok_clicked():
    print("ОК")

def cancel_clicked():
    print("Отменить")


root = Tk()
root.title('Регистрация электронной таблицы')
root.iconbitmap(default="favicon.ico")
root.geometry('500x600')
root.configure(bg='#f29baf')

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = 720
window_height = 690

position_top = int(screen_height/2 - window_height/2)
position_right = int(screen_width/2 - window_width/2)

root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

# FRAME TEXT
frame_text = Frame(root, bg='#f29baf', relief=SUNKEN)
frame_text.place(x=0, y=0, anchor='nw', width=700, height=100)

reg_text = Label(frame_text, text="Регистрационная страница электронной таблицы", font='arial 14', background='#f29baf')
reg_text.pack(anchor='nw', padx=10, pady=(10, 0))
questionnaire = Label(frame_text, text="Заполнив анкету, вы сможете пользоваться нашей электронной библиотекой", font='arial 12', fg='#262626', background='#f29baf')
questionnaire.pack(anchor='nw', padx=10, pady=(15, 0))

# FRAME FORM
frame_form = Frame(root, bg='#f29baf', relief=SUNKEN)
frame_form.place(x=10, y=100, width=700, height=300)  # Центрирование фрейма

# Field registration
reg_label = Label(frame_form, text="Введите регистрационное имя", fg='#262626', font='arial 12', background='#f29baf')
reg_label.grid(row=0, column=0,  pady=(0, 3), sticky='w')
reg_entry = Entry(frame_form, width=30)
reg_entry.grid(row=0, column=1,  pady=(0, 3))

# Field password
password_label = Label(frame_form, text="Введите пароль", font='arial 12', fg='#262626', background='#f29baf')
password_label.grid(row=1, column=0, pady=(0, 3), sticky='w')
password_entry = Entry(frame_form, show='*', width=30)
password_entry.grid(row=1, column=1, pady=(0, 3))

# Field confirm password
confirm_password_label = Label(frame_form, text="Подтвердите пароль", font='arial 12', fg='#262626', background='#f29baf')
confirm_password_label.grid(row=2, column=0,  pady=(0, 3), sticky='w')
confirm_password_entry = Entry(frame_form, show='*', width=30)
confirm_password_entry.grid(row=2, column=1, pady=(0, 3))

# Field check age
frame_radio = Frame(root, bg='#f29baf', relief=SUNKEN)
frame_radio.place(x=10, y=210, width=700, height=100)

age_label = Label(frame_radio, text="Ваш возраст", font='arial 12', fg='#262626', background='#f29baf')
age_label.grid(row=0, column=0, pady=(0, 3))

age_var = StringVar()

age_radio1 = Radiobutton(frame_radio, text='До 20', variable=age_var, value='До 20', font='arial 11', bg='#f29baf')
age_radio1.grid(row=0, column=1, padx=5, pady=(0, 3))
age_radio2 = Radiobutton(frame_radio, text='20-30', variable=age_var, value='20-30', font='arial 11', bg='#f29baf')
age_radio2.grid(row=0, column=2, padx=5, pady=(0, 3))
age_radio3 = Radiobutton(frame_radio, text='30-50', variable=age_var, value='30-50', font='arial 11', bg='#f29baf')
age_radio3.grid(row=0, column=3, padx=5, pady=(0, 3))
age_radio4 = Radiobutton(frame_radio, text='Старше 50', variable=age_var, value='старше 50', font='arial 11', bg='#f29baf')
age_radio4.grid(row=0, column=4, padx=5, pady=(0, 3))

# Field check language
frame_language = Frame(root, bg='#f29baf', relief=SUNKEN)
frame_language.place(x=10, y=250, width=700, height=100)

language_label = Label(frame_language, text="На каких языках вы читаете", font='arial 12', fg='#262626', background='#f29baf')
language_label.grid(row=0, column=0, pady=(0, 3))

language_var1 = StringVar()
language_var2 = StringVar()
language_var3 = StringVar()
language_var4 = StringVar()

language_check1 = Checkbutton(frame_language, text='Русский', variable=language_var1, onvalue='русский', offvalue='', font='arial 11', bg='#f29baf')
language_check1.grid(row=0, column=1, padx=5, pady=(0, 3))
language_check2 = Checkbutton(frame_language, text='Английский', variable=language_var2, onvalue='английский', offvalue='', font='arial 11', bg='#f29baf')
language_check2.grid(row=0, column=2, padx=5, pady=(0, 3))
language_check3 = Checkbutton(frame_language, text='Французский', variable=language_var3, onvalue='французский', offvalue='', font='arial 11', bg='#f29baf')
language_check3.grid(row=0, column=3, padx=5, pady=(0, 3))
language_check4 = Checkbutton(frame_language, text='Немецкий', variable=language_var4, onvalue='немецкий', offvalue='', font='arial 11', bg='#f29baf')
language_check4.grid(row=0, column=4, padx=5, pady=(0, 3))

# Field select format data
frame_select = Frame(root, bg='#f29baf', relief=SUNKEN)
frame_select.place(x=10, y=290, width=700, height=100)

format_label = Label(frame_select, text="Какой формат данных является для вас предпочтительным", font='arial 12', fg='#262626', background='#f29baf')
format_label.grid(row=0, column=0, pady=(0, 3), sticky='w')

formats = ['HTML', 'Plain text']

format_select = ttk.Combobox(frame_select, values=formats, font='arial 11', state='readonly')
format_select.place(x=2, y=35)
format_select.current(0)

# Field textarea
frame_text_buttons = Frame(root, bg='#f29baf', relief=SUNKEN)
frame_text_buttons.place(x=10, y=350, width=700, height=250)

authors_label = Label(frame_text_buttons, text="Ваши любимые авторы", font='arial 12', fg='#262626', background='#f29baf')
authors_label.grid(row=0, column=0, pady=(10, 5), sticky='w')

authors_text = Text(frame_text_buttons, font='arial 11', width=35, height=3.5)
authors_text.grid(row=1, column=0, padx=3, pady=5)

frame_buttons = Frame(frame_text_buttons, bg='#f29baf')
frame_buttons.grid(row=2, column=0, pady=(5, 0), sticky='w')

ok_button = Button(frame_buttons, text="OK", font='arial 11', command=ok_clicked, bd=0)
ok_button.grid(row=0, column=0, padx=3)

cancel_button = Button(frame_buttons, text="Отменить", font='arial 11', command=cancel_clicked, bd=0)
cancel_button.grid(row=0, column=1, padx=10)

# Check Lab
check_lab = Label(root, text="Проверка PHP Лабораторные по базам данных", fg='#262626', font='arial 12', background='#f29baf')
check_lab.place(x=10, y=515)

# Button Lab
btn_lab = Button(root, text='Лабораторные по базам данных', width=50, height=1, font='arial 12')
btn_lab.place(x=125, y=555)

# Additional text
frame_additional_text = Frame(root, bg='#f29baf', relief=SUNKEN)
frame_additional_text.place(x=200, y=600, width=700)

text1 = Label(frame_additional_text, text="Сегодня замечательный день.", fg='#262626', font='arial 12', background='#f29baf')
text1.grid(row=0, column=0)
text1 = Label(frame_additional_text, text="Я сделал свою первую интернет страничку.", fg='#262626', font='arial 12', background='#f29baf')
text1.grid(row=1, column=0)
text1 = Label(frame_additional_text, text="Я буду богатым и свободным человеком!", fg='#3827f5', font='arial 12', background='#f29baf')
text1.grid(row=2, column=0)

root.mainloop()