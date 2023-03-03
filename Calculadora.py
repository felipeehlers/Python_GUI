import tkinter as tk

root = tk.Tk()

info_plus = list()
info_sub = list()
count = int(0)
count_2 = int(0)
operator_T_F = int()
active = int(0)


def clear_program():
    global count
    global info_plus
    global info_sub
    global operator_T_F
    global active
    global count_2
    count = 0
    info_plus.clear()
    info_sub.clear()
    operator_T_F = None
    active = 0
    count_2 = 0


def number(num):
    global active
    global count_2
    num = str(num)
    atual = info.get() + num
    info.delete(0, 'end')
    info.insert(0, atual)
    active = 0
    count_2 = 0


def operation(bol):
    global count
    global count_2
    global info_plus
    global info_sub
    global operator_T_F
    global active

    if count < 1:
        if info.get() == '':
            clear_program()
            return
        else:
            info_plus.append(int(info.get()))
            count += 1
        operator_T_F = bol
        info.delete(0, 'end')
        return
    if active == '0':
        active = 1
        if operator_T_F == 1:
            info_plus.append(int(info.get()))
        elif operator_T_F == 0:
            info_sub.append(int(info.get()))
    elif active == '1' and operator_T_F != bol:
        if operator_T_F == 1:
            turn = info_plus.pop()
            info_sub.append(turn)
        elif operator_T_F == 0:
            turn = info_sub.pop()
            info_sub.append(turn)
    operator_T_F = bol
    info.delete(0, 'end')
    count_2 = 0


def clear():
    global count
    global info_plus
    global info_sub
    global operator_T_F
    global count_2
    info.delete(0, 'end')
    clear_program()
    count_2 = 0


def equals():
    global count
    global info_plus
    global info_sub
    global operator_T_F
    global count_2
    if operator_T_F and info.get() != '' and count_2 == 0:
        info_plus.append(int(info.get()))
    elif info.get() != '' and count_2 == 0:
        info_sub.append(int(info.get()))
    info.delete(0, 'end')
    result = sum(info_plus) - abs(sum(info_sub))
    info.insert(0, result)
    clear_program()
    count_2 = 1


info = tk.Entry(root, width=34, borderwidth=5)
info.grid(row=0, column=0, columnspan=2, sticky='n', pady=5, padx=5)

number_1 = tk.Button(root, text='1', padx=30, pady=25, command=lambda: number(1))
number_2 = tk.Button(root, text='2', padx=30, pady=25, command=lambda: number(2))
number_3 = tk.Button(root, text='3', padx=30, pady=25, command=lambda: number(3))
number_4 = tk.Button(root, text='4', padx=30, pady=25, command=lambda: number(4))
number_5 = tk.Button(root, text='5', padx=30, pady=25, command=lambda: number(5))
number_6 = tk.Button(root, text='6', padx=30, pady=25, command=lambda: number(6))
number_7 = tk.Button(root, text='7', padx=30, pady=25, command=lambda: number(7))
number_8 = tk.Button(root, text='8', padx=30, pady=25, command=lambda: number(8))
number_9 = tk.Button(root, text='9', padx=30, pady=25, command=lambda: number(9))
number_0 = tk.Button(root, text='0', padx=30, pady=25, command=lambda: number(0))
button_clear = tk.Button(root, text='C', padx=48, pady=25, command=clear)
button_plus = tk.Button(root, text='+', padx=29, pady=25, command=lambda: operation(1))
button_minus = tk.Button(root, text='-', padx=30, pady=25, command=lambda: operation(0))
button_equals = tk.Button(root, text='=', padx=48, pady=25, command=equals)

number_1.grid(row=3, column=0, sticky='w')
number_2.grid(row=3, column=0, columnspan=3, sticky='s')
number_3.grid(row=3, column=1, sticky='e')

number_4.grid(row=2, column=0, sticky='w')
number_5.grid(row=2, column=0, columnspan=3, sticky='s')
number_6.grid(row=2, column=1, sticky='e')

number_7.grid(row=1, column=0, sticky='w')
number_8.grid(row=1, column=0, columnspan=3, sticky='s')
number_9.grid(row=1, column=1, sticky='e')

button_minus.grid(row=4, column=0, sticky='w')
number_0.grid(row=4, column=0, columnspan=3, sticky='s')
button_plus.grid(row=4, column=1, sticky='e')

button_clear.grid(row=5, column=0, columnspan=1, sticky='w')
button_equals.grid(row=5, column=1, sticky='e')

root.mainloop()
