from math import sqrt  # Импорт функции для нахождения корня


def createPoints():
    """Функция для создания массива точек (x, y)"""
    mass = []
    while True:
        # Проверка исключений для корректной работы цикла заполнения
        try:
            x, y = map(int, input().split())  # Ввод значений для кортежа через map
        except ValueError:
            return mass
        else:
            mass.append((int(x), int(y)))


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

print("\nДля начала введите значения точек\nКак только закончите вводить значения, напишите в консоле end")
print("Пример ввода координат:\n5 1")

sortInfo(bubble_sort(createPoints()))