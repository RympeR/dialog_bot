import json
from urllib import request, parse

nums = [1, 2, 3, 4, 5, 3, 5, 3, 2]

file_name = "nums.json"

with open(file_name, 'w') as f:
    # json.dump(nums, f, encure_ascii=False)
    json.dump(nums, f, ensure_ascii=False)
with open(file_name, 'r', encoding="utf-8") as fl:
    nums_new = json.load(fl)

print(nums_new[0])

search = "pizza"
myUrl = "https://www.google.com/search?"
value = {'q': 'pizza'}

myheader = {}
myheader["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.92 Safari/537.36 Viv/2.9.1705.38"

# try:
#     mydata = parse.urlencode(value)
#     print(mydata)
#     myUrl += mydata
#     req = request.Request(myUrl, headers=myheader)
#     answer = request.urlopen(req)
#     answer = answer.readlines()
#     for line in answer:
#         print(line)
# except Exception as identifier:
#     print(identifier)


class Manage:
    def __init__(self, name):
        self.name = name
    
    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


