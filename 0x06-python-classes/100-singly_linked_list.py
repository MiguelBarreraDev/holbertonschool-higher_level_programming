#!/usr/bin/python3
"""Sinlgy linked list"""


class Node:
    """
    class Node that defines a node of a singly linked list
    """
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
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if isintance(value, Node) or value is None:
            self.__next_node = value
        else:
            raise TypeError('next_node must be a Node object')


"""Class SinglyLinkedList"""


class SinglyLinkedList:
    """
    class SinglyLinkedList that defines a singly linked list
    """
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        node = Node(value)
        if not self.__head or self.__head.data >= value:
            node.next_node = self.__head
            self.__head = node
        else:
            tmp = self.__head
            while (tmp.next_node and ((tmp.next_node).data < value)):
                tmp = tmp.next_node
            node.next_node = tmp.next_node
            tmp.next_node = node

    def __str__(self):
        data = ""
        tmp = self.__head
        while tmp:
            data += str(tmp.data)
            tmp = tmp.next_node
            if tmp:
                data += '\n'
        return data
