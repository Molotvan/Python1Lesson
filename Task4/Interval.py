number = input("Введите номер четверти ")


def Xinterval_definition(number):
    number = int(number)
    if number == 1 or number == 4:
        x_int = "(0 : +Ꝏ     )"
    else:
        x_int = "(0 : -Ꝏ     )"
    return x_int


def Yinterval_definition(number):
    number = int(number)
    if number == 1 or number == 2:
        y_int = "(0 : +Ꝏ     )"
    else:
        y_int = "(0 : -Ꝏ      )"

    return y_int


print("Диапазон значений X: " + Xinterval_definition(number) +
      ", Диапазон значений Y: " + Yinterval_definition(number))
