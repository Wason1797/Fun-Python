
class Matrix:

    def __init__(self, _items):  # this is the equivalent of a constructor
        self.items = _items

    def __repr__(self):  # ths is the equivalent of ToString() method
        obj = ""
        for column in self.items:
            for item in column:
                obj += str(item) + " "
            obj += "\n"
        return obj


matrix = Matrix([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
])

friends=["Nicole", "Fred", "Peter"]
ages = [21, 25, 22]

