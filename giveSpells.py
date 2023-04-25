import random
for i in range(1,28):
    for spell in random.sample(range(1,43),5):
        print(str(i)+","+str(spell))
