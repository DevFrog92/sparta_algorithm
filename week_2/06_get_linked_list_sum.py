class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

def _get_linked_list_sum(linked_list):
    head_node = linked_list.head
    sum_value = 0
    while head_node is not None:
        sum_value = sum_value*10 + head_node.data
        head_node = head_node.next
    return sum_value

def get_linked_list_sum(linked_list_1, linked_list_2):
    sum_1 = _get_linked_list_sum(linked_list_1)
    sum_2 = _get_linked_list_sum(linked_list_2)
    return sum_1+sum_2


linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))