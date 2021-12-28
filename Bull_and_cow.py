from tkinter import *
from tkinter import messagebox
import random
import keyboard



z=10
game_time = 1
def show_message():
    result = game()
    global z
    z += 1
    global game_time
    game_time +=1
    messagebox.showinfo("Результат", result)
    Label(text=result).grid(row=z*5, column=5, sticky="w")
    Label(text=message.get()).grid(row=z*5, column=7, sticky="w")



root = Tk()

root.title('Bull and Cows')
root.geometry("550x350")


message = StringVar()
number_label = Label(text="Введите 4 разных числа:")
number_label.grid(row=5, column=5, sticky="w")

message_entry = Entry(textvariable=message)
message_entry.place(relx=.5, rely=.1, anchor="w")
message_entry.bind('<Return>', show_message)

message_button = Button(text="Проверить", command=show_message)
message_button.place(relx=.6, rely=.2, anchor="w")

num_digits = 4
ran_number = random.sample(range(0,10), num_digits)
print(ran_number)



def game():
    number = [int(i) for i in str(message.get())]
    if number.count(0) > 1 or number.count(1) > 1 or number.count(2) > 1 or number.count(3) > 1 or number.count(4) > 1 or number.count(5) > 1 or number.count(6) > 1 or number.count(7) > 1 or number.count(8) > 1 or number.count(9) > 1:
        return "Вы ввели неверное число. Повторите ввод"
    elif number == ran_number:
        return f"Вы выйграли. Количество затраченных ходов: {game_time}"
    else:
        cow = 0
        bull = 0
        for x in range(0,num_digits):
            if number[x] == ran_number[x]:
                bull += 1
            elif number[x] in ran_number:
                cow+=1
        return f"Коров: {cow}; Быков: {bull}"


root.mainloop()