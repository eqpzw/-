class Graph:

    def __init__(self, n):
        self.n = n  # Количество вершин
        self.adj_matrix = []  # Матрица смежности
        self.visited = []  # Массив посещенных вершин
        self.component = []  # Компонента связности

    def read_adjacency_matrix(self):
        """Ввод матрицы смежности"""
        print(f"Введите матрицу смежности {self.n}x{self.n} (0 и 1 через пробел):")
        for i in range(self.n):
            while True:
                try:
                    row = list(map(int, input().split()))
                    if len(row) != self.n:
                        print(f"Ошибка! Нужно ввести ровно {self.n} чисел.")
                        continue
                    if any(x not in (0, 1) for x in row):
                        print("Ошибка! Все числа должны быть 0 или 1.")
                        continue
                    self.adj_matrix.append(row)
                    break
                except ValueError:
                    print("Ошибка! Введите целые числа (0 или 1).")

    def is_symmetric(self):
        """Проверяет, является ли граф неориентированным (матрица симметрична)"""
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if self.adj_matrix[i][j] != self.adj_matrix[j][i]:
                    return False
        return True

    def bfs(self, start_vertex):
        """Поиск в ширину для нахождения компоненты связности"""
        # Инициализация
        self.visited = [False] * self.n
        self.component = []

        # Очередь для BFS
        queue = []

        # Начинаем с стартовой вершины
        queue.append(start_vertex)
        self.visited[start_vertex] = True

        while queue:
            v = queue.pop(0)  # Извлекаем первый элемент
            self.component.append(v + 1)  # Сохраняем вершину (индексация с 1)

            # Проверяем всех соседей
            for u in range(self.n):
                if self.adj_matrix[v][u] == 1 and not self.visited[u]:
                    queue.append(u)
                    self.visited[u] = True

    def print_component_info(self):
        """Выводит информацию о компоненте связности"""
        print("\nРезультат:")
        print(f"Количество вершин в компоненте связности: {len(self.component)}")
        print("Сами вершины:", *sorted(self.component))


def read_int(prompt, min_val=None, max_val=None):
    """Функция для безопасного ввода целых чисел"""
    while True:
        try:
            x = int(input(prompt))
            if min_val is not None and x < min_val:
                print(f"Число должно быть не меньше {min_val}!")
                continue
            if max_val is not None and x > max_val:
                print(f"Число должно быть не больше {max_val}!")
                continue
            return x
        except ValueError:
            print("Ошибка ввода! Введите целое число.")


def main():
    """Основная функция"""
    # Ввод количества вершин и стартовой вершины
    n = read_int("Введите количество вершин графа (1<=n<=100): ", 1, 100)
    start_vertex = read_int(f"Введите стартовую вершину (1<=s<={n}): ", 1, n) - 1

    # Создаем граф
    graph = Graph(n)

    # Ввод матрицы смежности
    graph.read_adjacency_matrix()

    # Проверка на симметричность
    if graph.is_symmetric():
        print("Граф является неориентированным (матрица симметрична)")
    else:
        print("Граф является ориентированным (матрица не симметрична)")

    # Выполняем поиск в ширину
    graph.bfs(start_vertex)

    # Выводим результат
    graph.print_component_info()


if __name__ == "__main__":
    main()
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

