import tkinter

colors = ["gray", "red", "green"]
lastButton = ""
num = 0


def changeWindow(color=None):
    global num
    if type(color) is str:
        window.configure(bg=color)
    else:
        if num == 0:
            window.configure(bg=colors[0])
        elif num < 0:
            window.configure(bg=colors[1])
        else:
            window.configure(bg=colors[2])


def yellowWindow(event):
    window.configure(bg="yellow")


def labelClick(event):
    global num
    if lastButton == "Up":
        num *= 3
    else:
        num /= 3
    stringvar.set(str(int(num)))


def goUp():
    global lastButton
    global num
    lastButton = "Up"
    num += 1
    stringvar.set(str(int(num)))
    changeWindow()


def goDown():
    global num
    global lastButton
    lastButton = "Down"
    num -= 1
    stringvar.set(str(int(num)))
    changeWindow()





window = tkinter.Tk()
up = tkinter.Button(window, text="Up", command=goUp)
down = tkinter.Button(window, text="down", command=goDown)

window.title("Clicker")

window.geometry("200x100")


stringvar = tkinter.StringVar(value=str(num))

label1 = tkinter.Label(
    window,
    bg="white",
    fg="orange"
)

label1.bind("<Enter>", yellowWindow)
label1.bind("<Leave>", changeWindow)
label1.bind("<Double-Button-1>", labelClick)

label1.configure(textvariable=stringvar)

up.pack()
label1.pack()
down.pack()

window.mainloop()