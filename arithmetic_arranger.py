def arithmetic_arranger(problems, sol=False):
  if len(problems) > 5:
    return 'Error: Too many problems.'
  newlst = [el.split(" ") for el in problems]
  num1_lst = [el[0] for el in newlst]

  for el in num1_lst:
    if el.isdigit() is False:
        return "Error: Numbers must only contain digits."
    if len(el) > 4:
        return "Error: Numbers cannot be more than four digits."

  num2_lst = [el[2] for el in newlst]

  for el in num2_lst:
    if el.isdigit() is False:
        return "Error: Numbers must only contain digits."
    if len(el) > 4:
        return "Error: Numbers cannot be more than four digits."

  operands = [el[1] for el in newlst]

  for el in operands:
    if el != "+" and el != "-":
        return "Error: Operator must be '+' or '-'."

  first_line = ""
  second_line = ''
  third_line = ''
  fourth_line = ''

  for x in range(len(problems)):
    if x > 0:
        first_line += "    "
    if len(num1_lst[x]) > len(num2_lst[x]):
        first_line += "{}{}".format("  ", num1_lst[x])
    if len(num1_lst[x]) < len(num2_lst[x]):
        first_line += "{}{}".format(
            ' ' * (2 + (len(num2_lst[x]) - len(num1_lst[x]))), num1_lst[x])
    if (len(num1_lst[x]) == len(num2_lst[x])):
        first_line += "{}{}".format("  ", num1_lst[x])
    if x == len(problems):
        first_line += '\n'

    # second line
    if x > 0:
        second_line += '    '
    if len(num2_lst[x]) > len(num1_lst[x]):
        second_line += "{} {}".format(operands[x], num2_lst[x])
    if len(num2_lst[x]) < len(num1_lst[x]):
        whitesp = ' ' * (1 + (len(num1_lst[x]) - len(num2_lst[x])))
        second_line += "{}{}{}".format(operands[x], whitesp, num2_lst[x])
    if len(num2_lst[x]) == len(num1_lst[x]):
        second_line += "{} {}".format(operands[x], num2_lst[x])
    if x == len(problems):
        second_line += '\n'

    # third line
    dashes = "-" * (2 + max([len(x) for x in newlst[x]]))
    third_line += dashes
    if x == len(problems):
      third_line += '\n'
    elif x < len(problems) - 1:
        third_line += "    "

    # solution
    if sol is True:
        num1 = int(newlst[x][0])
        num2 = int(newlst[x][2])
        operand = newlst[x][1]
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