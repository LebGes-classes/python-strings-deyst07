text = input('Введите текст на английском: ')

lower_alpha = 'abcdefghijklmnopqrstuvwxyz'
upper_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabets = lower_alpha + upper_alpha
code = ''
words = []
K = 0

text2_parts = []
count = 0 

for ch in text:
    if ch in alphabets:
        text2_parts.append(ch)
        count += 1
        if count == 20:
            text2_parts.append(' ')
            count = 0
    else:
        text2_parts.append(ch)
        count = 0

text2 = ''.join(text2_parts)

word = ''

for ch in text2:
    if ch in alphabets:
        word += ch
    else:
        if word:
            words.append(word)
            if len(word) > K:
                K = len(word)
            word = ''

if word:
    words.append(word)
    if len(word) > K:
        K = len(word)

for char in text2:
    if char in lower_alpha:
        pos = (lower_alpha.index(char) + K) % 26
        code += lower_alpha[pos]
    elif char in upper_alpha:
        pos = (upper_alpha.index(char) + K) % 26
        code += upper_alpha[pos]
    else:
        code += char

print(f"Зашифрованный текст (сдвиг на {K} позиций): {code}")