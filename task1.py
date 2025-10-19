s = input("Введите строку: ")


words = []
word = ""

for ch in s:
    if ch != " ":
        word += ch
    else:
        if word != "":
            words.append(word)
            word = ""

if word != "":
    words.append(word)

reversed_words = ""

for i in range(len(words) - 1, -1, -1):
    reversed_words += words[i]
    if i != 0:
        reversed_words += " "

print("Зеркальный порядок слов:", reversed_words)

reversed_chars = ""

for i in range(len(s) - 1, -1, -1):
    reversed_chars += s[i]

print("Строка в обратном порядке символов:", reversed_chars)