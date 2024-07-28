#!/usr/bin/python
# Summary: next()方法的一些使用
from functools import partial


def demo(a, b, c=1):
    print(a, b, c)


def run_partial():
    demo_partial = partial(demo, a=1, b=2)
    demo_partial(a=5, c=4)


if __name__ == '__main__':
    run_partial()
