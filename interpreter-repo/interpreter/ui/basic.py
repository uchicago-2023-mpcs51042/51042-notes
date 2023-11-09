
from interpreter.ui.ui_controller import UIController

class BasicUI(UIController):

    def __init__(self):
        pass

    def input(self): 
        return input(">>> ")

    def  display(self, value, options=None): 
        print(value)
    


