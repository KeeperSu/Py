#!/usr/bin/python
# Summary: next()方法的一些使用


def run_next():
    d1 = {
        "a": 1,
        "b": 2,
    }
    print(d1.keys())
    iterator_d1 = iter(d1)
    print(iterator_d1)
    print(next(iterator_d1))


if __name__ == '__main__':
    run_next()
