__author__ = 'vasiliy'

from chapter_one.models import KeyActivation
from models import KEY_PRESS_UNIT_TYPE, KEY_RELEASE_UNIT_TYPE


class FatalError(Exception):
    pass


def getKeyActivationSequenceFromUnitSequence(unit_sequence):
    """ преобразует последовательность нажатий/отпусканий в последовательность активаций """
    prepared_sequence = __removeDuplicates(unit_sequence)
    result_sequence = list()

    while 0 < len(prepared_sequence):
        current_unit = prepared_sequence[0]
        del prepared_sequence[0]
        if current_unit.type == KEY_RELEASE_UNIT_TYPE:
            continue

        i = 0
        while i < len(prepared_sequence):
            if prepared_sequence[i] == current_unit:
                del prepared_sequence[i]
                continue
            if prepared_sequence[i].key_code == current_unit.key_code and prepared_sequence[
                i].type == KEY_RELEASE_UNIT_TYPE:
                result_sequence.append(
                    KeyActivation(current_unit.key_code, prepared_sequence[i].time_stamp - current_unit.time_stamp))
                del prepared_sequence[i]
                break
            if prepared_sequence[i].key_code != current_unit.key_code:
                i += 1
    return result_sequence


def __removeDuplicates(unit_sequence):
    """  удаляет дубликаты из последовательности нажатий/отпусканий  """
    without_duplicates = list(unit_sequence)
    i = 0
    while i < len(without_duplicates):
        current_unit = without_duplicates[i]
        j = 1
        while i + j < len(without_duplicates) and without_duplicates[i + j].time_stamp == current_unit.time_stamp:
            if without_duplicates[i + j] == current_unit:
                del without_duplicates[i + j]
            else:
                j += 1
        i += 1
    return without_duplicates


def getAverage(key_activation_sequence):
    """
    находит среднее время удержания кнопок
    :param key_activation_sequence:
    :return:
    """
    dictionary = dict()
    for key_activation in key_activation_sequence:
        if key_activation.key in dictionary.keys():
            dictionary[key_activation.key][0] += key_activation.activity_duration
            dictionary[key_activation.key][1] += 1
        else:
            dictionary[key_activation.key] = [key_activation.activity_duration, 1]
    result = dict()
    for key in dictionary.keys():
        result[key] = dictionary[key][0]/float(dictionary[key][1])
    return result