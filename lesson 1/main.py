from datetime import datetime

# 1

def time_out(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        func(*args, **kwargs)
        end = datetime.now()
        print(end - start)

    return wrapper


@time_out
def the_numbers_1(i):
    sum = i
    for _ in range(0, 10000000):
        sum += _


@time_out
def the_numbers_2(i):
    sum = i
    for _ in range(0, 100000):
        sum += _


@time_out
def the_numbers_3(i):
    sum = i
    for _ in range(0, 10):
        sum += _


# 2
funcs = {}


def cache(func):
    def wrapper(*args, **kwargs):
        if funcs.get(args[0]):
            return funcs[args[0]]
        else:
            x = func(*args, **kwargs)
            if args[0] is not None:
                funcs[args[0]] = x
            return x

    return wrapper


@cache
def fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


@time_out
def print_fibonacci(i):
    print(fibonacci(i))


if __name__ == '__main__':
    funcs = {}
    the_numbers_1(5)
    the_numbers_2(6)
    the_numbers_3(2)
    print_fibonacci(400)
    print_fibonacci(400)
