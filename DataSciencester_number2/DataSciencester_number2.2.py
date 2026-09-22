#МОДУЛИ

import re
my_regex = re.compile("[0-9]+", re.I)

#Здесь re - это название модуля, содержащего функции и константы для работы с регулярными выражениями

import re as regex
my_regex_two = regex.compile("[0-9]+", regex.I)

# Если из модуля необходимо получить несколько конкретных значений,
# то их можно импортировать в явном виде и использовать без ограничений 
from collections import defaultdict, Counter
lookup = defaultdict(int)
my_counter = Counter()

#Если объявить переменные и импортировать всю библиотеку
#то можно перезаписать все уже объявленные переменные(так нельзя)

match = 10         
from re import *   #Оппа в модуле re есть функия match
print(match)       #"<function re.match>"

