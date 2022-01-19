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
    """
    class SinglyLinkedList that defines a singly linked list
    """
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        node = Node(value)
        tmp = self.__head
        current = tmp
        if self.__head is None or tmp.data > value:
            node.next_node = self.__head
            self.__head = node
        else:
            """Alert"""
            tmp = self.__head
            while (tmp.next_node and ((tmp.next_node).data < value)):
                tmp = tmp.next_node
            node.next_node = tmp.next_node
            tmp.next_node = node

    def print_list(self):
        tmp = self.__head
        while tmp:
            print(tmp.data)
            tmp = tmp.next_node

    def __str__(self):
        data = ""
        while self.__head:
            data += str(self.__head.data)
            data += '\n'
            self.__head = self.__head.next_node
        return data
