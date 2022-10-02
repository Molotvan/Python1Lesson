from random import Random


def gen_coordinates():
    random = Random()
    while (1):
        x = random.randint(-10, 10)
        y = random.randint(-10, 10)
        if x != 0 and y != 0:
            break
    return x, y


def quater_definer(x, y):
    q = 0
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    else:
        return 4


print('Плоскость № ' +
      str(quater_definer(gen_coordinates()[0], gen_coordinates()[1])))
