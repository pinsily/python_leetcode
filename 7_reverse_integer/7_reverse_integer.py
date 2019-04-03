import sys
sys.path.append("../")

from leetcode_utils import run_function


def reverse_1(x: int) -> int:
    """[summary]

    [反转整数]
    :param
        x: [int]

    :returns: [reverse int]
    """
    if x >= 0:
        return reverse_int(str(x))
    else:
        return reverse_int(str(x)[1:])


def reverse_int(x: str) -> int:
    s = list(x)
    for i in range(len(s) // 2):
        s[i], s[len(s) - 1 - i] = s[len(s) - 1 - i], s[i]

    reverse_x = int("".join(s))
    if reverse_x <= -2147483649 or reverse_x > 2147483649:
        return 0
    return reverse_x


def reverse_2(x: int) -> int:
    """[summary]
    
    [很巧妙的方法]
    :param
        x: [description]
    
    :returns: [description]
    """
    reverse_x = 0
    neg = 1
    zero_middle = 0

    # Negative case
    if (x < 0):
        neg = -1
        x = -x

    while (x != 0):
        mod = x % 10
        if (zero_middle != 0):
            reverse_x = reverse_x * 100 + mod
            zero_middle = 0
        elif (mod != 0):
            reverse_x = reverse_x * 10 + mod
        else:
            zero_middle += 1
        x = x // 10

    if (reverse_x > 2147483649) or (reverse_x < -2147483649):
        return 0
    return neg * reverse_x


run_function(1, reverse_1, 12345678)
run_function(2, reverse_2, 12345678)
