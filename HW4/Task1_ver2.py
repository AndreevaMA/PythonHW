
num_after_comma = int(input('Input a number from -1 to -10: '))
print(num_after_comma)

d_pow = -5
d_precision = 10 ** d_pow
print(d_precision)

i = 2
upper_bound = 4
lower_bound = 4 - 4 / (2 * i - 1)

while upper_bound - lower_bound >= d_precision:
    i += 1
    upper_bound = lower_bound + 4 / (2 * i - 1)
    i += 1
    lower_bound = upper_bound - 4 / (2 * i - 1)

pi = (upper_bound + lower_bound) / 2
pi_str = str(pi)
for i in range(2 + (-1) * num_after_comma):
    print(pi_str[i], end = '')