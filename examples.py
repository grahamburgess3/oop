def increment(int):
    new_int = int + 1
    return new_int

class MyInt():
    def __init__(self):
        self.val = 0
    def increment(self):
        self.val += 1
    def __repr__(self):
        return str(self.val)

