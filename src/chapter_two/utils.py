__author__ = 'vasiliy'

from utils import get_inputs_sequence_from_messages_sequence


def get_digraphs_sequence(messages_sequence):
    result_sequence = list()
    for _tuple in get_inputs_sequence_from_messages_sequence(messages_sequence):
        i = 1
        while i < len(_tuple):
            result_sequence.append(_tuple[i].key_press_time - _tuple[i-1].key_press_time)
            i+=1
    return result_sequence


def get_threegraphs_sequence(messages_sequence):
    result_sequence = list()
    for _tuple in get_inputs_sequence_from_messages_sequence(messages_sequence):
        i = 2
        while i < len(_tuple):
            result_sequence.append(_tuple[i].key_press_time - _tuple[i-2].key_press_time)
            i+=1
    return result_sequence