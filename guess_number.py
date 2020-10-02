from tkinter import *
from tkinter import messagebox as mb
import random


class Window:
    def __init__(self, width, height, title="Вход", resizable=(False, False)):
        self.root = Tk()
        self.root.title(title)
        # self.root.geometry(f"{width}x{height}+200+200")
        self.root.resizable = (resizable[0], resizable[1])
        self.r_num = random.randint(0, 100)
        self.number_entry = Entry(self.root, justify=CENTER)

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        Label(self.root, text="Угадаешь число?", height=2).grid(row=0, column=0, columnspan=2)
        Button(self.root, text="Загадать число", width=10, command=self.random_num).grid(row=2, column=1, columnspan=2)
        self.number_entry.grid(row=4, column=1)
        Button(self.root, text="Отправить", width=10, command=self.compare_numbers).grid(row=5, column=1, sticky=E)
        Button(self.root, text="Выйти", width= 10, command=self.exit).grid(row=6, column=1, sticky=E)

    def random_num(self):
        self.r_num = random.randint(0, 100)

    def compare_numbers(self):
        number = int(self.number_entry.get())
        if number == self.root.r_num:
            mb.showinfo('Юуху', 'Ты угодал<3')
        elif number > self.root.r_num:
            mb.showinfo(';(', 'Загаданное число меньше')
        else:
            mb.showinfo(';(', 'Загаданное число больше')



    def exit(self):
        choice = mb.askyesno("Выход", "Вы хотите выйти?")
        if choice:
            self.root.destroy()


if __name__ == "__main__":
    window = Window(500, 500)
    window.run()