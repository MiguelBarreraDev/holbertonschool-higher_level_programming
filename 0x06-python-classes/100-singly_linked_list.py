#!/usr/bin/python3
class Node:

    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is None or value:
            self.__next_node = value
        else:
            raise TypeError('next_node must be a Node object')


class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
        node = Node(value)
        tmp = self.head
        current = tmp
        if self.head is None or tmp.data > value:
            node.next_node = self.head
            self.head = node
        else:
            """ 2 -> 5 -> 15 -> None  """
            """          curr """
            """     tmp  """
            """           10->  """
            while current.data < value:
                if current.next_node is None:
                    current.next_node = node
                    return
                tmp = current
                current = current.next_node
            node.next_node = current
            tmp.next_node = node

    def print_list(self):
        tmp = self.head
        while tmp:
            print(tmp.data)
            tmp = tmp.next_node

    def __str__(self):
        data = ""
        while self.head:
            data += str(self.head.data)
            data += '\n'
            self.head = self.head.next_node
        return data
