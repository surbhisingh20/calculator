# Surbhi Singh

def is_operator(x):
    return x == '+' or x == '-' or x == '/' or x == '*'


# returns true if x has greater precedence than y
# ( -> +,- -> /,*
def x_greater_than_y(x, y):
    if x == y:
        return False
    elif x == "(":
        return False
    elif x == "+" or x == "-":
        return False
    elif y == "*" or y == "/":
        return False
    return True


# given a list in postfix notation, computes value of equation
def evaluate_postfix(output_queue):
    ans_stack = []
    for tok in output_queue:
        if is_operator(tok):
            val1 = ans_stack.pop()
            val2 = ans_stack.pop()
            ans_stack.append(operate(val2, val1, tok))
        else:
            ans_stack.append(tok)
    return ans_stack.pop()


def operate(num1, num2, op):
    num1 = float(num1)
    num2 = float(num2)
    if op == '+':
        return num1 + num2
    if op == '-':
        return num1 - num2
    if op == "*":
        return num1 * num2
    if op == '/':
        return num1 / num2


def infix_to_postfix(infix):
    postfix, op_stack = [], []
    i = 0
    while i < len(infix):
        # read token
        token = infix[i]
        if token.isnumeric():  # allows multiple digit numbers to be read as a single token
            while i < len(infix) - 1 and infix[i + 1].isnumeric():
                token += infix[i + 1]
                i += 1
        # use token
        if token == '(':
            op_stack.append(token)
        elif token == ')':
            # removes operators after first left bracket onto output queue
            while len(op_stack) > 0 and op_stack[len(op_stack) - 1] != '(':
                x = op_stack.pop()
                postfix.append(x)
            op_stack.pop()
        elif is_operator(token):
            # adds operators to stack and moves operators on the top of the stack
            # with greater precedence to output queue
            while len(op_stack) > 0 and x_greater_than_y(op_stack[-1], token):
                x = op_stack.pop()
                postfix.append(x)
            op_stack.append(token)
        else:
            postfix.append(token)
        i += 1

    # moves operators from op_stack to postfix
    while len(op_stack) != 0:
        x = op_stack.pop()
        postfix.append(x)
    return postfix


if __name__ == "__main__":
    # infix = "3+((12)-5)*5"
    infix = input("Enter equation: ")
    print("infix", infix)
    postfix = infix_to_postfix(infix)
    print("postfix", postfix)
    ans = evaluate_postfix(postfix)
    print("answer: ", ans)
