# Imports libraries
import tkinter as tk
from tkinter.constants import BOTTOM, LEFT, RIGHT, TOP
import tkinter.font as font
from typing import Sized
import webbrowser
import time
import threading
from playsound import playsound

global backgroundcolour
backgrondcolour = "#65FF43"
global buttoncolour
buttoncolour = "#43F1FF"


# Function to be a command for a button. Goes to github website
def Github():
    webbrowser.open("https://github.com/")
# Function to be a command for a button. Goes to stackoverflow website
def Stackoverflow():
    webbrowser.open("https://stackoverflow.com/")
# Function to be a command for a button. Goes to youtue website
def Youtube():
    webbrowser.open("https://www.youtube.com/")
# Opens a new window, which contains the timer function
def Timer():
    # Starts a new thread which handles the timer
    def startthread():
        # Code for reading the entry made by user and is a command for the thread
        def passsecond():
            timeinputted = int(inSeconds.get())
            i = timeinputted
            running = True
            while running:
                time.sleep(1)
                i -= 1
                timelabel.configure(text = str(i))
                if i == 0:
                    playsound("https://quz1yp-a.akamaihd.net/downloads/ringtones/files/mp3/ring2-mp3-6551.mp3")
                    running = False
                else:
                    pass
        thread1 = threading.Thread(target = passsecond)
        thread1.start()
    
    # Setup for new window, with entry box, button and label
    window1 = tk.Tk()
    window1.title("Timer")
    window1.configure(bg = backgrondcolour)
    timelabel = tk.Label(window1, text = "Time")
    timelabel.pack(side = BOTTOM)
    inSeconds = tk.Entry(window1)
    inSeconds.pack(side = LEFT)
    startbutton = tk.Button(window1, text = "Start timer", command = startthread, bg = buttoncolour)
    startbutton.pack(side = LEFT)
    window1.mainloop()

# Todo list function; makes a new window and allows people to add and tick off tasks
def Todolist():
    def addtask():
        def delete():
            tasktext.pack_forget()
            removebutton.pack_forget()
        tasktext = tk.Label(window2, text = task.get())
        tasktext.pack(side = BOTTOM)
        removebutton = tk.Button(window2, text = "Done!", command = delete, bg = buttoncolour)
        removebutton.pack(side = BOTTOM)
    window2 = tk.Tk()
    window2.title("To-do list")
    window2.configure(bg = backgrondcolour)
    addButton = tk.Button(window2, text = "Add", command = addtask, bg = buttoncolour)
    task = tk.Entry(window2)
    task.pack(side = LEFT)
    addButton.pack(side = LEFT)
    instruction = tk.Label(window2, text = "Close the window to reset the to do list")
    instruction.pack(side = BOTTOM)
    window2.mainloop()

# Calculator code; starts a new window and allows people to do math operations
def Calculator():
    def add():
        global operator
        operator = "add"
    def subtract():
        global operator
        operator = "subtract"
    def multiply():
        global operator
        operator = "multiply"
    def divide():
        global operator
        operator = "divide"
    def caret():
        global operator
        operator = "power"
    def equals():
        thefirstnumber = float(number1.get())

        thesecondnumber = float(number2.get())
        if operator == "add":
            result = thefirstnumber + thesecondnumber
        elif operator == "subtract":
            result = thefirstnumber - thesecondnumber
        elif operator == "multiply":
            result = thefirstnumber * thesecondnumber
        elif operator == "divide":
            result = thefirstnumber / thesecondnumber
        elif operator == "power":
            result = thefirstnumber ** thesecondnumber
        finalresult = tk.Label(window3, text = str(result))
        finalresult.pack()
    window3 = tk.Tk()
    window3.title("Calculator")
    window3.configure(bg = backgrondcolour)
    number1 = tk.Entry(window3)
    number1.pack(side = LEFT)
    addoperator = tk.Button(window3, text = "+", command = add, bg = buttoncolour)
    subtractoperator = tk.Button(window3 ,text = "-", command = subtract, bg = buttoncolour)
    divideoperator = tk.Button(window3, text = "÷", command = divide, bg = buttoncolour)
    multiplyoperator = tk.Button(window3, text = "×", command = multiply, bg = buttoncolour)
    poweroperator = tk.Button(window3, text = "^", command = caret, bg = buttoncolour)
    addoperator.pack(side = LEFT)
    subtractoperator.pack(side = LEFT)
    multiplyoperator.pack(side = LEFT)
    divideoperator.pack(side = LEFT)
    poweroperator.pack(side = LEFT)
    number2 = tk.Entry(window3)
    number2.pack(side = LEFT)
    equalsign = tk.Button(window3, text = "=", command = equals, bg = buttoncolour)
    equalsign.pack()
def asciibinaryhex():
    webbrowser.open("https://image.slidesharecdn.com/ascii-conversion-chart-161005051303/95/ascii-conversionchart-1-638.jpg?cb=1475644451")
def info():
    window4 = tk.Tk()
    window4.title("Information")
    window4.configure(bg = backgrondcolour)
    infotext1 = tk.Label(window4, text = "This is the programmers toolkit. It is what every programmer needs.")
    infotext2 = tk.Label(window4, text = "It contains many tools that programmers may find useful while developing, such as a calculator,")
    infotext3 = tk.Label(window4, text = "a to-do list and dedicated buttons to take you to frequently used websites.")
    infotext1.pack()
    infotext2.pack()
    infotext3.pack()
    window4.mainloop()

# Main window setup
window = tk.Tk()
window.title("Toolkit")
window.configure(bg = backgrondcolour)

# Buttons
buttonfont = font.Font(family = "Helvetica", size = 40)
GitHubbutton = tk.Button(text = "GitHub", font = buttonfont, height = 7, width = 7, command = Github, bg = buttoncolour)
GitHubbutton.pack(side = LEFT)
Stackoverflowbutton = tk.Button(text = "Stack", font = buttonfont, height = 7, width = 7, command = Stackoverflow, bg = buttoncolour)
Stackoverflowbutton.pack(side = LEFT)
Youtubebutton = tk.Button(text = "Youtube", font = buttonfont, height = 7, width = 7, command = Youtube, bg = buttoncolour)
Youtubebutton.pack(side = LEFT)
Timerbutton = tk.Button(text = "Timer", font = buttonfont, height = 7, width = 7, command = Timer, bg = buttoncolour)
Timerbutton.pack(side = LEFT)
Todobutton = tk.Button(text = "To do", font = buttonfont, height = 7, width = 7, command = Todolist, bg = buttoncolour)
Todobutton.pack(side = LEFT)
Calculatorbutton = tk.Button(text = "Calculator", font = buttonfont, height = 7, width = 7, command = Calculator, bg = buttoncolour)
Calculatorbutton.pack(side = LEFT)
Asciibinaryhexbutton =tk.Button(text = "Binary", font = buttonfont, height = 7, width = 7, command = asciibinaryhex, bg = buttoncolour)
Asciibinaryhexbutton.pack(side = LEFT)
Infobutton = tk.Button(text = "Info", font = buttonfont, height = 3, width = 3, command = info, bg = buttoncolour)
Infobutton.pack()
# End loop
window.mainloop()