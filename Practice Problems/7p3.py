words = ["cat", "dog", "cat", "bird", "dog", "cat"]
count = {}

for word in words:
    if word in count:
        count[word] +=1
    else:
        count[word] = 1
print(count)