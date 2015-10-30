__author__ = 'vasiliy'

from chapter_one.models import KeyActivation


def get_key_activation_sequence(input_sequence):
    return [KeyActivation(_input.key_code, _input.key_release_time - _input.key_press_time) for _input in input_sequence]


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