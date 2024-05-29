my_string = input('Введите произвольную строку: ')
print('Длина введенного текста', len(my_string))
print('Строка в верхнем регистре:', my_string.upper(), '\nСтрока в нижнем регистре:',
      my_string.lower(), '\nСтрока без пробелов:', my_string.replace(' ', ''),
      '\nПервый символ строки:', my_string[0], '\nПоследний символ строки:', my_string[-1])

