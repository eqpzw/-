class TreeNode:
    """Узел дерева Хаффмана"""

    def __init__(self, char, freq):
        self.char = char  # Символ
        self.freq = freq  # Частота
        self.left = None
        self.right = None


class HuffmanTree:
    """Класс для работы с деревом Хаффмана"""

    def __init__(self, text):
        self.root = None
        self.codes = {}
        if text:
            self._build_tree(text)
            self._generate_codes()

    def _build_tree(self, text):
        """Строит дерево Хаффмана для текста через объединение деревьев"""
        # Считаем частоты символов
        freq = {}
        for char in text:
            freq[char] = freq.get(char, 0) + 1

        # Создаем начальные узлы
        nodes = []
        for char, frequency in freq.items():
            node = TreeNode(char, frequency)
            nodes.append(node)

        # Строим дерево объединяя узлы через left и right
        while len(nodes) > 1:
            # Сортируем узлы по частоте
            nodes.sort(key=lambda x: x.freq)

            # Берем два узла с наименьшей частотой
            left_node = nodes.pop(0)
            right_node = nodes.pop(0)

            # Создаем родительский узел и связываем через left и right
            parent = TreeNode(None, left_node.freq + right_node.freq)
            parent.left = left_node
            parent.right = right_node

            nodes.append(parent)

        self.root = nodes[0] if nodes else None

    def _generate_codes(self):
        """Генерирует коды Хаффмана для каждого символа"""
        self.codes = {}
        if self.root:
            self._traverse_tree(self.root, "")

    def _traverse_tree(self, node, code):
        """Рекурсивно обходит дерево для генерации кодов"""
        if node.char is not None:
            self.codes[node.char] = code
        else:
            if node.left:
                self._traverse_tree(node.left, code + "0")
            if node.right:
                self._traverse_tree(node.right, code + "1")

    def print_tree(self):
        """Выводит дерево в читаемом виде"""
        if self.root is None:
            print("Дерево пустое")
            return
        self._print_node(self.root)

    def _print_node(self, node, prefix="", is_left=True):
        """Рекурсивно выводит узел и его потомков"""
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
                self._print_node(node.left, new_prefix, False)
            if node.right:
                self._print_node(node.right, new_prefix, True)

    def encode_text(self, text):
        """Кодирует текст с помощью кодов Хаффмана"""
        return ''.join(self.codes[char] for char in text)

    def get_codes(self):
        """Возвращает словарь кодов"""
        return self.codes.copy()

    def get_unique_chars(self):
        """Возвращает множество уникальных символов"""
        return set(self.codes.keys())


def main():
    """Основная функция"""

    # Ввод текста с проверкой
    while True:
        text = input("Введите текст на русском языке: ").strip()
        if text:
            break
        print("Ошибка: текст не может быть пустым!")

    # Создаем дерево Хаффмана
    huffman_tree = HuffmanTree(text)

    # Уникальные буквы в тексте
    unique_chars = huffman_tree.get_unique_chars()
    print(f"\nУникальные буквы в тексте: {''.join(sorted(unique_chars))}")

    # Выводим дерево
    print("\nДерево Хаффмана:")
    huffman_tree.print_tree()

    # Получаем и выводим коды
    codes = huffman_tree.get_codes()
    print("\nКоды Хаффмана:")
    for char, code in sorted(codes.items()):
        print(f"'{char}': {code}")

    # Кодируем исходный текст
    encoded_text = huffman_tree.encode_text(text)
    print(f"\nЗакодированный текст: {encoded_text}")


if __name__ == "__main__":
    main()