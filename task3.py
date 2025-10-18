text = input('Введите текст: ')
lower_alpha = 'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
upper_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alphabets = lower_alpha + upper_alpha

# преобразуем в нижний регистр
lowertext = ''
for ch in text:
    if ch in lower_alpha:
        lowertext += ch
    elif ch in upper_alpha:
        pos = upper_alpha.index(ch)
        lowertext += lower_alpha[pos]
    else:
        lowertext += ch

# создаем список слов
words = []
word = ''
for i in range(len(lowertext)):
    if lowertext[i] in alphabets:
        word += lowertext[i]
    else:
        if word:
            words.append(word)
        word = ''

if word:
    words.append(word)

# создаем словарь и подсчитываем количество каждого слова
counter = {}
for word in words:
    if word in counter:
        counter[word] += 1
    else:
        counter[word] = 1

# создаем топ слов
items = list(counter.items())
n = len(items)
for i in range(n):
    max_idx = i
    for k in range(i + 1, n):
        if items[k][1] > items[max_idx][1]:
            max_idx = k
    items[i], items[max_idx] = items[max_idx], items[i]

for word, count in items:
    print(f"{word}: {count}")