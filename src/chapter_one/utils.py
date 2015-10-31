__author__ = 'vasiliy'

from chapter_one.models import KeyActivation, Distance


def get_key_activation_sequence(input_sequence):
    return [KeyActivation(_input.key_code, _input.key_release_time - _input.key_press_time) for _input in input_sequence]


def get_average_key_activation(key_activation_sequence):
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

def get_key_activation_dispersion(key_activation_sequence):
    average_key_activation = get_average_key_activation(key_activation_sequence)
    result = dict()
    for key in average_key_activation.keys():
        i = 0
        current_value = 0
        current_count = 0
        while i <  len(key_activation_sequence):
            if key_activation_sequence[i].key == key:
                current_value += (key_activation_sequence[i].activity_duration - average_key_activation[key]) ** 2
                current_count += 1
            i += 1
        result[key] = current_value/float(current_count)
    return result

def get_distance_sequence(input_sequence):
    dist_seq = list()

    i = 1
    while i < len(input_sequence):
        dist_seq.append(
            Distance(
                input_sequence[i - 1].key_code,
                input_sequence[i].key_code,
                input_sequence[i].key_press_time - input_sequence[i - 1].key_release_time
            )
        )
        i += 1
    return  dist_seq

def get_average_distance(distance_sequence):
    dictionary = dict()
    for distance in distance_sequence:
        if (distance.key_code_from, distance.key_code_to) in dictionary.keys():
            dictionary[(distance.key_code_from, distance.key_code_to)][0] += distance.distance
            dictionary[(distance.key_code_from, distance.key_code_to)][1] += 1
        else:
            dictionary[(distance.key_code_from, distance.key_code_to)] = [distance.distance, 1]
    result = dict()
    for key in dictionary.keys():
        result[key] = dictionary[key][0]/float(dictionary[key][1])
    return result

def get_distance_dispersion(distance_sequence):
    pass