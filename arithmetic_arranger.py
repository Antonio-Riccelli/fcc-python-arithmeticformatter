def arithmetic_arranger(problems, sol=False):
  first_line = ""
  second_line = ''
  third_line = ''
  fourth_line = ''

  if len(problems) > 5:
    return 'Error: Too many problems.'

  split_problems = [el.split(" ") for el in problems]

  for el in split_problems:
    if el[0].isdigit() is False or el[2].isdigit() is False:
        return "Error: Numbers must only contain digits."
    if len(el[0]) > 4 or len(el[2]) > 4:
        return "Error: Numbers cannot be more than four digits."
    if el[1] != "+" and el[1] != "-":
        return "Error: Operator must be '+' or '-'."

  num1_lst = [el[0] for el in split_problems]
  num2_lst = [el[2] for el in split_problems]
  operands = [el[1] for el in split_problems]

  for x in range(len(problems)):
    num1_len = len(num1_lst[x])
    num2_len = len(num2_lst[x])

    if x > 0:
        first_line += "    "
        second_line += '    '
    if num1_len >= num2_len:
        first_line += "{}{}".format("  ", num1_lst[x])
    if num1_len < num2_len:
        first_line += "{}{}".format(
            ' ' * (2 + (num2_len - num1_len)), num1_lst[x])
    if x == len(problems):
        first_line += '\n'
        second_line += '\n'
        third_line += '\n'


    # second line
    if num2_len >= num1_len:
        second_line += "{} {}".format(operands[x], num2_lst[x])
    if num2_len < num1_len:
        whitesp = ' ' * (1 + (num1_len - num2_len))
        second_line += "{}{}{}".format(operands[x], whitesp, num2_lst[x])

    # third line
    dashes = "-" * (2 + max([len(x) for x in split_problems[x]]))
    third_line += dashes
    if x < len(problems) - 1:
        third_line += "    "

    # solution
    if sol is True:
        num1 = int(split_problems[x][0])
        num2 = int(split_problems[x][2])
        operand = split_problems[x][1]
        op_result = 0
        if operand == "+":
          op_result = int(num1 + num2)
        elif operand == "-":
          op_result = int(num1 - num2)
        whitesp = int(len(dashes) - len(str(op_result)))
        fourth_line += "{}{}".format(" " * whitesp, op_result)

        if x < len(problems) - 1:
              fourth_line += "    "

  arranged_problems = first_line + "\n" + second_line + "\n" + third_line 
  if sol is True:
      arranged_problems += "\n" + fourth_line

  return arranged_problems