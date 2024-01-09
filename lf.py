from tkinter import *

window = Tk()
window.title("Приложение CtaviaNS")
window.geometry('420x500')
window.resizable(False, False)
window.iconbitmap(default="64.ico")
window.config(bg='#a6caf0')



def new_window():
    def convert_number():
        number = entry_number.get()
        from_base = int(entry_from_base.get())
        to_base = int(entry_to_base.get())

        try:
            if not number or not entry_from_base.get() or not entry_to_base.get():
                raise ValueError("Поля не могут \n быть пустыми")

            if from_base < 2 or from_base > 36 or to_base < 2 or to_base > 36:
                raise ValueError("Система счисления \n должна быть от 2 до 36")

            decimal_number = int(number, from_base)
            converted_number = ""

            while decimal_number > 0:
                remainder = decimal_number % to_base
                if remainder < 10:
                    converted_number = str(remainder) + converted_number
                else:
                    converted_number = chr(remainder + 55) + converted_number
                decimal_number = decimal_number // to_base

            label_result.config(text="Результат: " + converted_number)
        except ValueError as e:
            label_result.config(text="Ошибка: проверьте \n правильность \n введения данных")

    def validate_input(input_str):
        valid_chars = set('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        return all(char in valid_chars for char in input_str)

    window1 = Tk()
    window1.title("Приложение CtaviaNS")
    window1.geometry('420x500')
    window1.resizable(False, False)
    window1.iconbitmap(default="64.ico")
    window1.config(bg='#a6caf0')

    k = Label(window1, text="Перевод чисел  \n в различные Системы Счисления")
    k.pack(pady=0)
    k.config(bg="#a6caf0", font=("W3$iP", 16))

    l = Label(window1, text="Введите ваше число и \n его систему счисления:", font=("W3$iP", 13))
    l.place(x=0, y=80)
    l.config(bg="#a6caf0")

    entry_number = Entry(window1, validate="key", width=25, font=("W3$iP", 10))
    entry_number['validatecommand'] = (entry_number.register(validate_input), '%P')
    entry_number.place(x=13, y=140)

    entry_from_base = Entry(window1, validate="key", width=5, font=("W3$iP", 10))
    entry_from_base['validatecommand'] = (entry_from_base.register(validate_input), '%P')
    entry_from_base.place(x=240, y=140)

    l = Label(window1, text="Введите систему счисления,", font=("W3$iP", 13))
    l.place(x=10, y=170)
    l.config(bg="#a6caf0")
    l = Label(window1, text="в которую Вы хотите перевести число:", font=("W3$iP", 13))
    l.place(x=10, y=195)
    l.config(bg="#a6caf0")

    entry_to_base = Entry(window1, validate="key", width=5, font=("W3$iP", 10))
    entry_to_base['validatecommand'] = (entry_to_base.register(validate_input), '%P')
    entry_to_base.place(x=13, y=240)
    l = Label(window1, text="система счисления", font=("W3$iP", 13))
    l.place(x=52, y=238)
    l.config(bg="#a6caf0")

    button_convert = Button(window1, text="Конвертировать", command=convert_number)
    button_convert.place(x=13, y=280)
    button_convert.config(fg="#000000", bg="#a7a6f0", font=("W3$iP", 15), activebackground='#f0a6ef',
                          activeforeground="#000000")

    label_result = Label(window1, text="Результат:", font=("W3$iP", 17))
    label_result.place(x=10, y=350)
    label_result.config(bg="#a6caf0")

    window1.mainloop()




def new_window1():

    def convert_to_decimal(number, base):
        try:
            decimal_number = int(number, base)
            return decimal_number
        except ValueError:
            return None

    def convert_from_decimal(number, base):
        converted_number = ""
        while number > 0:
            remainder = number % base
            converted_number = str(remainder) + converted_number
            number = number // base
        return converted_number

    def calculate():
        number1 = entry_number1.get()
        number2 = entry_number2.get()
        base1 = int(entry_base1.get())
        base2 = int(entry_base2.get())
        result_base = int(entry_result_base.get())

        decimal_number1 = convert_to_decimal(number1, base1)
        decimal_number2 = convert_to_decimal(number2, base2)

        if decimal_number1 is None or decimal_number2 is None:
            label_result.config(text="Неправильный \n ввод чисел")
            return

        operation = variable_operation.get()
        if operation == "+":
            result = decimal_number1 + decimal_number2
        elif operation == "-":
            result = decimal_number1 - decimal_number2
        elif operation == "*":
            result = decimal_number1 * decimal_number2
        elif operation == "/":
            if decimal_number2 == 0:
                label_result.config(text="Деление на ноль  \n запрещено")
                return
            result = decimal_number1 // decimal_number2

        result_number = convert_from_decimal(result, result_base)
        label_result.config(text=result_number)

    window2 = Tk()
    window2.title("Приложение CtaviaNS")
    window2.geometry('420x500')
    window2.resizable(False, False)
    window2.iconbitmap(default="64.ico")
    window2.config(bg='#bed2f7')

    label = Label(window2, text="Арифметические действия \n чисел в некоторых СС", font=("Badonic", 18))
    label.pack(pady=0)
    label.config(bg="#bed2f7")

    label_number1 = Label(window2, text="Число 1:", font=("Badonic", 12))
    label_number1.place(x=11, y=70)
    label_number1.config(bg="#bed2f7")
    entry_number1 = Entry(window2)
    entry_number1.place(x=13, y=100)

    label_base1 = Label(window2, text="СС 1-го числа:", font=("Badonic", 13))
    label_base1.place(x=187, y=70)
    label_base1.config(bg="#bed2f7")
    entry_base1 = Entry(window2, width=5)
    entry_base1.place(x=190, y=100)

    label_operation = Label(window2, text="Операция:", font=("Badonic", 13))
    label_operation.place(x=65, y=160)
    label_operation.config(bg="#bed2f7")
    variable_operation = StringVar(window2)
    variable_operation.set("+")
    option_menu_operation = OptionMenu(window2, variable_operation, "+", "-", "*", "/")
    option_menu_operation.place(x=160, y=160)
    option_menu_operation.config(bg="#bed2f7", activebackground='#9a9bd6', highlightthickness = 0, width=3)
    option_menu_operation['menu'].config(bg='#bed2f7')

    label_number2 = Label(window2, text="Число 2:", font=("Badonic", 13))
    label_number2.place(x=13, y=210)
    label_number2.config(bg="#bed2f7")
    entry_number2 = Entry(window2)
    entry_number2.place(x=13, y=240)

    label_base2 = Label(window2, text="СС 2-го числа:", font=("Badonic", 13))
    label_base2.place(x=187, y=210)
    label_base2.config(bg="#bed2f7")
    entry_base2 = Entry(window2, width=5)
    entry_base2.place(x=190, y=240)

    label_result_base = Label(window2, text="СС результата:", font=("Badonic", 13))
    label_result_base.place(x=100, y=290)
    label_result_base.config(bg="#bed2f7")
    entry_result_base = Entry(window2, width=6)
    entry_result_base.place(x=235, y=290)

    button_calculate = Button(window2, text="Вычислить", command=calculate)
    button_calculate.place(x=140, y=340)
    button_calculate.config(fg="#06061c", bg="#9a9bd6", font=10, activebackground='#06061c', activeforeground="#9a9bd6")

    label_result = Label(window2, text="Результат: ", font=("Badonic", 17))
    label_result.place(x=125, y=380)
    label_result.config(bg='#bed2f7')

    window2.mainloop()

lbl = Label(window, text="CtaviaNS", font=("Clickuper", 35))
lbl.pack(pady=6)
lbl.config(bg="#a6caf0")

a = Label(window, text="Калькулятор Систем Счисления", font=("Clickuper", 13))
a.pack(pady=6)
a.config(bg="#a6caf0")

button1 = Button(window, text="Перевод чисел в различные СС", height=3, width=30, command=new_window)
button1.pack(pady=30)
button1.config(fg="#000000", bg="#a7a6f0", font=("Clickuper", 11), activebackground='#f0a6ef', activeforeground="#000000")

button2 = Button(window, text="Арифметические действия \n чисел в некоторых СС", height=4, width=30, command=new_window1)
button2.pack(pady=15)
button2.config(fg="#000000", bg="#a7a6f0", font=("Clickuper 11"), activebackground='#f0a6ef', activeforeground="#000000")


window.mainloop()
