__author__ = 'vasiliy'

from chapter_one.models import InnerDistance, OuterDistance
import math


def get_inner_distance_sequence(input_sequence):
    return [InnerDistance(_input.key_code, _input.key_release_time - _input.key_press_time) for _input in input_sequence]


def get_average_inner_distance(inner_distance_sequence):
    """
    находит математическое ожидание для каждой из кнопок
    :param inner_distance_sequence:
    :return:
    """
    dictionary = dict()
    for inner_distance in inner_distance_sequence:
        if inner_distance.key_code in dictionary.keys():
            dictionary[inner_distance.key_code][0] += inner_distance.distance
            dictionary[inner_distance.key_code][1] += 1
        else:
            dictionary[inner_distance.key_code] = [inner_distance.distance, 1]
    result = list()
    for key in dictionary.keys():
        result.append( InnerDistance(key, dictionary[key][0]/float(dictionary[key][1])) )
    return result


def get_inner_distance_dispersion(inner_distance_sequence):
    average_inner_distance_list = get_average_inner_distance(inner_distance_sequence)
    result = list()
    for aid in average_inner_distance_list:
        i = 0
        current_value = 0
        current_count = 0
        while i <  len(inner_distance_sequence):
            if inner_distance_sequence[i].key_code == aid.key_code:
                current_value += (inner_distance_sequence[i].distance - aid.distance) ** 2
                current_count += 1
            i += 1
        result.append( InnerDistance(aid.key_code, current_value/float(current_count)) )
    return result


def get_inner_distance_standard_deviation(inner_distance_sequence):
    inner_distance_dispersion_list = get_inner_distance_dispersion(inner_distance_sequence)
    for idd in inner_distance_dispersion_list:
        idd.distance = math.sqrt(idd.distance)
    return inner_distance_dispersion_list


def get_outer_distance_sequence(input_sequence):
    dist_seq = list()

    i = 1
    while i < len(input_sequence):
        dist_seq.append(
            OuterDistance(
                input_sequence[i - 1].key_code,
                input_sequence[i].key_code,
                input_sequence[i].key_press_time - input_sequence[i - 1].key_release_time
            )
        )
        i += 1
    return  dist_seq


def get_average_outer_distance(outer_distance_sequence):
    dictionary = dict()
    for distance in outer_distance_sequence: #TODO избавиться от словаря с адовыми кортежами вместо ключей
        if (distance.key_code_from, distance.key_code_to) in dictionary.keys():
            dictionary[(distance.key_code_from, distance.key_code_to)][0] += distance.distance
            dictionary[(distance.key_code_from, distance.key_code_to)][1] += 1
        else:
            dictionary[(distance.key_code_from, distance.key_code_to)] = [distance.distance, 1]
    result = list()
    for key in dictionary.keys():
        result.append( OuterDistance(key[0], key[1], dictionary[key][0]/float(dictionary[key][1])) )
    return result


def get_outer_distance_dispersion(outer_distance_sequence):
    average_distance = get_average_outer_distance(outer_distance_sequence)
    result = list()

    for ad in average_distance:
        i = 0
        current_value = 0
        current_count = 0
        while i <  len(outer_distance_sequence):
            if outer_distance_sequence[i].key_code_from == ad.key_code_from and outer_distance_sequence[i].key_code_to == ad.key_code_to:
                current_value += (outer_distance_sequence[i].distance - ad.distance) ** 2
                current_count += 1
            i += 1
        result.append( OuterDistance(ad.key_code_from, ad.key_code_to, current_value/float(current_count)) )
    return result


def get_outer_distance_standard_deviation(outer_distance_sequence):
    outer_distance_dispersion_list = get_outer_distance_dispersion(outer_distance_sequence)
    for odd in outer_distance_dispersion_list:
        odd.distance = math.sqrt(odd.distance)
    return outer_distance_dispersion_list