import random

text = input("한글을 입력하세요.")
text2 = list(text)
len_text = len(text)
rule = 0

for i in range(0, len_text):
    rule = (ord(text2[i])-44032) % 28
    if rule == 0:
        text2[i] = chr(ord(text2[i]) + random.randint(-rule, 27 - rule))
    else:
        text2[i] = text2[i]
print(text2)