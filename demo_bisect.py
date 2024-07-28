#!/usr/bin/python
# Summary: bisect模块的用法
import bisect


def run_bisect(ratio: str):
    break_points = (6, 7, 8, 8.5)
    # bisect is default eq bisect_right
    scores = ("D", "C", "B", "A", "S")
    idx = bisect.bisect(break_points, float(ratio))
    return scores[idx]


if __name__ == '__main__':
    res = run_bisect("9.1")
    print(res)
