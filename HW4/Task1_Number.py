# Вычислить число Пи c заданной точностью d
# Пример: при d = 0.001, π = 3.141    10 в степ.-1 ≤ d ≤ 10 в степ.-10

def precision_input():
    while True:
        result = int(input('Specify calculation precision as a power of 10 (a number from -1 to -10): '))
        
        flag = 0
        for i in range(-1, -11, -1):
            if i == result:
                flag = 1
                break
        
        if flag == 0:
            print('Error! Try again')
        else:
            return result


def main():
    d_pow = precision_input()
    d_precision = 10 ** d_pow

    i = 2
    upper_bound = 4
    lower_bound = 4 - 4 / (2 * i - 1)

    while upper_bound - lower_bound >= d_precision:
        i += 1
        upper_bound = lower_bound + 4 / (2 * i - 1)
        i += 1
        lower_bound = upper_bound - 4 / (2 * i - 1)

    pi = round((upper_bound + lower_bound) / 2, -d_pow)
    print(pi)

if __name__ == "__main__":
    main()







