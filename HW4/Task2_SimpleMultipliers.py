# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

def simple_create(stop_point):
    simple_num_list = [1, ]
    num = 2

    for i in range (2, stop_point):

        flag = 0
        for j in range(2, num):
            if num % j == 0:
                flag = 1
                break

        if flag == 0:
            simple_num_list.append(num)

        num += 1

    return simple_num_list

def main():
    from random import randint

    n = randint(4, 100)
    print(n)

    my_simples = simple_create(100) # создадим список простых чисел от 1 до 100
    print(my_simples)

    multiplier_list = []

    i = 1
    m = n

    while m > 1:
        if m % my_simples[i] == 0:
            multiplier_list.append(my_simples[i])
            m = m / my_simples[i]
            i = 1
        else:
            i += 1

    print(f'The list of simple multipliers of the number {n} is: {multiplier_list}.')

if __name__ == "__main__":
    main()