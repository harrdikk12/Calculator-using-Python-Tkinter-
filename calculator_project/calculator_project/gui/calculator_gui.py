from tkinter import *
from logic.calculator_logic import CalculatorLogic

class CalculatorGUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Calculator")
        self.root.geometry("644x600")
        self.scvalue = StringVar()
        self.scvalue.set("")
        self.screen = Entry(self.root, textvar=self.scvalue, font="lucida 40 bold")
        self.screen.pack(fill=X, ipadx=8, pady=10, padx=10)
        
        self.logic = CalculatorLogic(self.scvalue, self.screen)  # Initialize logic here
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ["9", "8", "7", "+"],
            ["6", "5", "4", "-"],
            ["3", "2", "1", "*"],
            ["0", "=", "C", "/"]
        ]
        for row in buttons:
            f = Frame(self.root, bg="gray")
            for btn_text in row:
                b = Button(f, text=btn_text, font="lucida 35 bold")
                b.pack(side="left", padx=8, pady=5)
                b.bind("<Button-1>", self.logic.click)
            f.pack()

    def run(self):
        self.root.mainloop()
