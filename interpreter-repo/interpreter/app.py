import sys 

from interpreter.ui.basic import BasicUI
from interpreter.ui.enhanced import EnhancedUI
from interpreter.evaluators.rpn import evaluate

def print_usage():
    print("usage: interpreter [-i infix_expression | -e]\n\t-i infix_expression = immediate mode. The interpreter immediately evaluates the provided infix_expression and exits.\n\t-e = Run the enhanced user interface (default: basic).")

def run_evaluator(ui, expr):
    value = evaluate(expr)
    if value: 
        ui.display(value)
    else:
        ui.display(f"Could not evaluate expression:{expr}")

def run_REPL(ui, init_options=None): 
    ui.display("Welcome to the Simple Arithmetic Interpreter.\nEnter in an infix expression or \"exit\" to quit.", init_options)
    expr = ui.input().strip() 
    while expr != "exit":
        run_evaluator(ui, expr) 
        expr = ui.input().strip() 

def run():

    if len(sys.argv) == 1: 
        ui = BasicUI() 
        run_REPL(ui) 
    elif len(sys.argv) <= 3:
        if sys.argv[1] == '-i':
            infix_expr = sys.argv[2]
            run_evaluator(BasicUI(), infix_expr) 
        elif sys.argv[1] == '-e':
            ui = EnhancedUI() 
            run_REPL(ui,True) 
        else:
            print_usage() 
    else: 
        print_usage() 





