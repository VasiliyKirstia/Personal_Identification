__author__ = 'vasiliy'

from chapter_one.models import KeyActivation
from models import KEY_PRESS_UNIT_TYPE, KEY_RELEASE_UNIT_TYPE
from utils import remove_duplicates, remove_intermediate_pressing


def get_key_activation_sequence(unit_sequence):
    """ преобразует последовательность нажатий/отпусканий в последовательность активаций """
    prepared_sequence = remove_intermediate_pressing(remove_duplicates(list(unit_sequence)))
    result_sequence = list()

    i = 0
    while i < len(prepared_sequence):
        current_unit = prepared_sequence[i]
        if current_unit.type == KEY_RELEASE_UNIT_TYPE:
            i += 1
            continue

        j = 0
        while i + j < len(prepared_sequence):
            if prepared_sequence[i + j].key_code == current_unit.key_code and prepared_sequence[i + j].type == KEY_RELEASE_UNIT_TYPE:
                result_sequence.append(
                    KeyActivation(current_unit.key_code, prepared_sequence[i + j].time_stamp - current_unit.time_stamp))
                break
            else:
                j += 1
        i += 1
    return result_sequence


def get_average(key_activation_sequence):
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