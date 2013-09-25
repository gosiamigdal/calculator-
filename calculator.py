first_num = int(raw_input("Type first number "))
operator = raw_input("Type an operator ")
second_num = int(raw_input("Type second numbers "))

cont = 1
while cont == 1:
    if operator == "+":
        result = first_num + second_num
    elif operator == "-":
        result = first_num - second_num
    print result

    cont = int(raw_input("Continue (0=not 1=yes)? "))
    operator = raw_input("Type an operator ")+
    second_num = int(raw_input("Type second numbers "))
