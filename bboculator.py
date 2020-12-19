import tkinter as t

window = None #None은 이름만 잡아두는 거
display_label = None
expression = ''

def setup_GUI():
    global window
    global display_label

    window = t.Tk()
    window.title('bboculator')
    window.resizable(False, False) #가로세로길이 고정

    display_label = t.Label(window, text='', anchor='e', relief=t.GROOVE, width=15, font='Arial 20')
    display_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
    btn1 = t.Button(window, text='1', width=5, height=2, font='Arial 15', command=press1)
    btn2 = t.Button(window, text='2', width=5, height=2, font='Arial 15', command=press2)
    btn3 = t.Button(window, text='3', width=5, height=2, font='Arial 15', command=press3)
    btn4 = t.Button(window, text='4', width=5, height=2, font='Arial 15', command=press4)
    btn5 = t.Button(window, text='5', width=5, height=2, font='Arial 15', command=press5)
    btn6 = t.Button(window, text='6', width=5, height=2, font='Arial 15', command=press6)
    btn7 = t.Button(window, text='7', width=5, height=2, font='Arial 15', command=press7)
    btn8 = t.Button(window, text='8', width=5, height=2, font='Arial 15', command=press8)
    btn9 = t.Button(window, text='9', width=5, height=2, font='Arial 15', command=press9)
    btn0 = t.Button(window, text='0', width=5, height=2, font='Arial 15', command=press0)

    btn1.grid(row=1, column=0) #grid는 '붙인다'는 의미
    btn2.grid(row=1, column=1)
    btn3.grid(row=1, column=2)
    btn4.grid(row=2, column=0)
    btn5.grid(row=2, column=1)
    btn6.grid(row=2, column=2)
    btn7.grid(row=3, column=0)
    btn8.grid(row=3, column=1)
    btn9.grid(row=3, column=2)
    btn0.grid(row=4, column=1)

    clearBtn = t.Button(window, text='C', width=5, height=2, font='Arial 15', command=press_clear)
    resultBtn = t.Button(window, text='=', width=5, height=2, font='Arial 15', command=press_result)
    addBtn = t.Button(window, text='+', width=5, height=2, font='Arial 15', command=press_add)
    subBtn = t.Button(window, text='-', width=5, height=2, font='Arial 15', command=press_sub)
    mulBtn = t.Button(window, text='X', width=5, height=2, font='Arial 15', command=press_mul)
    divBtn = t.Button(window, text='/', width=5, height=2, font='Arial 15', command=press_div)

    clearBtn.grid(row=4, column=0)
    resultBtn.grid(row=4, column=2)
    addBtn.grid(row=1, column=3)
    subBtn.grid(row=2, column=3)
    mulBtn.grid(row=3, column=3)
    divBtn.grid(row=4, column=3)

def press0():
    global expression
    expression = expression + '0'
    display_label['text'] = expression

def press1():
    global expression
    expression = expression + '1'
    display_label['text'] = expression

def press2():
    global expression
    expression = expression + '2'
    display_label['text'] = expression

def press3():
    global expression
    expression = expression + '3'
    display_label['text'] = expression

def press4():
    global expression
    expression = expression + '4'
    display_label['text'] = expression

def press5():
    global expression
    expression = expression + '5'
    display_label['text'] = expression

def press6():
    global expression
    expression = expression + '6'
    display_label['text'] = expression

def press7():
    global expression
    expression = expression + '7'
    display_label['text'] = expression

def press8():
    global expression
    expression = expression + '8'
    display_label['text'] = expression

def press9():
    global expression
    expression = expression + '9'
    display_label['text'] = expression

def press_add():
    global expression
    expression = expression + '+'
    display_label['text'] = expression

def press_sub():
    global expression
    expression = expression + '-'
    display_label['text'] = expression

def press_mul():
    global expression
    expression = expression + '*'
    display_label['text'] = expression

def press_div():
    global expression
    expression = expression + '/'
    display_label['text'] = expression #except (error)설명하는 부분 놓쳤음.

def press_clear():
    global expression
    expression = ''
    display_label['text'] = '0'

def press_result():
    global expression
    total = str(eval(expression))
    display_label['text'] = total
    expression = ''

setup_GUI()
window.mainloop()