from model import Model
from view import View


class Controller:
    def __init__(self) -> None:
        self.model = Model()
        self.view = View(self)

    def main(self):
        self.view.main()

    def ButtonHandler(self, button):
        res = self.model.computation(button)
        self.view.res.set(res)
        

if __name__ == '__main__':
    calculator = Controller()
    calculator.main()
