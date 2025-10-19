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

# собираем слова
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

# количество вхождений каждого слова
counter = {}

for word in words:
    if word in counter:
        counter[word] += 1
    else:
        counter[word] = 1

# сортировка
items = list(counter.items())
n = len(items)

for i in range(n):
    max_idx = i
    
    for k in range(i + 1, n):
        if items[k][1] > items[max_idx][1]:
            max_idx = k
    items[i], items[max_idx] = items[max_idx], items[i]

# --- 5. Вывод топ-5 ---
print("\nТоп-5 самых частых слов:\n")
for i in range(min(5, len(items))):
    word, count = items[i]
    print(f"{word}: {count}")