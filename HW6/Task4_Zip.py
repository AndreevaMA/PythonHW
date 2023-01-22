# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

#------------------------------------исходный код------------------------------------------

#----------------------считывание входных данных и записывание файла со сжатыми данными------------------------


# path = r'C:\Users\maria\Desktop\Python\PythonHW5\Initial_File.txt' # r в начале решает проблему со считыванием
# file_data = open(path, 'r')
# my_str = ''
# for line in file_data:
#     my_str += line
# file_data.close()

# my_str_list = list(my_str)
# print(my_str_list)

# RLE_keys = []
# RLE_values = []

# cycle_counter = 0
# while cycle_counter < len(my_str_list) - 1:
#     value_counter = 1
#     for i in range(1, len(my_str_list)):
#         if my_str_list[i] == my_str_list[i - 1]:
#             value_counter += 1
#             if i == len(my_str_list) - 1:
#                 RLE_keys.append(value_counter)
#                 RLE_values.append(my_str_list[i])
#         else:
#             RLE_keys.append(value_counter)
#             RLE_values.append(my_str_list[i - 1])
#             value_counter = 1
#             if i == len(my_str_list) - 1:
#                 RLE_keys.append(value_counter)
#                 RLE_values.append(my_str_list[i])
#         cycle_counter += 1

# print(RLE_keys)
# print(RLE_values)

# RLE_warehouse = []

# for i in range(len(RLE_keys)):
#     RLE_warehouse.append((RLE_keys[i], RLE_values[i]))
# print(RLE_warehouse)

# RLE_result = ''
# for element in RLE_warehouse:
#     RLE_result += (f'{element[0]}x{element[1]} ')
# print(RLE_result)

# with open('PythonHW5/RLE_result.txt', 'w', encoding = 'UTF-8') as my_file:
#     my_file.write(RLE_result)

# #----------------------считывание сжатых данных и их распаковка в отдельный файл------------------------

# path = r'C:\Users\maria\Desktop\Python\PythonHW5\RLE_result.txt' # r в начале решает проблему со считыванием
# file_data = open(path, 'r')
# new_str_list = []
# for line in file_data:
#     new_str_list += list(line.split())
# file_data.close()

# print(new_str_list)

# RLE_unpacked = []

# for element in new_str_list:
#     RLE_unpacked.append((int(element[0]), element[2]))
# print(RLE_unpacked)

# str_unpacked = ''

# for element in RLE_unpacked:
#     str_unpacked += element[1] * element[0]
# print(str_unpacked)

# with open('PythonHW5/Unpacked_result.txt', 'w', encoding = 'UTF-8') as my_file:
#     my_file.write(str_unpacked)



#-----------------------------------обновлённый код------------------------------------------

#----------------------считывание входных данных и записывание файла со сжатыми данными------------------------

path = r'C:\Users\maria\Desktop\Python\PythonHW5\Initial_File.txt' # r в начале решает проблему со считыванием
file_data = open(path, 'r')
my_str = ''
for line in file_data:
    my_str += line
file_data.close()

my_str_list = list(my_str)
print(my_str_list)

RLE_keys = []
RLE_values = []

cycle_counter = 0
while cycle_counter < len(my_str_list) - 1:
    value_counter = 1
    for i in range(1, len(my_str_list)):
        if my_str_list[i] == my_str_list[i - 1]:
            value_counter += 1
            if i == len(my_str_list) - 1:
                RLE_keys.append(value_counter)
                RLE_values.append(my_str_list[i])
        else:
            RLE_keys.append(value_counter)
            RLE_values.append(my_str_list[i - 1])
            value_counter = 1
            if i == len(my_str_list) - 1:
                RLE_keys.append(value_counter)
                RLE_values.append(my_str_list[i])
        cycle_counter += 1

print(RLE_keys)
print(RLE_values)

# используем zip
RLE_warehouse = list(zip(RLE_keys, RLE_values))
print(RLE_warehouse)

RLE_result = ''
for element in RLE_warehouse:
    RLE_result += (f'{element[0]}x{element[1]} ')
print(RLE_result)

with open('PythonHW5/RLE_result.txt', 'w', encoding = 'UTF-8') as my_file:
    my_file.write(RLE_result)

#----------------------считывание сжатых данных и их распаковка в отдельный файл------------------------

path = r'C:\Users\maria\Desktop\Python\PythonHW5\RLE_result.txt' # r в начале решает проблему со считыванием
file_data = open(path, 'r')
new_str_list = []
for line in file_data:
    new_str_list += list(line.split())
file_data.close()

print(new_str_list)

RLE_unpacked = []

for element in new_str_list:
    RLE_unpacked.append((int(element[0]), element[2]))
print(RLE_unpacked)

str_unpacked = ''

for element in RLE_unpacked:
    str_unpacked += element[1] * element[0]
print(str_unpacked)

with open('PythonHW5/Unpacked_result.txt', 'w', encoding = 'UTF-8') as my_file:
    my_file.write(str_unpacked)
