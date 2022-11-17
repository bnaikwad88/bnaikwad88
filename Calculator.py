import tkinter
from tkinter import *
from tkinter import messagebox
import math

# window
window = Tk()
window.title("Calculator")
window.geometry("370x670")
window.resizable(0, 0)

# Global Values
value = ""
Int = 0
operator = ""


def btn1_clicked():
    global value
    value = value + "1"
    data.set(value)


def btn2_clicked():
    global value
    value = value + "2"
    data.set(value)


def btn3_clicked():
    global value
    value = value + "3"
    data.set(value)


def btn4_clicked():
    global value
    value = value + "4"
    data.set(value)


def btn5_clicked():
    global value
    value = value + "5"
    data.set(value)


def btn6_clicked():
    global value
    value = value + "6"
    data.set(value)


def btn7_clicked():
    global value
    value = value + "7"
    data.set(value)


def btn8_clicked():
    global value
    value = value + "8"
    data.set(value, )


def btn9_clicked():
    global value
    value = value + "9"
    data.set(value)


def btn0_clicked():
    global value
    value = value + "0"
    data.set(value)


def sin_clicked():
    global value
    value = value + "Sin"
    data.set(value)


def bck_clicked():
    global Int
    global operator
    global value
    global value
    value = value[:-1]
    data.set(value)


def dot_clicked():
    global Int
    global operator
    global value
    global value
    value = value + "."
    data.set(value)


def addn_clicked():
    global Int
    global operator
    global value
    Int = int(value)
    operator = "+"
    value = value + "+"
    data.set(value)


def sub_clicked():
    global Int
    global operator
    global value
    Int = int(value)
    operator = "-"
    value = value + "-"
    data.set(value)


def div_clicked():
    global Int
    global operator
    global value
    Int = int(value)
    operator = "/"
    value = value + "/"
    data.set(value)


def mul_clicked():
    global Int
    global operator
    global value
    Int = int(value)
    operator = "*"
    value = value + "*"
    data.set(value)


def clear_clicked():
    global Int
    global operator
    global value
    value = ""
    Int = 0
    operator = ""
    data.set(value)


def sqrt():
    global value
    value = math.sqrt(float(value))
    data.set(float(value))
    value = str(value)


def sqr():
    global value
    value = (int(value) ** 2)
    data.set(round(value))
    value = str(value)


def per():
    global value
    value = (int(value) / 100)
    data.set(float(value))
    value = str(value)


def sin():
    global value
    value = float(value)
    value = round(math.sin(math.radians(value)), 5)
    data.set(value)
    value = str(value)


def cos():
    global value
    value = float(value)
    value = round(math.cos(math.radians(value)), 5)
    data.set(value)
    value = str(value)


def tan():
    global value
    value = float(value)
    value = round(math.tan(math.radians(value)), 5)
    data.set(value)
    value = str(value)


def rslt_clicked():
    global Int
    global operator
    global value
    value1 = value
    if operator == "+":
        x = int((value1.split("+")[1]))
        res = Int + x
        data.set(res)
        value = str(res)
    elif operator == "-":
        x = int((value1.split("-")[1]))
        res = Int - x
        data.set(res)
        value = str(res)
    elif operator == "*":
        x = int((value1.split("*")[1]))
        res = Int * x
        data.set(res)
        value = str(res)
    elif operator == "/":
        x = int((value1.split("/")[1]))
        if x == 0:
            messagebox.showerror("Error, Division by zero not allowed")
            Int = ""
            value = ""
            data.set(value)
        else:
            res = int(Int / x)
            data.set(res)
            value = str(res)
    elif operator == "Sin":
        value = float(value)
        value = round(math.sin(math.radians(value)), 5)
        data.set(value)
        value = str(value)
    elif operator == ".":
        x = float((value1.split(".")[1]))
        res = Int.x
        data.set(res)
        value = float(res)


# expression Frame
exp_frame = Frame(master=window, height=250, bg="#F2F1F0")
exp_frame.pack(expand=True, fill="both")

# total label
data = StringVar()
ttl_lbl = Label(exp_frame, text="Label", textvariable=data, anchor=SE, bg="#F2F1F0",
                fg="#25265E", padx=24, font=("din", 20))
ttl_lbl.pack(expand=True, fill='both')

# Button Frame
bttn_frame = Frame(master=window)
bttn_frame.pack(expand=True, fill="both")

for i in range(1, 5):
    bttn_frame.rowconfigure(i, weight=1)
    bttn_frame.columnconfigure(i, weight=1)

# Buttons
button0 = Button(master=bttn_frame, text='0', bg="seashell", fg="#25265E", font=("din", 24, "bold"),
                 borderwidth=0, command=btn0_clicked)
button0.grid(row=5, column=1, sticky=NSEW)

button_dec = Button(master=bttn_frame, text='.', bg="seashell", fg="#25265E", font=("din", 24, "bold"),
                    borderwidth=0, command=dot_clicked)
button_dec.grid(row=5, column=2, sticky=NSEW)

button_back = Button(master=bttn_frame, text='⌫', bg="seashell", fg="#25265E", font=("din", 24, "bold"),
                     borderwidth=0, command=bck_clicked)
button_back.grid(row=5, column=3, sticky=NSEW)

button_eql = Button(master=bttn_frame, text='=', bg="seashell", fg="#25265E", font=("din", 24, "bold"),
                    borderwidth=0, command=rslt_clicked)
button_eql.grid(row=5, column=4, sticky=NSEW)

button1 = Button(master=bttn_frame, text='1', bg="seashell", fg="#25265E", font=("din", 24, "bold"),
                 borderwidth=0, command=btn1_clicked)
button1.grid(row=4, column=1, sticky=NSEW)

button2 = Button(master=bttn_frame, text='2', bg="seashell", fg="#25265E", font=("din", 24, "bold"),
                 borderwidth=0, command=btn2_clicked)
button2.grid(row=4, column=2, sticky=NSEW)

button3 = Button(master=bttn_frame, text='3', bg="seashell", fg="#25265E", font=("din", 24, "bold"),
                 borderwidth=0, command=btn3_clicked)
button3.grid(row=4, column=3, sticky=NSEW)

button_sub = Button(master=bttn_frame, text='-', bg="seashell", fg="#25265E", font=("din", 24, "bold"),
                    borderwidth=0, command=sub_clicked)
button_sub.grid(row=4, column=4, sticky=NSEW)

button4 = Button(master=bttn_frame, text='4', bg="seashell", fg="#25265E", font=("din", 24, "bold"),
                 borderwidth=0, command=btn4_clicked)
button4.grid(row=3, column=1, sticky=NSEW)

button5 = Button(master=bttn_frame, text='5', bg="seashell", fg="#25265E", font=("din", 24, "bold"),
                 borderwidth=0, command=btn5_clicked)
button5.grid(row=3, column=2, sticky=NSEW)

button6 = Button(master=bttn_frame, text='6', bg="seashell", fg="#25265E", font=("din", 24, "bold"),
                 borderwidth=0, command=btn6_clicked)
button6.grid(row=3, column=3, sticky=NSEW)

button_add = Button(master=bttn_frame, text='+', bg="seashell", fg="#25265E", font=("din", 24, "bold"),
                    borderwidth=0, command=addn_clicked)
button_add.grid(row=3, column=4, sticky=NSEW)

button7 = Button(master=bttn_frame, text='7', bg="seashell", fg="#25265E", font=("din", 24, "bold"),
                 borderwidth=0, command=btn7_clicked)
button7.grid(row=2, column=1, sticky=NSEW)

button8 = Button(master=bttn_frame, text='8', bg="seashell", fg="#25265E", font=("din", 24, "bold"),
                 borderwidth=0, command=btn8_clicked)
button8.grid(row=2, column=2, sticky=NSEW)

button9 = Button(master=bttn_frame, text='9', bg="seashell", fg="#25265E", font=("din", 24, "bold"),
                 borderwidth=0, command=btn9_clicked)
button9.grid(row=2, column=3, sticky=NSEW)

button_mul = Button(master=bttn_frame, text='x', bg="seashell", fg="#25265E", font=("din", 24, "bold"),
                    borderwidth=0, command=mul_clicked)
button_mul.grid(row=2, column=4, sticky=NSEW)

button_sqrt = Button(master=bttn_frame, text='√', bg="seashell", fg="#25265E", font=("din", 24, "bold"),
                     borderwidth=0, command=sqrt)
button_sqrt.grid(row=1, column=1, sticky=NSEW)

button_sqr = Button(master=bttn_frame, text='x²', bg="seashell", fg="#25265E", font=("din", 24, "bold"),
                    borderwidth=0, command=sqr)
button_sqr.grid(row=1, column=2, sticky=NSEW)

button_per = Button(master=bttn_frame, text='%', bg="seashell", fg="#25265E", font=("din", 24, "bold"),
                    borderwidth=0, command=per)
button_per.grid(row=1, column=3, sticky=NSEW)

button_div = Button(master=bttn_frame, text='/', bg="seashell", fg="#25265E", font=("din", 24, "bold"),
                    borderwidth=0, command=div_clicked)
button_div.grid(row=1, column=4, sticky=NSEW)

button_clear = Button(master=bttn_frame, text='C', bg="seashell", fg="#25265E", font=("din", 24, "bold"),
                      borderwidth=0, command=clear_clicked)
button_clear.grid(row=0, column=1, sticky=NSEW)

button_sin = Button(master=bttn_frame, text='Sin', bg="seashell", fg="#25265E", font=("din", 24, "bold"),
                    borderwidth=0, command=sin)
button_sin.grid(row=0, column=2, sticky=NSEW)

button_cos = Button(master=bttn_frame, text='Cos', bg="seashell", fg="#25265E", font=("din", 24, "bold"),
                    borderwidth=0, command=cos)
button_cos.grid(row=0, column=3, sticky=NSEW)

button_tan = Button(master=bttn_frame, text='Tan', bg="seashell", fg="#25265E", font=("din", 24, "bold"),
                    borderwidth=0, command=tan)
button_tan.grid(row=0, column=4, sticky=NSEW)

window.mainloop()
