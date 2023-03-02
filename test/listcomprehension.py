with open('tongue-twister.txt') as f:
    counts = dict()

    for line in f:
        for word in line.split():
            counts[word] = counts.get(word, 0) + 1

    lst = list()

    # list comprehension
    lst = sorted([(v,k) for k,v in counts.items()], reverse=True)

    for val,key in lst[:10]:
        print(key, val)