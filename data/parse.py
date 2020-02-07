import json

with open("dialog.json",'a') as fj:
    dialogue = {}
    with open('txt/dialog.txt') as f:
        k = 0
        first = []
        sec = []

        for i in f.readlines():
            if i == "\n":
                continue
            if "-" in i:
                k += 1
            if k % 2 == 1:
                first.append(i[1:len(i)-1])
            elif k % 2 == 0:
                sec.append(i[1:len(i)-1])
            print(i)
        # for i in range(len(first)):
        #     first.insert(i,first[i].split('.'))
    dialogue["first"] = first
    dialogue["second"] = sec
    print(first)
    print(sec)
#     json.dump(dialogue, fj, ensure_ascii=False)
    
# with open("dialog.json", 'r', encoding="utf-8") as fl:
#     nums_new = json.load(fl)
#     print(nums_new)