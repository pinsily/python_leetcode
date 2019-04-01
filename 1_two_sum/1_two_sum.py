import logging

import sys

sys.path.append("../")

from leetcode_utils import run_function


def two_sum_1(nums: list, target: int) -> list:
    """[summary]

    [双重遍历 for 通不过, 太垃圾了]
    :param
        nums:   list[int]
        target: int

    :returns: list[index]
    """
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and nums[i] + nums[j] == target:
                return [i, j]


def two_sum_2(nums: list, target: int) -> list:
    """[summary]

    [双重遍历 for 采用一些技巧, 减少一半的繁琐]
    :param
        nums:   list[int]
        target: int

    :returns: list[index]
    """
    for i in range(len(nums) - 1):
        subtrahend = target - nums[i]
        for j in range(i + 1, len(nums)):
            if subtrahend == nums[j]:
                return [i, j]

    return []


def two_sum_3(nums: list, target: int) -> list:
    """[summary]

    [在 2 的基础上使用哈希表查询]
    :param
        nums:   list[int]
        target: int

    :returns: list[index]
    """
    nums_dict = {nums[i]: i for i in range(len(nums))}
    for i in range(len(nums)):
        subtrahend = target - nums[i]
        j = nums_dict.get(subtrahend)
        if j != None and j != i:
            return [i, j]

    return []


test_list = [2, 7, 11, 15, 34, 54, 32, 74, 82]
run_function(1, two_sum_1, test_list, 34)
run_function(2, two_sum_2, test_list, 34)
run_function(3, two_sum_3, test_list, 34)
