from interpreter.ui.ui_controller import UIController
import colorama

class EnhancedUI(UIController):

    def __init__(self):
        self._input_num = 0 
        colorama.init()

    def input(self): 
        self._input_num += 1 
        print(colorama.Fore.GREEN + "\nIn  [", end='')
        print(colorama.Style.BRIGHT + str(self._input_num), end='')
        print(colorama.Style.RESET_ALL, end='')
        print(colorama.Fore.GREEN + "]: ", end='')
        print(colorama.Style.RESET_ALL, end='')
        return input()

    def display(self, value, options=None): 
        print(colorama.Style.RESET_ALL, end='')
        if not options: 
            print(colorama.Fore.RED + "Out [", end='')
            print(colorama.Style.BRIGHT + str(self._input_num), end='')
            print(colorama.Style.RESET_ALL, end='')
            print(colorama.Fore.RED + "]: ", end='')
            print(colorama.Style.RESET_ALL, end='')

        print(value)