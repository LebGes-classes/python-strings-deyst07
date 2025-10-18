text = input('Напишите что-нибудь, и я это отзеркалю: ')
zerkalo = ''

for i in range(len(text) - 1, -1, -1):
    zerkalo += text[i]

print(zerkalo)