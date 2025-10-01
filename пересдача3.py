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
        self._build_tree(text)

    def _build_tree(self, text):
        """Строит дерево Хаффмана для текста"""
        if not text:
            return

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

        self.root = nodes[0] if nodes else None
        self._generate_codes()

    def _generate_codes(self, node=None, code=""):
        """Генерирует коды Хаффмана для каждого символа (внутренний метод)"""
        if node is None:
            node = self.root
            self.codes = {}

        if node is None:
            return

        # Если это лист (символ)
        if node.char is not None:
            self.codes[node.char] = code
        else:
            # Рекурсивно обходим потомков
            self._generate_codes(node.left, code + "0")
            self._generate_codes(node.right, code + "1")

    def print_tree(self, node=None, prefix="", is_left=True):
        """Выводит дерево в читаемом виде"""
        if node is None:
            node = self.root

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
                self.print_tree(node.left, new_prefix, False)
            if node.right:
                self.print_tree(node.right, new_prefix, True)

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