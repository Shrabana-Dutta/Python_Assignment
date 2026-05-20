file = open("Assignment 3/Asgn-3-Debajyoti-0011/supervised.txt", "r", encoding="utf-8")
text = file.read()

text = text.lower()

for ch in ",.!?:;()[]{}\"'":
    text = text.replace(ch, "")

words = text.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

file.close()

print(word_count)
