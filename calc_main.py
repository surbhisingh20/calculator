# Surbhi Singh

def is_operator(x):
    return x == '+' or x == '-' or x == '/' or x == '*'


# returns true if x has greater precedence than y
# order from low to high: (, [+,-], [/,*]
precedences = {"(": 0, "+": 1, "-": 1, "/": 2, "*": 2}
def x_geq_y(x, y):
    return precedences[x] - precedences[y] >= 0


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


# converts infix string into postfix list
def infix_to_postfix(infix):
    postfix, op_stack = [], []
    i = 0
    while i < len(infix):
        print("\t", i, "postfix", postfix, "op_stack", op_stack)
        # read token
        token = infix[i]
        if token.isnumeric() or token == ".":  # allows multiple digit numbers and decimals to be read as a single token
            while i < len(infix) - 1 and (infix[i + 1].isnumeric() or infix[i + 1] == '.'):
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
            while len(op_stack) > 0 and x_geq_y(op_stack[-1], token):
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


if __name__ == "__main__":
    infix = input("Enter equation: ")
    try:
        print("infix", infix)
        postfix = infix_to_postfix(infix)
        print("\npostfix", postfix)
        ans = evaluate_postfix(postfix)
        print("\nanswer: ", ans)
    except:
        print("\ninvalid equation")