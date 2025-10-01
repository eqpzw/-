# Класс для узла очереди - каждый элемент очереди
class Node:
    def __init__(self, value):
        self.value = value  # Значение узла
        self.next = None  # Ссылка на следующий узел

# Класс для очереди
class Queue:
    def __init__(self):
        self.head = None  # Первый элемент очереди
        self.tail = None  # Последний элемент очереди

    # Добавление элемента в конец очереди
    def add(self, value):
        new_node = Node(value)  # Создаем новый узел
        if not self.head:  # Если очередь пустая
            self.head = new_node  # Новый узел становится головой
            self.tail = new_node  # И хвостом одновременно
        else:
            self.tail.next = new_node  # Привязываем новый узел к концу
            self.tail = new_node  # Обновляем хвост

    # Удаление первых K элементов
    def remove_first_k(self, k):
        if not self.head:  # Проверка на пустую очередь
            raise ValueError("Очередь пуста")

        if k <= 0:  # Проверка корректности K
            raise ValueError("K должно быть положительным числом")

        removed_elements = []  # Список для удаленных элементов
        current = self.head  # Начинаем с головы
        count = 0

        # Проходим по первым K элементам
        while current and count < k:
            removed_elements.append(current.value)  # Добавляем значение в список
            current = current.next  # Переходим к следующему
            count += 1

        # Обновляем голову очереди
        self.head = current
        # Если очередь стала пустой, обнуляем хвост
        if not self.head:
            self.tail = None

        return removed_elements  # Возвращаем удаленные элементы

    # Вычисление суммы первых K элементов
    def sum_first_k(self, k):
        if not self.head:  # Если очередь пуста
            return 0

        if k <= 0:  # Если K некорректно
            return 0

        total = 0  # Сумма
        current = self.head  # Начинаем с головы
        count = 0

        # Суммируем первые K элементов
        while current and count < k:
            total += current.value  # Добавляем значение к сумме
            current = current.next  # Переходим к следующему
            count += 1

        return total  # Возвращаем сумму

    # Получение первого элемента очереди
    def get_first_element(self):
        if self.head:  # Если очередь не пуста
            return self.head, self.head.value  # Возвращаем узел и значение
        return None, None  # Иначе возвращаем None

    # Вывод всех элементов очереди
    def display(self):
        elements = []  # Список для элементов
        current = self.head  # Начинаем с головы

        # Проходим по всей очереди
        while current:
            elements.append(current.value)  # Добавляем значение
            current = current.next  # Переходим к следующему

        return elements  # Возвращаем список элементов


# Класс-итератор для обхода очереди
class QueueIterator:
    def __init__(self, queue):
        self.queue = queue  # Очередь для обхода
        self.forward_mode = True  # Режим обхода: True - прямой, False - обратный
        self.current = queue.head  # Текущий узел для прямого обхода
        self.reverse_elements = []  # Список для обратного обхода
        self.reverse_index = -1  # Индекс для обратного обхода

    def __iter__(self):
        return self  # Возвращаем сам итератор

    def __next__(self):
        # Прямой обход
        if self.forward_mode:
            if self.current is None:  # Если дошли до конца
                self.forward_mode = False  # Переключаем на обратный обход
                self._prepare_reverse()  # Подготавливаем данные
                if not self.reverse_elements:  # Если нет элементов
                    raise StopIteration  # Завершаем итерацию
                # Настраиваем обратный обход
                self.reverse_index = len(self.reverse_elements) - 1
                return self._get_next_reverse()  # Первый элемент обратного обхода

            value = self.current.value  # Получаем значение
            self.current = self.current.next  # Переходим к следующему
            return value  # Возвращаем значение

        # Обратный обход
        else:
            return self._get_next_reverse()

    # Подготовка данных для обратного обхода
    def _prepare_reverse(self):
        self.reverse_elements = []  # Очищаем список
        current = self.queue.head  # Начинаем с головы

        # Собираем все элементы в список
        while current:
            self.reverse_elements.append(current.value)
            current = current.next

    # Получение следующего элемента при обратном обходе
    def _get_next_reverse(self):
        if self.reverse_index < 0:  # Если дошли до начала
            raise StopIteration  # Завершаем итерацию

        value = self.reverse_elements[self.reverse_index]  # Берем элемент с конца
        self.reverse_index -= 1  # Двигаемся к началу
        return value  # Возвращаем значение


# Функция сохранения данных в двоичный файл
def save_to_binary_file(data, filename):
    try:
        # Открываем файл для записи в двоичном режиме
        with open(filename, 'wb') as f:
            # Сохраняем удаленные элементы
            f.write(f"Удаленные элементы: {data['removed_elements']}\n".encode('utf-8'))
            # Сохраняем сумму
            f.write(f"Сумма первых K элементов: {data['sum_first_k']}\n".encode('utf-8'))
            # Сохраняем новый первый элемент
            f.write(f"Новый первый элемент: {data['new_first_value']}\n".encode('utf-8'))
            # Сохраняем адрес нового первого элемента
            f.write(f"Адрес нового первого элемента: {data['new_first_node_address']}\n".encode('utf-8'))
            # Сохраняем очередь после удаления
            f.write(f"Очередь после удаления: {data['queue_after_removal']}\n".encode('utf-8'))
            # Сохраняем K
            f.write(f"K: {data['K']}\n".encode('utf-8'))
        return True
    except Exception as e:
        print(f"Ошибка при сохранении файла: {e}")
        return False


# Функция чтения данных из двоичного файла
def read_from_binary_file(filename):
    try:
        # Открываем файл для чтения в двоичном режиме
        with open(filename, 'rb') as f:
            content = f.read()  # Читаем все содержимое
            decoded_content = content.decode('utf-8')  # Декодируем из байтов в строку
            print("Содержимое файла:")
            print(decoded_content)
        return True
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return False


# Функция ввода очереди с клавиатуры
def input_queue():
    queue = Queue()  # Создаем новую очередь
    print("Вводите целые числа для добавления в очередь.")
    print("Для завершения ввода введите 'stop'")

    count = 0
    while True:
        # Запрос ввода от пользователя
        user_input = input(f"Введите число #{count + 1} (или 'stop' для завершения): ").strip()

        # Проверка на команду остановки
        if user_input.lower() == 'stop':
            if count == 0:  # Если не введено ни одного числа
                print("Вы не ввели ни одного числа!")
                continue
            break

        try:
            number = int(user_input)  # Пробуем преобразовать в число
            queue.add(number)  # Добавляем в очередь
            count += 1  # Увеличиваем счетчик
            print(f"Добавлено: {number}")
            print(f"Текущая очередь: {queue.display()}")
        except ValueError:
            print("Ошибка! Введите целое число или 'stop' для завершения.")

    return queue  # Возвращаем заполненную очередь


# Функция ввода числа K
def input_k():
    while True:
        try:
            # Запрос ввода K
            k = int(input("\nВведите число K (сколько элементов удалить): "))
            if k <= 0:  # Проверка на положительное число
                print("K должно быть положительным числом!")
                continue
            return k  # Возвращаем корректное K
        except ValueError:
            print("Ошибка! Введите целое число.")


# Основная функция программы
def main():

    # Ввод очереди с клавиатуры
    queue = input_queue()

    # Проверка что очередь не пуста
    if not queue.head:
        print("Очередь пуста! Программа завершена.")
        return

    print(f"\nИтоговая очередь: {queue.display()}")

    # Ввод числа K
    K = input_k()

    # Сохраняем исходную очередь для вычисления суммы
    original_queue_elements = queue.display()  # Получаем все элементы
    temp_queue = Queue()  # Создаем временную очередь
    # Копируем элементы во временную очередь
    for element in original_queue_elements:
        temp_queue.add(element)
    print(f"Исходная очередь: {queue.display()}")
    print(f"K = {K}")

    # Удаляем первые K элементов
    try:
        removed_elements = queue.remove_first_k(K)
        print(f"Удаленные элементы: {removed_elements}")
    except ValueError as e:
        print(f"Ошибка при удалении: {e}")
        return

    # Вычисляем сумму первых K элементов (из исходной очереди)
    sum_k = temp_queue.sum_first_k(K)
    print(f"Сумма первых {K} элементов: {sum_k}")

    # Получаем новый первый элемент
    new_first_node, new_first_value = queue.get_first_element()
    if new_first_node:
        print(f"Новый первый элемент: {new_first_value}")
        # Получаем адрес объекта в памяти
        new_first_address = hex(id(new_first_node))
        print(f"Адрес нового первого элемента: {new_first_address}")
    else:
        print("Очередь стала пустой после удаления")
        new_first_address = None

    print(f"Очередь после удаления: {queue.display()}")

    # Подготавливаем данные для сохранения
    data_to_save = {
        'removed_elements': removed_elements,  # Удаленные элементы
        'sum_first_k': sum_k,  # Сумма
        'new_first_value': new_first_value,  # Новый первый элемент
        'new_first_node_address': new_first_address,  # Адрес
        'queue_after_removal': queue.display(),  # Очередь после удаления
        'K': K  # Число K
    }

    # Сохраняем данные в файл
    if save_to_binary_file(data_to_save, 'rez.dat'):
        print(f"\n✓ Все данные успешно сохранены в файл 'rez.dat'")
    else:
        print(f"\n✗ Ошибка при сохранении данных!")

        return

    # Создаем копию текущей очереди для демонстрации
    demo_queue = Queue()
    for element in queue.display():
        demo_queue.add(element)

    if demo_queue.head:  # Если очередь не пуста
        print("Обход очереди с помощью итератора:")

        # Создаем итератор
        iterator = QueueIterator(demo_queue)

        print("Прямой порядок: ", end="")
        # Прямой обход
        for item in iterator:
            print(item, end=" ")
        print()

        # Создаем новый итератор для обратного обхода
        iterator = QueueIterator(demo_queue)
        print("Обратный порядок: ", end="")
        try:
            # Пропускаем прямой порядок
            while True:
                next(iterator)
        except StopIteration:
            pass  # Прямой порядок завершен

        # Выводим обратный порядок
        try:
            while True:
                print(next(iterator), end=" ")
        except StopIteration:
            pass
        print()
    else:
        print("Очередь пуста, нечего выводить.")

    if read_from_binary_file('rez.dat'):
        print("Данные успешно загружены из файла")
    else:
        print("Ошибка при загрузке данных из файла")


# Запуск программы
if __name__ == "__main__":
    main()


#ечисловой ввод
#Вводите целые числа для добавления в очередь.
#Для завершения ввода введите 'stop'
#Введите число #1 (или 'stop' для завершения): три
#Ошибка! Введите целое число или 'stop' для завершения.
#Введите число #1 (или 'stop' для завершения):