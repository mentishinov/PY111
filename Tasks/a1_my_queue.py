"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):
        self.queue = []

        # Начало - слева - enqueue
        # Конец - справа - dequeue

        # append, pop(-1) -> 0(1)
        # insert, del, pop(0) -> 0(n)
        ...  # todo для очереди можно использовать python list

    def enqueue(self, elem: Any) -> None:
        """
        Operation that add element to the end of the queue

        :param elem: element to be added
        :return: Nothing
        """
        last_elem = self.queue[-1]
        new_elem = last_elem.append(elem)

        print(new_elem)
        return None

    def dequeue(self) -> Any:
        """
        Return element from the beginning of the queue. Should return None if no elements.

        :return: dequeued element
        """
        first_elem = self.queue[0]
        deq_elem = first_elem.remove

        print(new_elem)
        return None

    def peek(self, ind: int = 0) -> Any:
        """
        Allow you to see at the element in the queue without dequeuing it

        :param ind: index of element (count from the beginning)
        :return: peeked element
        """
        print(ind)
        return None

    def clear(self) -> None:
        """
        Clear my queue

        :return: None
        """
        return None
