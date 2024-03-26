from tkinter import *


window = Tk()
window.title("Приложение CtaviaNS")
window.geometry('420x500')
window.resizable(False, False)
window.iconbitmap(default="64.ico")
window.config(bg='#a6caf0')


def go_back(main_window, current_window):
    current_window.destroy()
    main_window.deiconify()

def new_window():
    window.withdraw()

    def to_dec(num, cur):
        num = num.upper()
        shift = 10 - ord("A")
        ans = 0
        sAns = ""
        j = 0
        for i in num[::-1]:
            ans += int(f"{i if i.isdigit() else (ord(i) + shift)}") * (cur ** j)
            sAns += f"{i if i.isdigit() else (ord(i) + shift)}*{cur}^{j} + "
            j = j + 1

        sAns = sAns[:-2]
        return (sAns, ans)

    def from_dec(num, to):
        tmp = num
        shift = 10 - ord("A")
        sR = ""
        sAns = ""
        while tmp != 0:
            div = tmp // to
            mod = tmp % to
            sR += f"{tmp}/{to}: div = {div}, mod = {mod} ({chr(mod - shift)})" + "\n"
            tmp = div
            sAns = str(mod if mod < 10 else chr(mod - shift)) + sAns

        return (sR, sAns)

    def convert_number():
        number = entry_number.get()
        from_base = int(entry_from_base.get())
        to_base = int(entry_to_base.get())

        rToDec = to_dec(number, from_base)[0]
        ansToDec = to_dec(number, from_base)[1]
        rFromDec = from_dec(ansToDec, to_base)[0]
        ansFromDec = from_dec(ansToDec, to_base)[1]

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
            return (rToDec, ansToDec, rFromDec, ansFromDec)
        except ValueError as e:
            label_result.config(text="Ошибка: проверьте \n правильность \n введения данных")

    def validate_input(input_str):
        valid_chars = set('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        return all(char in valid_chars for char in input_str)

    def open_second_window1():

        second_window1 = Toplevel(window1)

        second_window1.title("Приложение CtaviaNS")
        second_window1.geometry('420x500')
        second_window1.resizable(False, False)
        second_window1.iconbitmap(default="64.ico")
        second_window1.config(bg='#a6caf0')
        tmp = convert_number()
        second_label = Label(second_window1, text="Решение: ", font=("W3$iP", 16), bg="#a6caf0")
        second_label.pack()

        second_label = Label(second_window1, text=tmp[0] + "= " + str(tmp[1]) + "\n" + tmp[2] + tmp[3],
                                 font=("Verdana", 13), bg="#a6caf0")
        second_label.pack()

    window1 = Tk()
    window1.title("Приложение CtaviaNS")
    window1.geometry('420x500')
    window1.resizable(False, False)
    window1.iconbitmap(default="64.ico")
    window1.config(bg='#a6caf0')

    k = Label(window1, text="Перевод чисел  \n в различные Системы Счисления")
    k.pack(pady=1)
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

    button_convert = Button(window1, text="Конвертировать", command=lambda: (convert_number(), open_second_window1()))
    button_convert.place(x=13, y=280)
    button_convert.config(fg="#000000", bg="#a7a6f0", font=("W3$iP", 15), activebackground='#f0a6ef',
                          activeforeground="#000000")

    label_result = Label(window1, text="Результат:", font=("W3$iP", 17))
    label_result.place(x=10, y=350)
    label_result.config(bg="#a6caf0")

    button_back = Button(window1, text="Назад", command=lambda: go_back(window, window1))
    button_back.place(x=10, y=7)
    button_back.config(fg="#000000", bg="#a7a6f0", font=("W3$iP", 10), activebackground='#f0a6ef',
                       activeforeground="#000000")

    window1.mainloop()


def new_window1():
    window.withdraw()

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
    window2.geometry(window.geometry())
    window2.resizable(False, False)
    window2.iconbitmap(default="64.ico")
    window2.config(bg='#a6caf0')

    label = Label(window2, text="Арифметические \n действия чисел в некоторых СС", font=("W3$iP", 16))
    label.pack(pady=15)
    label.config(bg="#a6caf0")

    label_number1 = Label(window2, text="Число 1:", font=("W3$iP", 14))
    label_number1.place(x=11, y=80)
    label_number1.config(bg="#a6caf0")
    entry_number1 = Entry(window2, font=("W3$iP", 10))
    entry_number1.place(x=13, y=120)

    label_base1 = Label(window2, text="СС 1-го числа:", font=("W3$iP", 14))
    label_base1.place(x=189, y=80)
    label_base1.config(bg="#a6caf0")
    entry_base1 = Entry(window2, width=5, font=("W3$iP", 10))
    entry_base1.place(x=190, y=120)

    label_operation = Label(window2, text="Операция:", font=("W3$iP", 14))
    label_operation.place(x=85, y=160)
    label_operation.config(bg="#a6caf0")
    variable_operation = StringVar(window2)
    variable_operation.set("+")
    option_menu_operation = OptionMenu(window2, variable_operation, "+", "-", "*", "/")
    option_menu_operation.place(x=200, y=160)
    option_menu_operation.config(bg="#a7a6f0", activebackground='#f0a6ef', highlightthickness = 0, width=3, font=("Verdana", 14))
    option_menu_operation['menu'].config(bg='#d0d0f7',activebackground='#f0a3f0', activeforeground='#000000', font=("Verdana", 14))

    label_number2 = Label(window2, text="Число 2:", font=("W3$iP", 14))
    label_number2.place(x=13, y=220)
    label_number2.config(bg="#a6caf0")
    entry_number2 = Entry(window2, font=("W3$iP", 10))
    entry_number2.place(x=13, y=260)

    label_base2 = Label(window2, text="СС 2-го числа:", font=("W3$iP", 14))
    label_base2.place(x=189, y=220)
    label_base2.config(bg="#a6caf0")
    entry_base2 = Entry(window2, width=5, font=("W3$iP", 10))
    entry_base2.place(x=190, y=260)

    label_result_base = Label(window2, text="СС результата:", font=("W3$iP", 14))
    label_result_base.place(x=75, y=290)
    label_result_base.config(bg="#a6caf0")
    entry_result_base = Entry(window2, width=6, font=("W3$iP", 10))
    entry_result_base.place(x=250, y=295)

    button_calculate = Button(window2, text="Вычислить", command=calculate)
    button_calculate.place(x=140, y=340)
    button_calculate.config(fg="#000000", bg="#a7a6f0", font=("W3$iP", 15), activebackground='#f0a6ef',
                          activeforeground="#000000")

    label_result = Label(window2, text="Результат: ", font=("W3$iP", 17))
    label_result.place(x=125, y=390)
    label_result.config(bg='#a6caf0')

    button_back = Button(window2, text="Назад", command=lambda: go_back(window, window2))
    button_back.place(x=10,y=10)
    button_back.config(fg="#000000", bg="#a7a6f0", font=("W3$iP", 10), activebackground='#f0a6ef',
                       activeforeground="#000000")

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