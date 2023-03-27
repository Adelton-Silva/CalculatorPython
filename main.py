from tkinter import *

root = Tk()
root.title('Python calculator')
root.geometry('408x355')
root.minsize(408,355)
root.maxsize(408,355)

num1 = ''
divide = FALSE
multlication = FALSE
add = FALSE
sub = FALSE

root.configure(background='#282828')

e = Entry(root, width=15, borderwidth=4, relief=FLAT, fg='#FFFFFF', bg='#a7a28F', font=('futura', 25, 'bold'), justify=CENTER)
e.grid(
    row=0,
    column=0,
    columnspan=4,
    pady=2
)

#function button click
def button_click(num):
   e.insert(END, num)

#operation functions
#divide function 
def button_divide():
    global num1
    global divide
    divide = TRUE
    num1 = e.get()
    e.delete(0, END)

#multiplication function
def button_multiplication():
    global num1
    global multlication
    multlication = TRUE
    num1 = e.get()
    e.delete(0, END)

#subtraction function
def button_subtraction():
    global num1
    global sub
    sub = TRUE
    num1 = e.get()
    e.delete(0, END)

#add function
def add_button():
    global num1
    global add
    add = TRUE
    num1 = e.get()
    e.delete(0, END)

#clear function
def clear_button():
    e.delete(0, END)

#equal function
def equal_button():
    global sub
    global add
    global multlication
    global divide
    num2 = e.get()
    e.delete(0, END)

    if add == True:
        e.insert(0, int(num1) + int(num2))
        add = FALSE

    if multlication == True:
        e.insert(0, int(num1) * int(num2))
        multlication = FALSE
    
    if sub == True:
        e.insert(0, int(num1) - int(num2))
        sub = FALSE
    
    if divide == True:
        e.insert(0, int(num1) / int(num2))
        divide = FALSE

divide = Button(root,
                text='÷',
                padx=40,
                pady=20,
                command=button_divide,
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
                )
divide.grid(row=0, column=4)

#first row
one = Button(root,
                text='1',
                padx=40,
                pady=20,
                command=lambda: button_click(1),
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
                )
one.grid(row=1, column=1)

two = Button(root,
                text='2',
                padx=40,
                pady=20,
                command=lambda: button_click(2),
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
                )
two.grid(row=1, column=2)

three = Button(root,
                text='3',
                padx=40,
                pady=20,
                command=lambda: button_click(3),
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
                )
three.grid(row=1, column=3)

mult = Button(root,
                text='x',
                padx=40,
                pady=20,
                command=button_multiplication,
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
                )
mult.grid(row=1, column=4)

#second row
four = Button(root,
                text='4',
                padx=40,
                pady=20,
                command=lambda: button_click(4),
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
                )
four.grid(row=2, column=1)

five = Button(root,
                text='5',
                padx=40,
                pady=20,
                command=lambda: button_click(5),
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
                )
five.grid(row=2, column=2)

six = Button(root,
                text='6',
                padx=40,
                pady=20,
                command=lambda: button_click(6),
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
                )
six.grid(row=2, column=3)

sub = Button(root,
                text='-',
                padx=41.5,
                pady=20,
                command=button_subtraction,
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
                )
sub.grid(row=2, column=4)

#third row
seven = Button(root,
                text='7',
                padx=40,
                pady=20,
                command=lambda: button_click(7),
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
                )
seven.grid(row=3, column=1)

eight = Button(root,
                text='8',
                padx=40,
                pady=20,
                command=lambda: button_click(8),
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
                )
eight.grid(row=3, column=2)

nine = Button(root,
                text='9',
                padx=40,
                pady=20,
                command=lambda: button_click(9),
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
                )
nine.grid(row=3, column=3)

add = Button(root,
                text='+',
                padx=40,
                pady=20,
                command=add_button,
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
                )
add.grid(row=3, column=4)

#fourth row
zero = Button(root,
                text='0',
                padx=91,
                pady=20,
                command=lambda: button_click(0),
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
                )
zero.grid(row=4, column=1, columnspan=2)

clear = Button(root,
                text='c',
                padx=40,
                pady=20,
                command=clear_button,
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
                )
clear.grid(row=4, column=3)

equal = Button(root,
                text='=',
                padx=40,
                pady=20,
                command=equal_button,
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
                )
equal.grid(row=4, column=4)


root.mainloop()