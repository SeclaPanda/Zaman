n = int(input())
s = []
p = 0
o = 0
z = 0
for a in range(n):
    b = int(input())
    s.append(b)
for a in range(len(s)):
    if s[a] > 0:
        p += 1
    elif s[a] < 0:
        o += 1
    elif s[a] == 0:
        z += 1
pp = (p / n) * 100
po = (o / n) * 100
pz = (z / n) * 100
if pp > po and pp > pz:
    print(f'Положительных элементов - {pp}% и их больше всего')
elif po > pp and po > pz:
    print(f'Отрицательных элементов - {po}% и их больше всего')
elif pz > pp and pz > po:
    print(f'Нулевых элементов - {pz}% и их больше всего')