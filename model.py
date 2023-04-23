class Model:
    def __init__(self) -> None:
        self.res = ""

    def computation(self, button):
        if button == "C":
            self.res = ""
        elif isinstance(button, int):
            self.res += str(button)
        elif button == "+/-":
            if self.res[0] == "-":
                self.res = self.res[1:]
            else:
                self.res = "-" + self.res  
        return self.res