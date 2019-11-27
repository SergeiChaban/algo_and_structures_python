from datetime import datetime


def time_test(func):
    def wrapper():
        start = datetime.now()
        result = func()
        print(datetime.now() - start)
        return result
    return wrapper


@time_test
def first():
    m = []
    for i in range(10**4):
        if i % 2 == 0:
            m.append(i)
    return m


@time_test
def second():
    m = [x for x in range(10**4) if x % 2 == 0]
    return m


m1 = first()
m2 = second()

