

import re


def isWeekEnd(d):
    if int(d) > 5:
        print("выходной день")
    else:
        print("Будний день")


isWeekEnd(input())
