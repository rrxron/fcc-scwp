# works when firewall is OFF
import urllib.request, urllib.parse, urllib.error

for line in urllib.request.urlopen("http://data.pr4e.org/romeo.txt"):
    print(line.decode().strip())

counts = dict()
for line in urllib.request.urlopen("http://data.pr4e.org/romeo.txt"):
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)