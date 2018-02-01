from abc import ABC, abstractmethod


class ContainerFullException(Exception):
    pass


class ContainerEmptyException(Exception):
    pass


class AbstractContainer(ABC):

    @abstractmethod
    def put(self, item):
        pass

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def copy(self):
        pass

    @abstractmethod
    def is_empty(self):
        pass

# A queue class (not python's queue)
# Uses a dictionary for the queue.
# Raises EmptyQueueError when dq'ing from an empty queue.


class Queue(AbstractContainer):
    NAME = 'queue'

    def __init__(self: 'Queue') -> None:
        # Representation invariant:
        # _first and _next are ints.
        # _contents is a dict of int:object.
        # _next-_first is the number of elements in me.
        # If _next>_first, then
        #   _contents[_first], ..., _contents[_next-1]
        #    are the elements in the order they were inserted.
        self._contents = {}
        self._first = 0
        self._next = 0

    def __str__(self: 'Queue') -> str:
        s = ""
        for i in range(self._first, self._next):
            s = s + str(self._contents[i]) + ", "
        return s[:-2]

    def enqueue(self: 'Queue', item: 'object') -> None:
        self._contents[self._next] = item
        self._next = self._next + 1

    def dequeue(self: 'Queue') -> object:
        if self.is_empty():
            raise ContainerEmptyException()
        item = self._contents[self._first]
        del self._contents[self._first]
        self._first = self._first + 1
        return item

    def is_empty(self: 'Queue') -> bool:
        return self._first == self._next

    def put(self, item):
        self.enqueue(item)

    def get(self):
        return self.dequeue()

    def copy(self):
        copy_stack = Queue()
        copy_stack._contents = self._contents.copy()
        copy_stack._first = self._first
        copy_stack._next = self._next
        return copy_stack

# A stack class
# Uses a dictionary for the stack.
# Raises EmptyStackError when popping from an empty stack.
# Needs comments.



class Stack(AbstractContainer):
    NAME = 'stack'

    def __init__(self: 'Stack') -> None:
        self._contents = {}
        self._num_items = 0

    def __str__(self: 'Stack') -> str:
        s = ""
        for i in range(1, self._num_items + 1):
            s = s + str(self._contents[i]) + ", "
        return s[:-2]

    def push(self: 'Stack', item: 'object') -> None:
        self._num_items = self._num_items + 1
        self._contents[self._num_items] = item

    def pop(self: 'Stack') -> object:
        if self.is_empty():
            raise ContainerEmptyException()
        item = self._contents[self._num_items]
        del self._contents[self._num_items]
        self._num_items = self._num_items - 1
        return item

    def is_empty(self: 'Stack') -> bool:
        return self._num_items == 0

    def put(self, item):
        self.push(item)

    def get(self):
        return self.pop()

    def copy(self):
        copy_stack = Stack()
        copy_stack._contents = self._contents.copy()
        copy_stack._num_items = self._num_items
        return copy_stack


class NeckQueue(AbstractContainer):
    """The Class which represents the neck queue"""
    NAME = 'neckqueue'

    def __init__(self: "NeckQueue") -> None:
        """(NeckQueue) -> NoneType
        Initialize the NeckQueue method.
        """
        # Initialize the two stacks used to implement the NeckQueue.
        self._inverse_stack = Stack()
        self._direct_stack = Stack()
        # Initialize the length of the stack.
        self.length = 0
        # Initialize the head item of the stack.
        self._head = None

    def dequeue(self: "NeckQueue") -> object:
        """(NeckQueue) -> object
        Return the second item in the neck queue. If there is only one
        item left in the queue, then return that item. If this method is
        invoked when there is no item in the neck queue, raise the
        EmptyQueueError.
        RAISE: EmptyQueueError
        """
        # If there is no item in the container, then raise EmptyQueueError.
        if self.length == 0:
            raise ContainerEmptyException()
        # If there is only one item in the container, then return the head item.
        if self.length == 1:
            result = self._head
        # Otherwise,
        else:
            # If there is no item in the inverse stack, pop all items in the
            # direct stack to the inverse stack to reverse the order of all
            # items, so that, the container will return the item in FIFO manner.
            if self._inverse_stack.is_empty():
                while not self._direct_stack.is_empty():
                    self._inverse_stack.push(self._direct_stack.pop())
            # Pop the first item in the inverse stack as the return value.
            result = self._inverse_stack.pop()
        # decrease the length of the container by one.
        self.length -= 1
        # Return value.
        return result

    def enqueue(self: "NeckQueue", o: object) -> None:
        """(NeckQueue, object) -> NoneType
        Given any object, append the object to the tail of the current
        neck queue.
        """
        # If there is no item in the NeckQueue, then insert the item as the head
        # of the NeckQueue.
        if self.length == 0:
            self._head = o
        # Otherwise, insert the object to the direct stack of the NeckQueue.
        else:
            self._direct_stack.push(o)
        # Increase the length of the container by one.
        self.length += 1

    def is_empty(self: "NeckQueue") -> bool:
        """(NeckQueue) -> bool
        Return whether the current neck queue is empty.
        """
        # If the length of the NeckQueue is 0, then it is empty.
        return self.length == 0

    def put(self, item):
        self.enqueue(item)

    def get(self):
        return self.dequeue()

    def copy(self: 'NeckQueue') -> 'NeckQueue':
        """(NeckQueue) -> NeckQueue
        Copy the current instance and return another instance.
        """
        # Declare the new NeckQueue.
        copy_queue = NeckQueue()
        # Copy all attributes in current NeckQueue.
        copy_queue.length = self.length
        copy_queue._head = self._head
        copy_queue._direct_stack = self._direct_stack.copy()
        copy_queue._inverse_stack = self._inverse_stack.copy()
        return copy_queue


class Bucket(AbstractContainer):
    """The class which represents the bucket"""
    NAME = 'bucket'

    def __init__(self: 'Bucket') -> None:
        self._item = None
        self._is_full = False

    def push(self: 'Bucket', item: object) -> None:
        if self._is_full:
            raise ContainerFullException()
        self._item = item
        self._is_full = True

    def pop(self: 'Bucket') -> object:
        if not self._is_full:
            raise ContainerEmptyException()
        self._is_full = False
        return self._item

    def is_empty(self: 'Bucket') -> bool:
        return not self._is_full

    def put(self: 'Bucket', item: object) -> None:
        self.push(item)

    def get(self: 'Bucket') -> object:
        return self.pop()

    def copy(self: 'Bucket') -> 'Bucket':
        copy_bucket = Bucket()
        copy_bucket._is_full = self._is_full
        copy_bucket._item = self._item
        return copy_bucket


if __name__ == '__main__':
    neck = NeckQueue()

    my_word = 'banana'
    for char in my_word:
        neck.enqueue(char)

    scrabbled_word = ''
    while not neck.is_empty():
        scrabbled_word += neck.dequeue()

    print(scrabbled_word)

    my_word = 'airplay'
    for char in my_word:
        neck.enqueue(char)

    scrabbled_word = ''
    while not neck.is_empty():
        scrabbled_word += neck.dequeue()

    print(scrabbled_word)
