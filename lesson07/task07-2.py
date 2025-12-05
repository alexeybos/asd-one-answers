# 7. Упорядоченный список
# 8.* Добавьте метод удаления всех дубликатов из упорядоченного списка.
# Сложность временная O(n) и пространственная O(1)
    def delete_duplicates(self):
        node = self.head
        if node is None:
            return
        while node.next is not None:
            if node.value == node.next.value:
                self.__del_node(node)
            node = node.next

    def __del_node(self, node: Node):
        if node is None:
            return
        if node.prev is None and node.next is None:
            self.clean(self.__ascending)
            return
        if self.head == node:
            self.head = node.next
            node.next.prev = None
            return
        if self.tail == node:
            self.tail = node.prev
            node.prev.next = None
            return
        node.prev.next = node.next
        node.next.prev = node.prev

# 7. Упорядоченный список
# 9.* Напишите алгоритм слияния двух упорядоченных списков в один, сохраняя порядок элементов.
#
# Для упрощения предполагаем, что списки упорядочены однонаправленно
# 1. Берем первые элементы списка.
# 2. Сравниваем элементы
# 3. Наименьший (наибольший) элемент кладем в результирующий список.
#    В этом случае элемент всегда будет tail, т.е. будет вставляться сразу, без дополнительного цикла по списку.
#    В списке, из которого взяли элемент переходим в next. Идем на шаг 2.
# 4. Когда заканчивается один из списков, перекладываем в результирующий список оставшиеся элементы из второго списка
# Сложность временная O(n) и пространственная O(n)

# 7. Упорядоченный список
# 10.* Напишите метод проверки наличия заданного упорядоченного под-списка (параметр метода) в текущем списке.
# Сложность временная O(n) и пространственная O(1)
    def check_sub_list_in_list(self, list) -> bool:
        if len(list) > self.len():
            return False
        i = 0
        node = self.find(list[i])
        if node is None:
            return False
        while node is not None:
            if node.value == list[i] and i == len(list) - 1:
                return True
            if node.value == list[i]:
                i += 1
            else:
                i = 0
            node = node.next
        return False

# 7. Упорядоченный список
# 11.* Добавьте метод, который находит наиболее часто встречающееся значение в списке.
# Сложность временная O(n) и пространственная O(1)
    def find_most_frequent(self):
        node = self.head
        most_frequent = node.value
        cur_frequent = node.value
        max_cnt = 0
        cnt = 0
        while node is not None:
            if node.value == cur_frequent:
                cnt += 1
            else:
                cur_cnt = cnt
                cnt = 1
            if node.value != cur_frequent and cur_cnt > max_cnt:
                most_frequent = cur_frequent
                cur_frequent = node.value
                max_cnt = cur_cnt
            node = node.next
        return most_frequent

# 7. Упорядоченный список
# 12.* Добавьте в упорядоченный список возможность найти индекс элемента (параметр) в списке, которая должна работать за o(log N).
    def get_index(self, val):
        cnt = self.len()
        if self.head is None:
            return -1
        if self.head == val:
            return 0
        if self.tail == val:
            return cnt - 1
        node = self.head
        left_node = self.head
        left_index = 0
        right_index = cnt - 1
        mid = int((right_index - left_index) / 2)
        while left_index <= right_index:
            ind = 0
            for i in range(ind, mid):
                node = node.next
                ind += 1
            if self.__ascending:
                compare_result = self.compare(val, node.value)
            else:
                compare_result = self.compare(node.value, val)
            if compare_result == 0:
                return ind + left_index
            if compare_result == -1:
                right_index = ind + left_index - 1
                node = left_node
            else:
                left_index = ind + left_index + 1
                left_node = node.next
                node = node.next
            mid = int((right_index - left_index) / 2)
        return -1


# Рефлексия по эталонным решениям предыдущих заданий:
# 5. Очереди
# 3.* Напишите функцию, которая "вращает" очередь по кругу на N элементов.
# Задание простое, реализовано как рекомендовано эталоном.

# 4.* Реализуйте очередь с помощью двух стеков.
# Здесь тоже все по рекомендациям. При первом прохождении насколько помню изначально было сделано не оптимально -
# перегонял во второй стек сразу при вталкивании. В этот раз такой ошибки не допустил.

# 5.* Добавьте функцию, которая обращает все элементы в очереди в обратном порядке.
# Задание простое, реализовано как рекомендовано эталоном.

# 6.* Реализуйте круговую (циклическую буферную) очередь статическим массивом фиксированного размера.
# По самому алгоритму в основном все сделано верно. Но два важны отличия, которые я не додумал при реализации:
# 1. указатель tail указывает не на ячейку, куда будет добавлен элемент, а на последний добавленный элемент.
# И, как следствие, при пустой очереди его показания некорректны. Соответственно отсюда следует
# 2. Состояния "пустая/полная очередь" определяются не по значениям указателей head/tail, а считается count и
# сравнивается с заданным размером массива. Тут я не додумался до "нужно оставлять одну пустую ячейку между head и tail,
# чтобы различать состояния "пусто" и "полно"."
# Но вообще подход с пустой ячейкой мне кажется более надежным и правильным, когда полнота очереди определяется состоянием
# указателей, а не учетом дополнительных "специальных" внутренних параметров.