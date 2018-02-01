class LinkedList:
    class _LLNode:
        def __init__(self, item, next=None):
            self.item = item
            self.next = next
            pass

    def __init__(self):
        self._head = None

    # rest of the LL function converted to methods
    def insert_head(self, o):
        """(LinkedList, object) -> NoneType
        Insert data <o> to <self> at the head
        """
        next_node = self._LLNode(o, self._head)
        self._head = next_node

class LLNode:
    """ A node for a linked list of objects.
    """

    def __init__(self, o, next = None):
        """ (LLNode, object, LLNode) - > NoneType

        Initialize a new LLNode with data <o> and
        pointer (to next node in list) <next>.
        """
        self._data = o
        self._next = next

    def __str__(self):
        """ (LLNode) -> str

        Return a readable string of <self>.
        """
        return ("LLNode: " + str(self._data) +
                " -> " + str(self._next))

    def __repr__(self):
        """ (LLNode) -> str

        Return a string representation of <self>.
        """
        return ("LLNode(" + repr(self._data) +
                ", " + repr(self._next) + ")")

    def get_data(self):
        """ (LLNode) -> int

        Return the data in <self>.
        """
        return (self._data)

    def set_data(self, o):
        """ (LLNode, object) -> None

        Store data <o> in <self>.
        """
        self._data = o

    def get_next(self):
        """ (LLNode) -> LLNode

        Return pointer to next node in <self>.
        """
        return (self._next)

    def set_next(self, next):
        """ (LLNode, LLNode) -> None

        Store pointer <next> in <self>.
        """
        self._next = next


def find(head: LLNode, o):
    """(LLNode, object) -> LLNode
    Return a node with data <o> in the list whose head is pointed to the
    <head>.
    Return None if no such node exists.
    """
    if o == head.get_data():
        return True
    next_node = head.get_next()
    if next_node is None:
        return False
    return find(next_node, o)


def find_reverse(head: LLNode, o):
    next_node = head.get_next()
    is_equal = head.get_data() == o
    if next_node is not None:
        result = find_reverse(next_node, o)
    elif is_equal:
        return head



def find_2(head: LLNode, o):
    """(head, o) -> (LLNode, LLNode)
    Return 2 nodes, the first with data <o>, the is the node that points
    to the first on the linked list whose head is <head>. For node,
    return None if it doesn't exist.

    :param head:
    :param o:
    :return:
    """


if __name__ == "__main__":
    a = LLNode(1)
    b = LLNode(2)
    a.set_next(b)
    b.set_next(LLNode(4))
    print(find_reverse(b, 2))


