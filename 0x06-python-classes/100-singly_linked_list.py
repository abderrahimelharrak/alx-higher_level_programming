#!/usr/bin/python3
"""Define classes for a singly-linked list."""

class Node:
    """Representation a node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new Node.

        Args:
            data (int): The data of the new Node.
            next_node (Node): The next node of the new Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """set and get the data of the Node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """set and get the next_node of the Node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Representation a singly-linked list."""

    def __init__(self):
        """Initalization a new SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Insertion a new Node to the SinglyLinkedList.

        Args:
            value (Node): The new Node to insert.
        """
        nouveau = Node(value)
        if self.__head is None:
            nouveau.next_node = None
            self.__head = nouveau
        elif self.__head.data > value:
            nouveau.next_node = self.__head
            self.__head = nouveau
        else:
            temp = self.__head
            while (temp.next_node is not None and
                    temp.next_node.data < value):
                temp = temp.next_node
            nouveau.next_node = temp.next_node
            temp.next_node = nouveau

    def __ptr__(self):
        """Definir the print() representation of a SinglyLinkedList."""
        values = []
        temp = self.__head
        while temp is not None:
            values.append(ptr(temp.data))
            temp = temp.next_node
        return ('\n'.join(values))
