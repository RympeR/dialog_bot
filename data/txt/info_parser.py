from json import load, dump
import os

# os.chdir('txt')
phrases = list()
res = {'Я': list(), 'Люблю': list(), 'Увлечения': list(), 'Другое': list()}
os.chdir('txt')
print(os.getcwd())
with open("profiles.txt", 'r', encoding='utf-8') as f:
    for i in f.readlines():
        phrases.append(i.split('    '))
    for i in range(len(phrases)):
        if '\t' in str(phrases[i][0]):
            phrases[i][0] = str(phrases[i]).replace(r'\t', '')
        phrases[i][0] = phrases[i][0].split('.')
        # phrases[i][0] = str(phrases[i][0])[2:-2]
        for k in phrases[i][0]:
            if k.endswith(r"\n']"):
                continue

            if k.startswith("['") and k.count(' ') > 4:
                k = k[2:]

            elif k.startswith("['"):
                k = k[2:]
            print(k)
            # print(k[0])
            if 'Люблю' or 'люблю'in k:
                res['Люблю'].append(k)
            elif 'Я' == k[0]:
                res['Я'].append(k)
                print('here')
            elif 'обожаю' or 'увлекаюсь' or 'Увлекаюсь' or 'Обожаю' in k:
                res['Увлечения'].append(k)
            else:
                res['Другое'].append(k)

print(res['Я'])
