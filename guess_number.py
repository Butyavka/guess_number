from tkinter import *
from tkinter import messagebox as mb
import random


class Window:
    def __init__(self, width, height, title="Вход", resizable=(False, False)):
        self.root = Tk()
        self.root.title(title)
        # self.root.geometry(f"{width}x{height}+200+200")
        self.root.resizable = (resizable[0], resizable[1])
        self.ran_num = 0
        self.check = 0
        self.number_entry = Entry(self.root, justify=CENTER)

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        Label(self.root, text="Угадаешь число?", height=2).grid(row=0, column=0, columnspan=2)
        Button(self.root, text="Загадать число", width=15, command=self.random_num).grid(row=2, column=1, columnspan=2)
        self.number_entry.grid(row=4, column=1)

        Button(self.root, text="Отправить", width=10, command=self.compare_numbers).grid(row=5, column=1, columnspan=2)
        Button(self.root, text="Выйти", width= 10, command=self.exit).grid(row=6, column=1, columnspan=2)

    def random_num(self):
        self.ran_num = random.randint(0, 100)
        Label(self.root, text=self.ran_num, height=2).grid(row=9, column=0, columnspan=2)

    def compare_numbers(self):
        number = 0
        try:
            number = int(self.number_entry.get())
        except ValueError:
            self.check += 1
            Label(self.root, text=f'Число попыток: {self.check}', height=2).grid(row=7, column=0, columnspan=2)
            return mb.showerror('Ошибка', "Введенные тобой символы не являются числом")

        if number == self.ran_num:
            self.check += 1
            mb.showinfo('Юуху', f'Ты угодал c {self.check} попытки <3')
            self.check = 0
            Label(self.root, text=f'Число попыток: {self.check}', height=2).grid(row=7, column=0, columnspan=2)
        elif number > self.ran_num:
            mb.showinfo(';(', 'Загаданное число меньше')
            self.check += 1
            Label(self.root, text=f'Число попыток: {self.check}', height=2).grid(row=7, column=0, columnspan=2)
        else:
            mb.showinfo(';(', 'Загаданное число больше')
            self.check += 1
            Label(self.root, text=f'Число попыток: {self.check}', height=2).grid(row=7, column=0, columnspan=2)

    def exit(self):
        choice = mb.askyesno("Выход", "Вы хотите выйти?")
        if choice:
            self.root.destroy()


if __name__ == "__main__":
    window = Window(500, 500)
    window.run()