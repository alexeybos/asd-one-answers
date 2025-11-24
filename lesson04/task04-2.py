# Задачи текущего урока (4. Стек)
# 4. Стек
# 4.2 Переделайте реализацию стека так, чтобы она работала не с хвостом списка как с верхушкой стека, а с его головой
# Сложность pop() - O(n); push() O(n) - т.к. при удалении и вставке первого элемента всегда происходит сдвиг массива
class HeadStack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        val = self.peek()
        if val is None:
            return None
        del self.stack[0]
        return val

    def push(self, value):
        self.stack.insert(0, value)

    def peek(self):
        if self.size() == 0:
            return None
        val = self.stack[0]
        return val

# 4. Стек
# 5.* Напишите функцию, которая проверяет сбалансированность открывающих и закрывающих скобок
# Сложность временная и пространственная O(n)
def is_brackets_balanced(brackets: str) -> bool:
    stack = Stack()
    cur_char = '('
    for char in brackets:
        if char == '(':
            stack.push(char)
        else:
            cur_char = stack.pop()
        if cur_char is None:
            return False
    return stack.size() == 0

# 4. Стек
# 6.* Расширьте функцию проверки сбалансированности скобок, если скобки могут быть трех типов: (), {}, [].
# Сложность временная и пространственная O(n)
def is_brackets_balanced_extended(brackets: str) -> bool:
    stack = Stack()
    dct = {'(': ')', '[': ']', '{': '}'}
    is_bracket_equal = True
    for char in brackets:
        if char in dct.keys():
            stack.push(dct.get(char))
        else:
            is_bracket_equal = stack.pop() == char
        if not is_bracket_equal:
            return False
    return stack.size() == 0

# 4. Стек
# 7.* Добавьте в стек функцию, возвращающую текущий минимальный элемент в нём за O(1)
# 4. Стек
# 8.* Добавьте в стек функцию, которая возвращает среднее значение всех элементов в стеке. Она должна выполняться за O(1).
# Обе добавлены в модифицированный класс Stack ниже:
class Stack:
    def __init__(self):
        self.stack = []
        self.min_values = []
        self.sum = 0

    # 4. Стек
    # 7.* Добавьте в стек функцию, возвращающую текущий минимальный элемент в нём за O(1)
    def get_min_value(self):
        return self.min_values[-1]

    # 4. Стек
    # 8.* Добавьте в стек функцию, которая возвращает среднее значение всех элементов в стеке. Она должна выполняться за O(1).
    def get_average(self):
        return self.sum / self.size()

    def size(self):
        return len(self.stack)

    def pop(self):
        val = self.peek()
        if val is None:
            return None
        del self.stack[-1]
        if isinstance(val, (int, float)):
            self.sum -= val
        if isinstance(val, (int, float)) and val == self.min_values[-1]:
            self.min_values.pop()
        return val

    def push(self, value):
        self.stack.append(value)
        if isinstance(value, (int, float)):
            self.sum += value
        if isinstance(value, (int, float)) and (len(self.min_values) == 0 or value <= self.min_values[-1]):
            self.min_values.append(value)

    def peek(self):
        if self.size() == 0:
            return None
        val = self.stack[self.size() - 1]
        return val

# 4. Стек
# 9*. Напишите функцию, которая с помощью двух стеков реализует вычисление постфиксных выражений.
# Сложность временная и пространственная O(n)
def calc_postfix_expression(expression: str):
    stack1 = Stack()
    stack2 = Stack()
    lambda_sum = lambda x, y: x + y
    lambda_subtract = lambda x, y: x - y
    lambda_prod = lambda x, y: x * y
    lambda_div = lambda x, y: x / y
    operators = {'+': lambda_sum, '-': lambda_subtract, '*': lambda_prod, '/': lambda_div}
    result = 0
    expression_as_list = expression[::-1].split()
    for item in expression_as_list:
        stack1.push(item)
    item = stack1.pop()
    while item is not None and item != '=':
        if item in operators.keys():
            x = stack2.pop()
            y = stack2.pop()
            result = operators[item](int(x), int(y))
            stack2.push(result)
        else:
            stack2.push(item)
        item = stack1.pop()
    return result

# Рефлексия по эталонным решениям предыдущих заданий:
# 2. Двунаправленный связный (связанный) список
# 2.10.* Метод, который "переворачивает" порядок элементов в связном списке.
# Здесь без сюрпризов - реализовано как рекомендовано эталоном. Разве что head с tail поменял местами сразу, до прохода по всему списку.

# 2.11.* Добавьте булев метод, который сообщает, имеются ли циклы (замкнутые на себя по кругу) внутри списка.
# Эталон: Цикл for по элементам до длины списка, и если конечным узлом не будет хвост, значит в списке есть цикл.
# Реализация: использован алгоритм "черепахи и зайца". Задачу он решает, но эталонный алгоритм кажется проще.
# В случае отсутствия циклов он отработает медленнее, т.к. "заяц" достигает хвоста быстрее, но в случае наличия цикла,
# в зависимости то его размера и места нахождения, может завершиться быстрее использованного алгоритма.

# 2.12.* Добавьте метод, сортирующий список.
# В эталоне предложена пузырьковая сортировка, а в моем решении я использовал сортировку слиянием, т.к. по различным источникам именно ее рекомендуют
# для сортировки двусвязного списка. Сложности: временная О(n**2) против O(n log n), а вот пространственная: О(1) у пузырьковой против О(log n) у слияния.

# 2.13.* Добавьте метод, объединяющий два списка в третий. Cписки предварительно отсортировать, и выдать результирующий список, в котором все элементы также будут упорядочены.
# По сути были использованы методы, написанные для предыдущего задания, т.к. merge двух отсортированных списков является частью алгоритма сортировки слиянием.
# Т.о. рекомендации эталонного решения выполнены

# 2.14.* Список с двумя фиктивными (dummy) узлами. И список с одним dummy узлом
# Все рекомендации эталонного решения выполнены - узел Dummy наследник Node, никаких лишних полей не содержит.
# Проверка в методах идет по типу узла. Второй вариант (с одним dummy-узлом) также реализован.

