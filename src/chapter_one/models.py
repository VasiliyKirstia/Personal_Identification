__author__ = 'vasiliy'

class InnerDistance:
    """  внутреннее растояние   """
    def __init__(self, key_code, distance):
        self.distance = distance
        self.key_code = key_code

    def __str__(self):
        return "{key} : {dist}ms".format(
            key=self.key_code,
            dist=self.distance
        )

    def __eq__(self, other):
        return self.distance == other.distance and self.key_code == other.key_code

class OuterDistance:
    """ растояние между отпусканием n-й клавиши и нажатием n+1 """
    def __init__(self, key_code_from, key_code_to, distance):
        self.key_code_from = key_code_from
        self.key_code_to = key_code_to
        self.distance = distance

    def __eq__(self, other):
        return self.key_code_from == other.key_code_from and self.key_code_to == other.key_code_to and self.distance == other.distance
