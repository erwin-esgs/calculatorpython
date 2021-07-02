import tkinter as tk
from tkinter.ttk import*

master = tk.Tk()
master.title("Calculator Sederhana")
master.geometry("350x150")

value = 0
operation = []

v = tk.StringVar()
entry1 = tk.Entry(master, text=v, width=40)
v.set(str(value))
entry1.configure(state='readonly')
entry1.grid(row=0, column=0, columnspan=3)


def buttonClear():
    global value, operation
    value = 0
    v.set(str(value))
    operation = []


def buttonClick(stringval):
    global value
    value = int(str(value)+stringval)
    v.set(str(value))


def executeOperation():
    global operation
    if(operation[1] == '+'):
        value = operation[0]+operation[2]
        v.set(str(value))
    else:
        if(operation[1] == '-'):
            value = operation[0]-operation[2]
            v.set(str(value))
        else:
            if(operation[1] == 'x'):
                value = operation[0]*operation[2]
                v.set(str(value))
            else:
                if(operation[1] == '/'):
                    value = operation[0]/operation[2]
                    v.set(str(value))


def buttonOperation(stringval):
    global value, operation
    if(stringval == '+'):
        if (len(operation) == 0):
            operation.append(float(v.get()))
            operation.append('+')
            value = 0
            # print(operation)
        else:
            if (len(operation) == 2):
                del operation[-1]
                operation.append('+')
                # print(operation)
            else:
                operation.append(value)
                executeOperation()
                operation = []
                operation.append(float(v.get()))
                operation.append('+')
                value = 0
                # print(operation)

    if(stringval == '-'):
        if (len(operation) == 0):
            operation.append(float(v.get()))
            operation.append('-')
            value = 0
            # print(operation)

        else:
            if (len(operation) == 2):
                del operation[-1]
                operation.append('-')
                # print(operation)

            else:
                operation.append(value)
                executeOperation()
                operation = []
                operation.append(float(v.get()))
                operation.append('-')
                value = 0
                # print(operation)

    if(stringval == 'x'):
        if (len(operation) == 0):
            operation.append(float(v.get()))
            operation.append('x')
            value = 0
            # print(operation)

        else:
            if (len(operation) == 2):
                del operation[-1]
                operation.append('x')
                # print(operation)

            else:
                operation.append(value)
                executeOperation()
                operation = []
                operation.append(float(v.get()))
                operation.append('x')
                value = 0
                # print(operation)

    if(stringval == '/'):
        if (len(operation) == 0):
            operation.append(float(v.get()))
            operation.append('/')
            value = 0
            # print(operation)

        else:
            if (len(operation) == 2):
                del operation[-1]
                operation.append('/')
                # print(operation)

            else:
                operation.append(value)
                executeOperation()
                operation = []
                operation.append(float(v.get()))
                operation.append('/')
                value = 0
                # print(operation)

    if(stringval == '='):
        if (len(operation) > 1):
            operation.append(value)
            executeOperation()
            value = 0
            operation = []
            # print(operation)


button1 = tk.Button(master, text="1", width=10,
                    command=lambda: buttonClick("1"))
button1.grid(row=1, column=0)

button2 = tk.Button(master, text="2", width=10,
                    command=lambda: buttonClick("2"))
button2.grid(row=1, column=1)

button3 = tk.Button(master, text="3", width=10,
                    command=lambda: buttonClick("3"))
button3.grid(row=1, column=2)

button4 = tk.Button(master, text="4", width=10,
                    command=lambda: buttonClick("4"))
button4.grid(row=2, column=0)

button5 = tk.Button(master, text="5", width=10,
                    command=lambda: buttonClick("5"))
button5.grid(row=2, column=1)

button6 = tk.Button(master, text="6", width=10,
                    command=lambda: buttonClick("6"))
button6.grid(row=2, column=2)

button7 = tk.Button(master, text="7", width=10,
                    command=lambda: buttonClick("7"))
button7.grid(row=3, column=0)

button8 = tk.Button(master, text="8", width=10,
                    command=lambda: buttonClick("8"))
button8.grid(row=3, column=1)

button9 = tk.Button(master, text="9", width=10,
                    command=lambda: buttonClick("9"))
button9.grid(row=3, column=2)

button0 = tk.Button(master, text="0", width=10,
                    command=lambda: buttonClick("0"))
button0.grid(row=4, column=1)

buttonequal = tk.Button(master, text="=", width=10,
                        command=lambda: buttonOperation("="))
buttonequal.grid(row=4, column=2)

buttonplus = tk.Button(master, text="+", width=10,
                       command=lambda: buttonOperation("+"))
buttonplus.grid(row=1, column=3)

buttonminus = tk.Button(master, text="-", width=10,
                        command=lambda: buttonOperation("-"))
buttonminus.grid(row=2, column=3)

buttontimes = tk.Button(master, text="x", width=10,
                        command=lambda: buttonOperation("x"))
buttontimes.grid(row=3, column=3)

buttondivide = tk.Button(master, text="/", width=10,
                         command=lambda: buttonOperation("/"))
buttondivide.grid(row=4, column=3)

buttonclear = tk.Button(master, text="CE", width=10,
                        command=lambda: buttonClear())
buttonclear.grid(row=0, column=3)


def keyEvent(key):
    # print(key.keysym)
    if(key.keysym == "0"):
        buttonClick("0")
    if(key.keysym == "1"):
        buttonClick("1")
    if(key.keysym == "2"):
        buttonClick("2")
    if(key.keysym == "3"):
        buttonClick("3")
    if(key.keysym == "4"):
        buttonClick("4")
    if(key.keysym == "5"):
        buttonClick("5")
    if(key.keysym == "6"):
        buttonClick("6")
    if(key.keysym == "7"):
        buttonClick("7")
    if(key.keysym == "8"):
        buttonClick("8")
    if(key.keysym == "9"):
        buttonClick("9")
    if(key.keysym == "plus"):
        buttonOperation("+")
    if(key.keysym == "minus"):
        buttonOperation("-")
    if(key.keysym == "asterisk"):
        buttonOperation("x")
    if(key.keysym == "slash"):
        buttonOperation("/")
    if(key.keysym == "Return"):
        buttonOperation("=")
    if(key.keysym == "equal"):
        buttonOperation("=")
    if(key.keysym == "Escape"):
        buttonClear()
    if(key.keysym == "BackSpace"):
        buttonClear()


master.bind_all('<KeyRelease>', keyEvent)
master.mainloop()
