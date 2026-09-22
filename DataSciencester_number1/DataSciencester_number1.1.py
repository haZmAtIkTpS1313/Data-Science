users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"}
]
#Значения 0 - id, говорит о том кто с кем находиться в дружеских отношениях
#Hero - Dunn
#Hero - Sue
#Dunn - Sue
#Dunn - Chi
#Sue - Chi
#Chi - Thor 
#Thor - Clive
#live - Hicks
#Clive - Devin 
#Hicks - Kate 
#Devin - Kate 
#Kate - Klein
friendship_pairs = [(0,1), (0,2), (1,2), (1,3), (2,3), (3,4),
                     (4,5), (5,6), (5,7), (6,8), (7,8), (8,9)]

#Инициализировать словарь пустым списком для идентификатора
#каждого пользователя 
friendships = {user["id"] : [] for user in users}

#и перебрать все дружеские пары, заполняя их 
for i in friendships:
    for j in friendships:
        friendships[i].append(j) # Добавить j как друга для i
        friendships[j].append(i) # Добавить i как друга для j


#Число друзей 
def number_of_friends(user):
    """" Сколько друзей есть у пользователя user ?"""
    user_id = user["id"]
    friends_ids = friendships[user_id]
    return len(friends_ids)
total_connections = sum(number_of_friends(user)   #Суммарное число
                        for user in users)        #связей - 24

num_users = len(users)
avg_connections = total_connections / num_users # 24 / 10 = 2.4


# Создать список в формате (id пользователя, число друзей)
num_friends_by_id = [(user["id"], number_of_friends(user)) 
                    for user in users]

num_friends_by_id.sort(                             #Отсортировать список по полю
    key = lambda id_and_friends: id_and_friends[1], #num_friends
    reverse=True)                                   #в убывающем порядке

#Какая пара представлена кортежем (user_id, num_friends),
#т.е. идентификатором пользователя и числом друзей 
#  [(1, 3), (2, 3), (3, 3), (5, 3), (8, 3), 
#   (0, 2), (4, 2), (6, 2), (7, 2), (9, 1)]

# Список айди друзей пользователя user (плохой вариант)
def foaf_id_bad(user):
    # float означает товарищ товарища 
    return [float_id 
            for friend_id in friendships[user["id"]]
            for foaf_id in friendships[friend_id]]
print (friendships[0])
print (friendships[1])
print (friendships[2])


from collections import Counter

def friends_of_friends(user):
    user_id = user["id"]
    return Counter(
        foaf_id
        for friend_id in friendships[user_id]    # По каждому моему другу
        for foaf_id in friendships[friend_id]    # отыскать его друзей
        if foaf_id != user_id                    # которые не являются мной
        and foaf_id not in friendships[user_id]  # и не являются моими друзьями 
    )

print(friends_of_friends(users[3]))              # Counter ({0:2,5:1})


interests = [
    (0, "Hadoop") , (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "spicy"),
    (2, "numpy") , (2, "statsmodels"), (2, "pandas"),
    (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programm languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mathout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artifical intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
] 

# Исследователи данных, которым нравится целевая тема target_intereset
def data_scientists_who_like(target_intereset):
    """Отыскать идентификаторы всех пользователей,
    которым интересна целевая тема."""
    return [user_id
            for user_id, user_intereset in interests
            if user_intereset == target_intereset]



from collections import defaultdict

#Идентификаторы пользователей по идентификатору темы
#Ключи - это интересующие темы, 
#Значение - списки тем для конкретного идентификатора 
user_ids_by_interest = defaultdict(list)

for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)

#interests_by_user_id = defaultdict(list)
#for user_id, interest in interests:
#    interests_by_user_id[user_id].append(interset)

#Наиболее общие интересы с пользователем user
def most_common_interests_with(user):
    return Counter(
        interestes_user_id
        for interest in interests_by_user_id[user["id"]]
        for interested_user_id in user_id_by_interest[interest]
        if interested_user_id != user["id"]
    )


# Зарплаты и стаж
salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                        (48000, 0.7), (76000, 6),
                        (69000, 6.5), (76000, 7.5),
                        (60000, 2.5), (83000, 10),
                        (48000, 1.9), (63000, 4.2)]
#Стажная группа
def tenure_bucket(tenure):
    if tenure < 2:
        return "менее двух"
    elif tenure < 5:
        return "между двумя и пятью"
    else:
        return "более пяти"    
#Зарплата в зависимости от стажной группы
#Ключи - это стажные группы, значения - списки зарплат в этой группе.
# Словарь содержит списки зарплат, соответствующие каждой стажной группе

salary_by_tenure_bucket = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)

#Средняя зарплата по группе
#Ключи - это стажные группыб значения - средняя зарплата по этой группе
average_salary_by_bucket = {
    tenure_bucket : sum(salaries) / len(salaries)
    for tenure_bucket in salary_by_tenure_bucket.iteritems()
    for salaries in salary_by_tenure_bucket.iteritems()
}

#Предсказать оплату, исходя из стажа 
def predict_paid_or_unpaid(years_experience):
    if years_experience < 3.0:
        return "Оплачено"
    elif years_experience < 8.5:
        return "Не оплачено"
    else: 
        return "Оплачено"

#Слова и количества появлений 
words_and_counts = Counter(word
                           for user, interest in interests
                           for word in interest.lower().split())
for word, count , in words_and_counts.most_common():
    if count > 1:
        print(word, count)
