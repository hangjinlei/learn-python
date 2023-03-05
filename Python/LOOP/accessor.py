class Person:
    def __init__(self, first_name):
        self._first_name = first_name

    @property
    def first_name(self) -> str:
        print("getter")
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError("Expected a string")
        print("setter")
        self._first_name = value

    @first_name.deleter
    def first_name(self):
        print("deleter")
        raise AttributeError("Can't delete attribute")
        # del self._first_name
