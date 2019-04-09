import sys

sys.path.append("../")

from leetcode_utils import run_function

def my_atoi(s: str) -> int:
    s = s.lstrip()
    if not s:
        return 0

    sign = ''
    if s[0] in ['+', '-']:
        sign = s[0]
        s = s[1:]
    result = []
    try:
        for c in s:
            int(c)
            result.append(c)
    except ValueError:
        pass

    if not result:
        return 0

    result = int('{}{}'.format(sign, ''.join(result)))
    if result <= pow(-2,31):
        return pow(-2,31)
    elif result >= pow(2,31):
        return pow(2,31) - 1

    return result


run_function(1, my_atoi, "12345r566")
