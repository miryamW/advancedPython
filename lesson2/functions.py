def find_primes(x):
    numbers = []
    for num in range(x):

        if num > 1:

            for i in range(2, num):
                if (num % i) == 0:
                    break

            else:
                numbers.append(num)
    return numbers


def sort_list(num_list):
    return sorted(num_list)


def calculate_expression(str):
    sum_str = 0
    for c in str:
        sum_str += int(c)
    return sum_str



