__author__ = 'vasiliy'

KEY_PRESS_UNIT_TYPE = 0
KEY_RELEASE_UNIT_TYPE = 1

class Unit:
    def __init__(self, time_stamp, key_code, unit_type):
        self.time_stamp = time_stamp
        self.key_code = key_code
        self.type = unit_type

    def __str__(self):
        return str(
            "{time}: {key}  {type}".format(
                key=self.key_code,
                time=self.time_stamp,
                type=('PRESS' if self.type == KEY_PRESS_UNIT_TYPE else 'release')
            )
        )

class Pack:
    units_sequence = []
    is_sorted = False

    def addUnit(self, unit):
        if Unit is not Unit:
            raise TypeError
        self.units_sequence.append(unit)
        self.is_sorted = False

    def isSorted(self):
        return self.is_sorted

    def Sort(self):
        if not self.is_sorted:
            return #don`t sort
        else:
            self.is_sorted = True
            return #sort