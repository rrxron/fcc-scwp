with open('tongue-twister.txt') as f:
    counts = dict()

    for line in f:
        for word in line.split():
            counts[word] = counts.get(word, 0) + 1
    lst = list()

    for key, val in counts.items():
        lst.append((val,key))
    lst = sorted(lst, reverse=True)

    for val,key in lst[:10]:
        print(key, val)
