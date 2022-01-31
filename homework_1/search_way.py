from math import sqrt  # Импорт функции для нахождения корня


def createPoints():
    """Функция для создания массива"""
    mass = [(0, 2), (2, 5), (5, 2), (6, 6), (8, 3)]
    return mass


def formulaDistant(point1, point2):
    """Функция нахождения расстояния между точками"""
    return sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)


def bubble_sort(arr):
    """Функция сортировки пузырьком"""
    def swap(i, j):
        """Функция свапа для двух элементов в массиве"""
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    swapped = True

    x = -1  # Значения для порядкового уменьшения количества проходов через массив
    while swapped:
        swapped = False
        x = x + 1
        for i in range(2, n - x):
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True

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


sortInfo(bubble_sort(createPoints()))
