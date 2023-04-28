class Model:
    def __init__(self) -> None:
        self.res = ""

    def computation(self, button):
        if button == "C":
            self.res = ""
        elif isinstance(button, int):
            self.res += str(button)
        elif button == "00":
            self.res += "00"
        elif button == "000":
            self.res += "000"
        elif button == "=":
            self.res = str(eval(self.res))
        elif button == "←":
            self.res = self.res[:len(self.res)-1]
        elif button == "(" or button == ")":
            self.res += button
        elif self.res != "":    
            if button == "+":
                self.res += "+"
            elif button == "-":
                self.res += "-"
            elif button == "÷":
                self.res += "/"
            elif button == "×":
                self.res += "*"
            elif button == ",":
                self.res += "."
                
        return self.res