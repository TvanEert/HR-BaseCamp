from ict_skills import skills1
import itertools

wishlist = {'Python','SQL','Java','Blockchain'}
names = []
n = 0
check = 0

for name in skills1.keys():
    names.append(name)
combinations = list(itertools.combinations(names, 3))
for combination in combinations:
    a, b, c = combinations[n]
    group = skills1[a] | skills1[b] | skills1[c]
    if all(x in group for x in wishlist):
        n+=1
        check += 1
    else:
        n+=1

for name in names:
    if not skills1[name] & wishlist:
        names.remove(name)
        print("removed ", name)
    
for name in names:
    print(skills1[name])

