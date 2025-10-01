class Quadrilateral:
    """
    Класс четырехугольник
    """

    def __init__(self, a, b, c, d):
        # Проверяем что все стороны числа
        if not all(isinstance(x, (int, float)) for x in [a, b, c, d]):
            raise TypeError("Стороны должны быть числами")

        # Проверяем что все стороны положительные
        if not all(x > 0 for x in [a, b, c, d]):
            raise ValueError("Стороны должны быть больше 0")
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def perimeter(self):
        """Считаем периметр"""
        return self.a + self.b + self.c + self.d

    def __str__(self):
        return f"Четырехугольник({self.a}, {self.b}, {self.c}, {self.d})"


class Rectangle(Quadrilateral):
    """
    Класс прямоугольник - наследуется от четырехугольника
    """

    def __init__(self, length, width):
        # Проверяем входные данные
        if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
            raise TypeError("Длина и ширина должны быть числами")

        if length <= 0 or width <= 0:
            raise ValueError("Длина и ширина должны быть больше 0")

        # Вызываем конструктор родителя: для прямоугольника стороны a,b,a,b
        super().__init__(length, width, length, width)

        self.length = length
        self.width = width

    def area(self):
        """Площадь прямоугольника"""
        return self.length * self.width

    def __str__(self):
        return f"Прямоугольник({self.length} x {self.width})"


class Square(Rectangle):
    """
    Класс квадрат - наследуется от прямоугольника
    """

    def __init__(self, side):
        # Проверяем входные данные
        if not isinstance(side, (int, float)):
            raise TypeError("Сторона должна быть числом")

        if side <= 0:
            raise ValueError("Сторона должна быть больше 0")

        # Вызываем конструктор родителя: для квадрата side, side
        super().__init__(side, side)

        self.side = side

    def __str__(self):
        return f"Квадрат({self.side})"


def input_positive_number(prompt):
    """
    Функция для ввода положительного числа с проверкой
    """
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Ошибка: число должно быть больше 0. Попробуйте снова.")
                continue
            return value
        except ValueError:
            print("Ошибка: введите корректное число. Попробуйте снова.")


def create_quadrilateral():
    """
    Создание четырехугольника с вводом данных с клавиатуры
    """
    print("Введите длины четырех сторон:")
    a = input_positive_number("Сторона A: ")
    b = input_positive_number("Сторона B: ")
    c = input_positive_number("Сторона C: ")
    d = input_positive_number("Сторона D: ")

    try:
        quadrilateral = Quadrilateral(a, b, c, d)
        print(f"\n Четырехугольник успешно создан!")
        print(f"Параметры: {quadrilateral}")
        print(f"Периметр: {quadrilateral.perimeter()}")
        return quadrilateral
    except Exception as e:
        print(f"Ошибка при создании четырехугольника: {e}")
        return None


def create_rectangle():
    """
    Создание прямоугольника с вводом данных с клавиатуры
    """

    print("Введите размеры прямоугольника:")
    length = input_positive_number("Длина: ")
    width = input_positive_number("Ширина: ")

    try:
        rectangle = Rectangle(length, width)
        print(f"\n Прямоугольник успешно создан!")
        print(f"Параметры: {rectangle}")
        print(f"Периметр: {rectangle.perimeter()}")
        print(f"Площадь: {rectangle.area()}")
        return rectangle
    except Exception as e:
        print(f"Ошибка при создании прямоугольника: {e}")
        return None


def create_square():
    """
    Создание квадрата с вводом данных с клавиатуры
    """
    side = input_positive_number("Введите длину стороны квадрата: ")

    try:
        square = Square(side)
        print(f"\n Квадрат успешно создан!")
        print(f"Параметры: {square}")
        print(f"Периметр: {square.perimeter()}")
        print(f"Площадь: {square.area()}")
        return square
    except Exception as e:
        print(f"Ошибка при создании квадрата: {e}")
        return None

def show_menu():

    print("1.Создать четырехугольник")
    print("2.Создать прямоугольник")
    print("3.Создать квадрат")
    print("4.Выход")

def main():
    """
    Основная функция программы
    """
    figures = []  # Список для хранения созданных фигур
    while True:
        show_menu()
        choice = input("\nВыберите действие (1-4): ").strip()

        if choice == '1':
            figure = create_quadrilateral()
            if figure:
                figures.append(figure)

        elif choice == '2':
            figure = create_rectangle()
            if figure:
                figures.append(figure)

        elif choice == '3':
            figure = create_square()
            if figure:
                figures.append(figure)

        elif choice == '4':
            break

        else:
            print("Неверный выбор. Пожалуйста, введите число от 1 до 4.")
if __name__ == "__main__":
    main()


#проверка на отрицательное число
#Введите длины четырех сторон:
#Сторона A: -2
#Ошибка: число должно быть больше 0. Попробуйте снова.

#нечисловой ввод
#Выберите действие (1-4): 3
#Введите длину стороны квадрата: три
#Ошибка: введите корректное число. Попробуйте снова.

#тест на 0
#Введите размеры прямоугольника:
#Длина: 0
#Ошибка: число должно быть больше 0. Попробуйте снова.

#