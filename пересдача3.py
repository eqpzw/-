class TreeNode:
    """Узел дерева Хаффмана"""

    def __init__(self, char, freq):
        self.char = char  # Символ
        self.freq = freq  # Частота
        self.left = None
        self.right = None


def build_huffman_tree(text):
    """Строит дерево Хаффмана для текста"""
    # Считаем частоты символов
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1

    # Создаем узлы для каждого символа
    nodes = [TreeNode(char, freq) for char, freq in freq.items()]

    # Строим дерево
    while len(nodes) > 1:
        # Сортируем по частоте
        nodes.sort(key=lambda x: x.freq)

        # Берем два узла с наименьшей частотой
        left = nodes.pop(0)
        right = nodes.pop(0)

        # Создаем родительский узел
        parent = TreeNode(None, left.freq + right.freq)
        parent.left = left
        parent.right = right

        nodes.append(parent)

    return nodes[0] if nodes else None


def print_tree(node, prefix="", is_left=True):
    """Выводит дерево в читаемом виде"""
    if node is None:
        return

    # Выводим текущий узел
    if node.char is not None:
        print(f"{prefix}{'├── ' if not is_left else '└── '}'{node.char}':{node.freq}")
    else:
        print(f"{prefix}{'├── ' if not is_left else '└── '}*:{node.freq}")

    # Рекурсивно выводим потомков
    if node.left or node.right:
        new_prefix = prefix + ("│   " if not is_left else "    ")
        if node.left:
            print_tree(node.left, new_prefix, False)
        if node.right:
            print_tree(node.right, new_prefix, True)


def get_huffman_codes(node, code="", codes=None):
    """Генерирует коды Хаффмана для каждого символа"""
    if codes is None:
        codes = {}

    if node is None:
        return codes

    # Если это лист (символ)
    if node.char is not None:
        codes[node.char] = code
    else:
        # Рекурсивно обходим потомков
        get_huffman_codes(node.left, code + "0", codes)
        get_huffman_codes(node.right, code + "1", codes)

    return codes


def main():
    """Основная функция"""

    # Ввод текста с проверкой
    while True:
        text = input("Введите текст на русском языке: ").strip()
        if text:
            break
        print("Ошибка: текст не может быть пустым!")


    # Уникальные буквы в тексте
    unique_chars = set(text)
    print(f"\nУникальные буквы в тексте: {''.join(sorted(unique_chars))}")

    # Строим дерево Хаффмана
    root = build_huffman_tree(text)

    if root is None:
        print("Не удалось построить дерево!")
        return

    # Выводим дерево
    print("\nДерево Хаффмана:")
    print_tree(root)

    # Получаем и выводим коды
    codes = get_huffman_codes(root)
    print("\nКоды Хаффмана:")
    for char, code in sorted(codes.items()):
        print(f"'{char}': {code}")

    # Кодируем исходный текст
    encoded_text = ''.join(codes[char] for char in text)
    print(f"\nЗакодированный текст: {encoded_text}")

if __name__ == "__main__":
    main()

#1тест на правильность работы программы
#Уникальные буквы в тексте: ипр

#Дерево Хаффмана:
#└── *:6
#    ├── 'п':3
#    └── *:3
#        ├── 'и':1
#        └── 'р':2

#Коды Хаффмана:
#'и': 10
#'п': 0
#'р': 11

#Закодированный текст: 000111110

#2тест на неверный ввод
#Введите текст на русском языке:
#Ошибка: текст не может быть пустым!

#3тест