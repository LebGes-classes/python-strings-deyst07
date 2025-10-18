text = input('Введите текст на английском: ')
lower_alpha = 'abcdefghijklmnopqrstuvwxyz'
upper_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabets = lower_alpha + upper_alpha
code = ''
words = []
K = 0
k = 0

word = ''
for i in range(len(text)):
    if text[i] in alphabets:
        word += text[i]
        k += 1
    else:
        if word:
            words.append(word)
            if k > K:
                K = k
            k = 0
        word = ''

if word:
    words.append(word)
    if k > K:
        K = k

for char in text:
    if char in lower_alpha:
        pos = (lower_alpha.index(char) + K) % 26
        code += lower_alpha[pos]
    elif char in upper_alpha:
        pos = (upper_alpha.index(char) + K) % 26
        code += upper_alpha[pos]
    else:
        code += char

print(f"Зашифрованный текст (сдвиг на {K} позиций): {code}")