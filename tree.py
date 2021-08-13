class Node:
    def __init__(self, value):
        self._value = value
        self._parent = None
        self._children = []

    @property
    def value(self):
        return self._value

    @property
    def children(self):
        return self._children

    @property
    def parent(self):
        return self._parent

    # Call a TA on this one
    def add_child(self, new_child):
        if new_child not in self._children:
            self._children.append(new_child)
            self._parent = new_child

    def remove_child(self, node):
        self._children.pop(node)
        self._parent = None

    @parent.setter
    def parent(self, new_parent):
        self._parent = new_parent
        self.parent.add_child(self)
        self.parent.remove_child(self)
