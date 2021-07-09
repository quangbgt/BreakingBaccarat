# Define Card object
class Card:

    def __init__(self, name=None, point=None, group=None):
        self.name = name
        self.point = point
        self.group = group

    def to_string(self):
        return '{}/{}/{}'.format(self.name, str(self.point), self.group)
