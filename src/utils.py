__author__ = 'vasiliy'
from models import KEY_PRESS_UNIT_TYPE, KEY_RELEASE_UNIT_TYPE, Unit, Input

def remove_duplicates(unit_sequence):
    """  удаляет дубликаты из последовательности нажатий/отпусканий  """
    i = 0
    while i < len(unit_sequence):
        current_unit = unit_sequence[i]
        j = 1
        while i + j < len(unit_sequence) and unit_sequence[i + j].time_stamp == current_unit.time_stamp:
            if unit_sequence[i + j].key_code == current_unit.key_code and unit_sequence[i + j].type == current_unit.type:
                del unit_sequence[i + j]
            else:
                j += 1
        i += 1
    return unit_sequence

def remove_intermediate_pressing(unit_sequence):
    """ удаляет промежуточные срабатывания события key_press во время удержания клавиши нажатой """
    i = 0
    while i < len(unit_sequence):
        if unit_sequence[i].type == KEY_RELEASE_UNIT_TYPE:
            i += 1
            continue

        current_unit = unit_sequence[i]

        j = 1
        while i + j < len(unit_sequence):
            if unit_sequence[i + j].key_code == current_unit.key_code and unit_sequence[i + j].type == KEY_RELEASE_UNIT_TYPE:
                break
            if unit_sequence[i + j].key_code != current_unit.key_code:
                j += 1
                continue
            if unit_sequence[i + j].key_code == current_unit.key_code and unit_sequence[i + j].type == current_unit.type:
                del unit_sequence[i + j]
        i += 1
    return unit_sequence


def get_inputs_sequence(unit_sequence, is_raw):
    if is_raw:
        unit_sequence = remove_intermediate_pressing(remove_duplicates(unit_sequence))
    input_sequence = list()

    i = 0
    while i < len(unit_sequence):
        if unit_sequence[i].type == KEY_RELEASE_UNIT_TYPE:
            i += 1
            continue

        current_unit = unit_sequence[i]

        j = 1
        while i + j < len(unit_sequence):
            if unit_sequence[i + j].key_code == current_unit.key_code and unit_sequence[i + j].type == KEY_RELEASE_UNIT_TYPE:
                input_sequence.append(Input(current_unit.key_code, current_unit.time_stamp, unit_sequence[i + j].time_stamp))
                break
            else:
                j += 1
        i += 1
    return input_sequence


def get_inputs_sequence_from_messages_sequence(messages_sequence):
    input_sequence = list()

    for message in messages_sequence:
        temp_seq = list()
        i = 0
        while i < len(message):
            if message[i].type == KEY_RELEASE_UNIT_TYPE:
                i += 1
                continue

            current_unit = message[i]

            j = 1
            while i + j < len(message):
                if message[i + j].key_code == current_unit.key_code and message[i + j].type == KEY_RELEASE_UNIT_TYPE:
                    temp_seq.append(Input(current_unit.key_code, current_unit.time_stamp, message[i + j].time_stamp))
                    break
                else:
                    j += 1
            i += 1
        input_sequence.append(tuple(temp_seq))
    return input_sequence