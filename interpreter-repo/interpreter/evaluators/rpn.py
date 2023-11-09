###
#   Problem Solving with Algorithms and Data Structures using Python
#   Cite: https://runestone.academy/runestone/books/published/pythonds/BasicDS/ConvertingDecimalNumberstoBinaryNumbers.html
#   with a few modifications by Lamont Samuels 
###
from interpreter.collections.stack import Stack 

COMPUTE_DIC = {'*': lambda op1, op2: op1 * op2, 
               '+': lambda op1, op2: op1 + op2, 
               '/': lambda op1, op2: op1 / op2, 
               '-': lambda op1, op2: op1 - op2
              }

def evaluate(infix_expr): 
    '''
    Computes the float value of the given infix expression. 

    Inputs:
      infix_expr (string): the infix expression

    Returns:
      (float) the value after evaluating the infix expression. 
    '''
    post_expr = infix_to_postfix(infix_expr)
    op_stack = Stack() 
    tokens = post_expr.split()

    for token in tokens:
        if token.isdigit():
            op_stack.push(int(token))
        else:
            op2 = op_stack.pop()
            op1 = op_stack.pop()
            fn = COMPUTE_DIC.get(token)         
            op_stack.push(fn(op1,op2))

    value = op_stack.pop()
    return float(value)  

def infix_to_postfix(infix_expr): 
    '''
    Convers the infix expression into postfix

    Inputs:
      infix_expr (string): the infix expression

    Returns:
      (string) the postfix expression for the given infix expression 
    '''
    prec = {"*": 3, "/": 3, "+":2, "-":2, "(":1}  
    op_stack = Stack()
    postfix = []
    tokens = infix_expr.split()

    for token in tokens:
        if token.isdigit():
            postfix.append(token)
        elif token == '(':
            op_stack.push(token)
        elif token == ')':
            topToken = op_stack.pop()
            while topToken != '(':
                postfix.append(topToken)
                topToken = op_stack.pop()
        elif token.isspace():
            continue     
        else:
            while (not op_stack) and \
               (prec[op_stack.peek()] >= prec[token]):
                  postfix.append(op_stack.pop())
            op_stack.push(token)

    while not op_stack:
        postfix.append(op_stack.pop())

    return " ".join(postfix)