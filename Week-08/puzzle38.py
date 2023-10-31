from ict_skills import skills1

wishlist = {'Python','SQL','Java','Blockchain'}
names = []

for name in skills1.keys():
    print(name)
    names.append(name)

for name in names:
    if skills1[name] not in wishlist:
        names.remove(name)
        print("removed ", name)
    
for name in names:
    print(skills1[name])