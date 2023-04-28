import math
import re

class Model:

    def __init__(self) -> None:
        self.res = ""
        self.h = { #словарь, значение будет заменяет ключ в строке
            "×": "*", 
            "÷": "/", 
            "√": "math.sqrt(",
            "e": "math.e",
            "π": "math.pi",
            "!": "math.factorial(",
            "sin": "math.sin(math.radians(",
            "cos": "math.cos(math.radians(",
            "tan": "math.tan(math.radians(",
            "lg": "math.log10(",
            "ln": "self.loge(",
            "d_sqrt": "self.d_sqrt",
                  }

    def d_sqrt(self, base, degree): # для степенного корня
        return pow(base, 1/degree)

    def loge(self, num): # для логарифма по основанию е
        return math.log(num, math.e)

    def CalcPercent(self, result): #это говно-код, но он работает
        try:
            expression = re.search(r"\d+.\d+%", result).group(0)
            result = result.replace(expression, "")

            signs = "+-*/"

            for sign in signs:
                try:
                    SignIndex = expression.index(sign)
                except:
                    pass
            
            if (SignIndex == None):
                return False
            
            base = expression[:SignIndex]
            percent = expression[SignIndex+1:-1]
            sign = expression[SignIndex]

            result += str(f"{float(base)} {sign} {float(percent)} * {float(base)} / 100")
        except:
            pass

        return result

    def ParseResult(self, result):

        #перебор словаря, и замена в примере ключей на значение элемента  
        for key in self.h.keys():
            result = result.replace(key, self.h[key])

        if self.CalcPercent(result) == False:
            return

        #ниже происходит подсчет скобок, если открывающихся больше, 
        #чем закрывающихся, то их количество выравнивается, 
        #путем добавления закрывающихся скобок в конец строки

        OpenBrakes = 0
        CloseBrakes = 0

        for i in result:
            if i == "(":
                OpenBrakes+=1
            if i == ")":
                CloseBrakes+= 1

        for i in range(OpenBrakes-CloseBrakes):
            result += ")";

        return result


    def computation(self, button): #тут определяется, что будет происходить при нажатии той или иной клавиши
        if button == "C": #при нажатии на С 
            self.res = "" #переменная, хранящая пример/результат будет обнулена 
        elif button == "←": # при нажатии на стрелочку
            if self.res == "error":
                self.res = ""
            else:
                self.res = str(self.res)
                self.res = self.res[:len(self.res)-1] #переменная будет укорочена на один символ сзади, путем замены строки на ее срез с первого символа до предпоследнего
        elif isinstance(button, int) or button == "00": #если нажатая клавиша равна 00 или является экземпляром класса int, т.е. является целым числом
            self.res += str(button) #то значение клавиши добавляется в результат
        elif button in "- + × ÷ , ( ) √ e π ! % sin cos tan lg ln".split(): #если нажата одна из кнопок
            self.res+=button #то ее значение добавляется в поле результата 
            # ниже все аналогично
        elif button == "x²":
            self.res+="**2"
        elif button == "xʸ":
            self.res+="**"
        elif button == "ʸ√x":
            self.res+="d_sqrt("
        elif button == "=": 
            try: #отлов ошибок
                self.res = str(eval(self.ParseResult(self.res))) #значение результата передается в функцию "ParseResult", в качестве аргумента.
                                                                 #результат функции вычисляется, переводится в строку и передается в общий результат
            except:
                self.res = "error"

        # if self.res[-2:] == ".0": #округление целого числа к int (4.0 -> 4)
        #     self.res = str(int(self.res))

        return str(self.res)
    
    
