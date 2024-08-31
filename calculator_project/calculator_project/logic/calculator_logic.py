class CalculatorLogic:
    def __init__(self, scvalue, screen):
        self.scvalue = scvalue
        self.screen = screen

    def click(self, event):
        text = event.widget.cget("text")
        print(text)
        if text == "=":
            try:
                value = eval(self.scvalue.get())
                self.scvalue.set(value)
            except Exception as e:
                self.scvalue.set("Error")
            self.screen.update()
        elif text == "C":
            self.scvalue.set("")
            self.screen.update()
        else:
            self.scvalue.set(self.scvalue.get() + text)
            self.screen.update()
