__author__ = 'vasiliy'

KEY_PRESS_UNIT_TYPE = 0
KEY_RELEASE_UNIT_TYPE = 1


class Unit:
    """
    абстракция нажатия/отпускания клавиши клавиатуры
    """
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

    def __eq__(self, other):
        return self.key_code == other.key_code and self.type == other.type and self.time_stamp == other.time_stamp

class Input:
    def __init__(self, key_code, key_press_time, key_release_time):
        self.key_code = key_code
        self. key_press_time = key_press_time
        self.key_release_time = key_release_time

    def __str__(self):
        return "<{k}: {p} - {r}>".format(k=self.key_code, p=self.key_press_time, r=self.key_release_time)

    def __eq__(self, other):
        return self.key_code == other.key_code and self.key_release_time == other.key_release_time and self.key_press_time == other.key_press_time
