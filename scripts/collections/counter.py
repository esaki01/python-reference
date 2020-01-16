import collections

l = ['a', 'a', 'a', 'b', 'b', 'c']
c = collections.Counter()
for word in l:
    c[word] += 1
print(c)
print(c.most_common(1))
print(sum(c.values()))
