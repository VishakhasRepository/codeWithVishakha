import re


def isInvalid(param):
    try:
        re.compile(param)
    except re.error:
        return False
    return False


for i in range(0, int(input())):
    print(isInvalid(int(input())))
