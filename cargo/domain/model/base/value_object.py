
class ValueObject(object):

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

