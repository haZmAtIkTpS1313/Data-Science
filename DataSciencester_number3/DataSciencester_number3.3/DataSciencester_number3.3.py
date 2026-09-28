# Словарь или ассоциативный список - это еще одна фундаментальная структура данных
# В нем значения ассоциированы с ключами, что позволяет быстро извлекать значения соответствующее конкретному ключу

empty_dict = {}                     #Первый способ
empty_dict2 = dict()                #Второй способ
grades = {"Joel": 80, "Tim": 95}    #Третий способ

# Жоступ к значению по ключу можно получить при помощи квадратных скобок
joels_grade = grades["Joel"]    # равно 80

# При попытке запросить значения, которое в словаре отсуствует, будет выдано сообщения об ошибке ключа KeyError:
try:
    kates_grade = grades["Kate"]
except KeyError:
    print("Оценка для Кэйт отсуствуют!")

# Проверить наличие ключа можно при помощи оператора in

joel_has_grade = "Joel" in grades      # True
kate_has_grade = "Kate" in grades      # False

# Словари имеют метод get, который при поиске отсутствующего ключа вместо
# вызова исключения возвращает значения по умолчанию

joels_grde = grades.get("Joel", 0)     # равно 80
kates_grade = grades.get("Kate", 0)    # равно 0
no_ones_grade = grades.get("Никто")   # Значения по умолчанию равно None

# Присваивание значения по ключу выполняется при помощи тех же квадратных скобок

grades["Tim"] = 99             # Заменяет старое значение
grades["Kate"] = 100           #Добавляем третью запись
num_students = len(grades)     # равно 3


# Словари часто используются в качестве простого способа представить структурные данные
tweet = {
    "user": "joelgrus",
    "text": "Наука о данных - потрясающая тема",
    "retweet_count": 100,
    "hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}

tweet_keys = tweet.keys()               # Итерируемый объект для ключей
tweet_values = tweet.values()           # Итерируемый объект для значений
tweet_items = tweet.items()             # Итерируемый объект для кортежей
                                        # (ключ, значение)
"user" in tweet_keys                    # ВОзвращает True  но не по-Python'овски
"user" in tweet                         # Python'овский способ проверки ключа
                                        # Используя быстрое in 
"joelgrus" in tweet_values              # True (медленно, но единственный способ проверки)



# Словарь defaultdict 

# Частотности слов
word_counts = {}
document = {}
for word in document:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# Кроме этого можно воспользоваться приемом под названием лучше просить прощения, чем разрешения
# и перехватывать ошибку при попытке обратиться к отсутствующему ключу

word_count = {}
for word in document:
    try:
        word_count[word] +=1
    except KeyError:
        word_count[word] = 1

# Третий подход - использовать метод get, который изящно выходит из ситуации с отсуствующими ключами

words_counts = {}
for word in document:
    previous_count = words_counts.get(word, 0)
    words_counts[word] = previous_count + 1


# Все перечисленные приемы немного громоздкие, и по этой причине целеобразно использовать словарь defaultdict, т.е. словарь со значением по умолчанию

from collections import defaultdict

wordis_count = defaultdict(int)             # int() возвращает 0
for word in document:
    wordis_count[word] += 1


# Кроме того, использование словарей defaultdict имеет практическую пользу во время работы со списками
# словарями и даже со собственными функциями

dd_list = defaultdict(list)                       # list() возвращает пустой список
dd_list[2].append(1)                              # Теперь dd_list содержит {2: [1]}

dd_dict = defaultdict(dict)                       # dict() возвращает пустой словарь dict()
dd_dict["Joel"]["City"] = "Cietl"                 # { "Joel" : { "City" : "Cietl" } }

dd_pair = defaultdict(lambda: [0, 0])
dd_pair[2][1] = 1                                 # Теперь dd_pair содержит { 2: [0, 1] }


# Счётчики

# Словарь-счетчика Counter трансформирует последовательность значения в объект, походий на словарь defaultdict(int)
# где ключам поставлены в соотвествие количества появлений. Он в основном будет применяться при создании гистрограмм

from collections import Counter

c = Counter([0, 1, 2, 0]) # В результает с равно { 0 : 2, 1 : 1, 2 : 1}

# Его функционал позволяет достаточно легко решать задачу подсчета количества появлений слов

#  Лучши1 вариант подсчета количества появлений слов 
word_countss = Counter(document)

# Словарь Counter распологается методом most_common, который нередко бывает полезен 
# Напечатать 1- наиболее встречаемых слов и их количество появлений
for word, count in word_countss.most_common(10):
    print(word,count)


# Множества 
# Еще одна полезная структура данных - это множество set,
# которая представляет собой совокупность неупорядоченных элементов без повторов

s = set()          # Задать пустое множество
s.add(1)           # Теперь s равно ( 1 )
s.add(2)           # Теперь s равно ( 2 )
s.add(2)           # s как и прежде равно ( 1, 2 )
x = len(s)         # равно 2
y = 2 in s         # равно True
z = 3 in s         # равно False


# Список стоп-слов
stopwords_list = ["a", "an", "at"] + hundreds_of_other_words + ["yet", "you"]
"zip" in stopwords_list    # False, но проверяется каждый элемент

# Множество стоп-кадров
stopwords_set = set(stopwords_list)
"zip" in stopwords_set     # False, но очень быстро

# Вторая причина - получение уникальных элементов в наборе данных

item_list = [1, 2, 3, 1, 2, 3]            # Список
num_items = len(item_list)                # равно 6
item_set = set(item_list)                 # Множество (1, 2, 3)
num_distinct_items = len(item_set)        # равно 3
distinct_item_list = list(item_list)      # Список [1, 2, 3]

# Множества будут применяться намного реже словарей и списков
