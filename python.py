#imports
from tkinter import *
from tkinter import ttk
import tkinter
#end imports


#frame
class Application(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        root.title('My First Program')

    #buttons
    def create_widgets(self):
        self.hi_there = tkinter.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tkinter.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

        self.test = tkinter.Button(self)
        self.test["text"] = "This is a test button, can it do math?"
        self.test["command"] = self.do_math
        self.test.pack(side="top")

        self.nextStep = tkinter.Button(self)
        self.nextStep["text"] = "nextStep is cool!"
        self.nextStep["command"] = self.output
        self.nextStep.pack()

    def say_hi(self):
        print("hi there, everyone!")
    
    def do_math(self):
        print(5 * 50)

    def output(self):
        print("Think Different!")

    
root = tkinter.Tk()
app= Application(master=root)
app.mainloop()

