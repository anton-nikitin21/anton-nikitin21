# диаграма точечная 

# выбираем саму диаграмму - выбрать данные - добавить - пряму по двум точкам
# надо связать - изменить тип диаграмму для ряда - точечная зависимость с прямыми
# выделяем прямую - добавить линию тренда - линейная 


clustersA = [[], []]

for s in open('27A_18050.txt'):
    x, y = [float(i) for i in s.split()]
    if y < -2*x+4:
        clustersA[0].append([x, y])
    else:
        clustersA[1].append([x, y])

clustersB = [[], [], []]

for s in open('27B_18050.txt'):
    x, y = [float(i) for i in s.split()]
    if y> 1.6*x+0.4:
        clustersB[0].append([x, y])
    elif y<=2*x+20:
        clustersB[1].append([x, y])
    else:
        clustersB[2].append([x, y])

def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def center(kl):
    m = []
    for p in kl:
        sm = sum(dist(p, p1) for p1 in kl)
        m.append([sm, p])
    return min(m)[1]

centerA = [center(kl) for kl in clustersA]
centerB = [center(kl) for kl in clustersB]

PxA = sum(x for x, y in centerA) / 2 * 10000
PyA = sum(y for x, y in centerA) / 2 * 10000
print(int(PxA), int(PyA))

PxB = sum(x for x, y in centerB) / 3 * 10000
PyB = sum(y for x, y in centerB) / 3 * 10000
print(int(PxB), int(PyB))

# clasterA.sort(key=len)
#clasterA=clasterA[1:]