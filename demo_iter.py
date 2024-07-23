#!/usr/bin/python
# Summary:
#   1. iter()的另外一种用法，iter(callable, sentinel)，
#       以次方式调用iter()函数时，会得到一个特殊的迭代器对象，
#       循环遍历这个迭代器，会不断返回callable()的结果，加入结果等于sentinel，迭代过程中止
import sys
from functools import partial
from collections import defaultdict


def count_digits_v1(file):
    count = 0
    block_size = 1024 * 8
    with open(file) as f:
        _read = partial(f.read, block_size)
        for chunk in iter(_read, ""):
            for s in chunk:
                if s.isdigit():
                    count += 1
        return count


def read_digits(fp, block_size=1024 * 8):
    _read = partial(fp.read, block_size)
    for chunk in iter(_read, ""):
        for s in chunk:
            if s.isdigit():
                yield s


def count_digits(file):
    with open(file) as f:
        count = 0
        for s in read_digits(f):
            count += 1
    return count


def count_digits_even(file):
    counter = defaultdict(int)
    with open(file) as f:
        for num in read_digits(f):
            if int(num) % 2 == 0:
                counter[int(num)] += 1
    return counter


if __name__ == '__main__':
    counts = count_digits(r"D:\Dev\Code\data\iter.txt")
    print(counts)