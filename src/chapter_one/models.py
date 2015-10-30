__author__ = 'vasiliy'

class KeyActivation:
    """  содержит информацию о том, как долго клавиша удерживалась нажатой   """
    def __init__(self, key, activity_duration):
        self.activity_duration = activity_duration
        self.key = key

    def __str__(self):
        return "{key} : {duration}ms".format(
            key=self.key,
            duration=self.activity_duration
        )

    def __eq__(self, other):
        return self.activity_duration == other.activity_duration and self.key == other.key