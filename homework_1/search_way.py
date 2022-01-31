from math import sqrt  # Импорт функции для нахождения корня


def createPoints():
    """Функция для создания массива"""
    mass = [(0, 2), (2, 5), (5, 2), (6, 6), (8, 3)]
    return mass


def formulaDistant(point1, point2):
    """Функция нахождения расстояния между точками"""
    return sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)


def sortArr(arr):
    """Функция сортировки массива по значению расстояния между точками (от min до max)"""
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr) - 2):
            if formulaDistant(arr[i], arr[i + 1]) > formulaDistant(arr[i], arr[i + 2]):
                arr[i + 1], arr[i + 2] = arr[i + 2], arr[i + 1]

    return arr


def sortInfo(arr):
    """Функция вывода информации по построению маршрута"""
    countDistant = 0  # Дистанция всего пути
    for i in range(len(arr) - 1):
        countDistant += formulaDistant(arr[i], arr[i + 1])
        print(str(arr[i]) + " -> " + str(arr[i + 1]) + "[" + str(countDistant) + "]", end=' ')
    countDistant += formulaDistant(arr[-1], arr[0])
    print(" -> " + str(arr[0]) + "[" + str(countDistant) + "]" + " = " + str(countDistant))


print('\tДобро пожаловать в программу "Вычисления кратчайшего пути для почтальона"')
print("-" * 81)

sortInfo(sortArr(createPoints()))
