# Напишите программу, удаляющую из текста все слова, содержащие "абв".

my_str = 'Проыдабв ыЫджвы, пДДовабв, лщцыАБВ ывуцы, длаб 456. Щопам абвдызоп аБвзщшавблл фЛЦо АБВбв.'
print(my_str)


#-----------------убираем из текста слова с 'абв', стоящие без знаков препинания------------------------

new_str_list = list(filter(lambda el: not ('абв' in el.lower() and el.lower().isalpha()), my_str.split()))
print(' '.join(new_str_list))

#-----------------убираем из текста слова с 'абв', стоящие со знаками препинания------------------------

upd_str_list = []

for el in new_str_list:
    if 'абв' in el.lower() and not el.lower().isalpha():
        temp_list = list(el.lower())
        i = 0
        count = 0
        count_num = len(temp_list)
        while(count < count_num):
            if temp_list[i].isalpha():
                temp_list.remove(temp_list[i])
            else:
                i += 1
            count += 1
        upd_str_list.append(''.join(temp_list))
    else:
        upd_str_list.append(el)

upd_str = ' '.join(upd_str_list)
print(upd_str)