
class Repo(object):

    def __init__(self):
        self._repo = {}

    def add(self, id, obj):
        if id in self._repo:
            return False
        self._repo[id] = obj
        return True

    def remove(self, id):
        if id in self._repo:
            del self._repo[id]

    def update(self, id, obj):
        if id in self._repo:
            self._repo[id] = obj
            return True
        return False

    def get(self, id):
        return self._repo[id]

