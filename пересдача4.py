
# Функция для безопасного чтения числа
def read_int(prompt, min_val=None, max_val=None):
    while True:
        try:
            x = int(input(prompt))
            if (min_val is not None and x < min_val) or (max_val is not None and x > max_val):
                print(f"Введите число от {min_val} до {max_val}!")
                continue
            return x
        except ValueError:
            print("Ошибка ввода! Введите целое число.")


# Ввод количества вершин и стартовой вершины
N = read_int("Введите количество вершин графа (1<=n<=100): ", 1, 100)
S = read_int(f"Введите стартовую вершину (1<=s<={N}): ", 1, N) - 1

# Ввод матрицы смежности
print(f"Введите матрицу смежности {N}x{N} (0 и 1 через пробел):")
graph = []
for i in range(N):
    while True:
        try:
            row = list(map(int, input().split()))
            if len(row) != N or any(x not in (0, 1) for x in row):
                raise ValueError
            graph.append(row)
            break
        except ValueError:
            print(f"Ошибка! Введите ровно {N} чисел (0 или 1).")


# Массив для отметки посещённых вершин
visited = [False] * N

# Очередь
queue = []

# Список вершин в компоненте
component = []

queue.append(S)       # добавляем стартовую вершину
visited[S] = True     # помечаем её как посещённую

while len(queue) > 0:# пока очередь не пуста
    v = queue.pop(0)# достаём первый элемент из очереди
    component.append(v + 1)# сохраняем вершину (возвращаем индексацию с 1)

    # идём по всем соседям вершины
    for u in range(N):
        if graph[v][u] == 1 and not visited[u]:
            queue.append(u)# кладём соседа в очередь
            visited[u] = True# отмечаем посещённым


print("\nРезультат:")
print(f"Количество вершин в компоненте связности: {len(component)}")
print("Сами вершины:", *component)

#1нечисловой ввод
#Введите стартовую вершину (1<=s<=2): первая
#Ошибка ввода! Введите целое число.

#2количество вершин
#Введите количество вершин графа (1<=n<=100): 2
#Введите стартовую вершину (1<=s<=2): 5
#Введите число от 1 до 2!

#3ввод
#Введите матрицу смежности 3x3 (0 и 1 через пробел):
#0 0 0
#0 0 0\
#Ошибка! Введите ровно 3 чисел (0 или 1).

