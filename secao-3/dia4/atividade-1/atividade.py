from linked_list import LinkedList
# from node import Node


class Queue:
    def __init__(self) -> None:
        self.__data = LinkedList()

    def is_empty(self):
        return not len(self.__data)

    def enqueue(self, value):
        self.__data.insert_last(value)

    def dequeue(self):
        return self.__data.remove_first()

    def peek(self):
        return self.__data.get_element_at(0)

    def __str__(self):
        if (self.__data):
            return f"{self.__data}."
        return f"{self.__data}."


linta = Queue()
linta.enqueue('keyla')
linta.enqueue('rafa')
linta.enqueue('tutu')
print(linta)
