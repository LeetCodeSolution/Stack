# 级别映射
levels = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
}


def transform(expression):
    """
    中缀转后缀
    :param expression:
    :return:
    """
    expression = list(expression)
    ops = []
    result = ''
    while len(expression):
        item = expression.pop(0)
        # 数字直接输出
        if item.isdigit():
            result += item
        # 左括号直接压栈
        elif item == '(':
            ops.append(item)
        # 后括号直接提栈直到遇到左括号
        elif item == ')':
            while len(ops):
                op = ops.pop()
                if op == '(':
                    break
                result += op
        else:
            # 其他算术运算符看优先级
            while len(ops) >= 0:
                if len(ops) == 0:
                    ops.append(item)
                    break
                op = ops.pop()
                # 栈顶是左括号或者栈顶优先级低，栈顶元素取出后压回，新符号也压栈
                if op == '(' or levels[item] > levels[op]:
                    ops.append(op)
                    ops.append(item)
                    break
                else:
                    # 否则将符号弹出并输出
                    result += op
    while len(ops):
        result += ops.pop()
    return result


def calculate(expression):
    """
    逆波兰表达式计算
    :param expression:
    :return:
    """
    expression = list(expression)
    stack = []
    while len(expression):
        item = expression.pop(0)
        if item in ['+', '-', '*', '/']:
            op = item
            item2 = stack.pop()
            item1 = stack.pop()
            # 直接利用 eval 计算，不用判断符号
            result = eval(str(item1) + op + str(item2))
            stack.append(result)
        else:
            stack.append(item)
    # 最后的结果就是运算结果
    return stack.pop()


expression = '6*(5+(2-3)*8+3)'
print('Expression:', expression)
expression = transform(expression)
print('Transform Result:', expression)
result = calculate(expression)
print('Result:', result)
