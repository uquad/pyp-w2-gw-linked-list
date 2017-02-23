from .interface import AbstractLinkedList
from linked_list import Node


class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None):
        if elements is not None:
            self.start=Node(elements)
            self.end=Node(elements)
        else:
            self.start=None
            self.end=None

    def __str__(self):
        pass

    def __len__(self):
        pass

    def __iter__(self):
        pass

    def __getitem__(self, index):
        pass

    def __add__(self, other):
        pass

    def __iadd__(self, other):
        pass


    def __ne__(self, other):
        pass

    def __eq__(self, other):
        pass

    def append(self, elem):
        pass

    def count(self):
        pass

    def pop(self, index=None):
        pass
