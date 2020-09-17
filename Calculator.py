from tkinter import *

expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)
    
def clear():
    global expression
    expression = ""
    equation.set("")

def equal():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        
    except:
        equation.set("error")
    expression = ""

if __name__ == '__main__':
    
    screen = Tk()

    screen.geometry("350x250")
    screen.title("Simple Calculator")

    equation = StringVar()
    equation.set("Enter your expresssion")

    answer_field = Entry(screen, textvariable = equation)
    answer_field.grid(columnspan = 4, ipadx = 100)

    oneButton = Button(screen,text = '1',bg = 'light blue', activebackground = "red", command = lambda: press(1), height = 3, width = 10)
    oneButton.grid(row = 2, column = 0)

    twoButton = Button(screen,text = '2',bg = 'light blue',activebackground = "red", command = lambda: press(2), height = 3, width = 10)
    twoButton.grid(row = 2, column = 1)

    threeButton = Button(screen,text = '3',bg = 'light blue',activebackground = "red", command = lambda: press(3), height = 3, width = 10)
    threeButton.grid(row = 2, column = 2)

    fourButton = Button(screen,text = '4',bg = 'light blue', activebackground = "red", command = lambda: press(4),height = 3, width = 10)
    fourButton.grid(row = 3, column = 0)

    fiveButton = Button(screen,text = '5',bg = 'light blue', activebackground = "red", command = lambda: press(5),height = 3, width = 10)
    fiveButton.grid(row = 3, column = 1)

    sixButton = Button(screen,text = '6',bg = 'light blue', activebackground = "red", command = lambda: press(6), height = 3, width = 10)
    sixButton.grid(row = 3, column = 2)

    sevenButton = Button(screen,text = '7',bg = 'light blue', activebackground = "red", command = lambda: press(7),height = 3, width = 10)
    sevenButton.grid(row = 4, column = 0)

    eightButton = Button(screen,text = '8',bg = 'light blue',activebackground = "red", command = lambda: press(8), height = 3, width = 10)
    eightButton.grid(row = 4, column = 1)

    nineButton = Button(screen,text = '9',bg = 'light blue', activebackground = "red", command = lambda: press(9),height = 3, width = 10)
    nineButton.grid(row = 4, column = 2)

    zeroButton = Button(screen,text = '0',bg = 'light blue', activebackground = "red", command = lambda: press(0),height = 3, width = 10)
    zeroButton.grid(row = 5, column = 1)

    plusButton = Button(screen,text = '+',bg = 'light blue',activebackground = "red", command = lambda: press("+") ,height = 3, width = 10)
    plusButton.grid(row = 2, column = 3)

    minusButton = Button(screen,text = '-',bg = 'light blue',activebackground = "red", command = lambda: press("-"), height = 3, width = 10)
    minusButton.grid(row = 3, column = 3)

    multiplyButton = Button(screen,text = 'x',bg = 'light blue', activebackground = "red", command = lambda: press("*"),height = 3, width = 10)
    multiplyButton.grid(row = 4, column = 3)

    divideButton = Button(screen,text = '/',bg = 'light blue', activebackground = "red", command = lambda: press("/"),height = 3, width = 10)
    divideButton.grid(row = 5, column = 3)

    clearButton = Button(screen,text = 'CLEAR',bg = 'light blue',activebackground = "red", command = clear, height = 3, width = 10)
    clearButton.grid(row = 5, column = 0)

    equalButton = Button(screen,text = '=',bg = 'light blue', activebackground = "red", command = equal,height = 3, width = 10)
    equalButton.grid(row = 5, column = 2)

    screen.mainloop()
