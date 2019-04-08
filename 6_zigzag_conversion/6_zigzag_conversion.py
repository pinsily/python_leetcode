import sys

sys.path.append("../")

from leetcode_utils import run_function


def convert_1(s: str, numRows: int) -> str:
    """[summary]
    
    [Z字型排列字符串]
    :param
        s: [str, ]
        numRows: [row number]
    
    :returns: [str]
    """
    if numRows <= 1:
        return s

    rows = [[] for _ in range(numRows)]
    cur_row, d = 0, 1
    for char in s:
        rows[cur_row].append(char)
        cur_row += d
        if cur_row in [0, numRows - 1]:
            d = -d
    return "".join(["".join(r) for r in rows])


run_function(1, convert_1, "PAYPALISHIRING", 3)
