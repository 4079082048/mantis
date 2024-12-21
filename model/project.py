from sys import maxsize
class Project:

    def __init__(self, name=None, description=None, status=None, inherit_global = None, view_state=None):
        self.name = name
        self.description = description
        self.status = status
        self.inherit_global = inherit_global
        self.view_state = view_state



    def __repr__(self):
        return "%s:%s:%s" % (self.name, self.description, self.status)


    def __eq__(self, other):
        return (self.name is None or other.name is None or self.name == other.name) and self.description == other.description and self.description == other.description


    def id_or_max(self):
            if self.name:
                return int(self.name)
            else:
                return maxsize

