from ASD1.lesson01.task01 import LinkedList, Node

# 1. Связанный (связный) список
# 1.8. функцию поэлементного сложения двух одинаковых по размеру списков
# сложность (обе): O(n)
# Рефлексия по эталонному решению:
# Основные рекомендации соблюдены (сначала проверка длин, в цикле проверка только одного списка), но:
# 1. При неравенстве списков выбрасывается не исключение, а возвращается пустой список - не очень логичное поведение
# 2. Сейчас даже не могу сказать, зачем я в первоначальную проверку длин засунул list1.len() == 0
# Она просто лишняя и забирает дополнительные ресурсы. (Специально слазил в решение с первого прохождения курса - там я такую глупую проверку не добавлял :)
def sum_one_size_lists(list1: LinkedList, list2: LinkedList) -> LinkedList:
    result_list = LinkedList()
    if list1.len() != list2.len() or list1.len() == 0:
        return result_list
    node_list1 = list1.head
    node_list2 = list2.head
    while node_list1 is not None:
        result_list.add_in_tail(Node(node_list1.value + node_list2.value))
        node_list1 = node_list1.next
        node_list2 = node_list2.next

    return result_list