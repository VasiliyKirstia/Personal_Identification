__author__ = 'vasiliy'

import unittest
from utils import remove_duplicates, Unit, KEY_RELEASE_UNIT_TYPE, KEY_PRESS_UNIT_TYPE, remove_intermediate_pressing, get_inputs_sequence
from models import Input

class TestRemoveDuplicates(unittest.TestCase):
    def test_remove(self):
        l = [
            Unit(10, 10, KEY_PRESS_UNIT_TYPE),
            Unit(10, 11, KEY_PRESS_UNIT_TYPE),
            Unit(10, 10, KEY_PRESS_UNIT_TYPE),
            Unit(10, 11, KEY_PRESS_UNIT_TYPE),
            Unit(11, 10, KEY_RELEASE_UNIT_TYPE),
            Unit(11, 10, KEY_RELEASE_UNIT_TYPE),
        ]
        self.assertEqual(
            remove_duplicates(l),
            [
                Unit(10, 10, KEY_PRESS_UNIT_TYPE),
                Unit(10, 11, KEY_PRESS_UNIT_TYPE),
                Unit(11, 10, KEY_RELEASE_UNIT_TYPE),
            ]
        )

class TestRemoveIntermediatePressing(unittest.TestCase):
    def test_remove(self):
        l = [
            Unit(1, 10, KEY_PRESS_UNIT_TYPE),
            Unit(2, 11, KEY_PRESS_UNIT_TYPE),
            Unit(3, 10, KEY_PRESS_UNIT_TYPE),
            Unit(3.1, 10, KEY_PRESS_UNIT_TYPE),
            Unit(4, 11, KEY_PRESS_UNIT_TYPE),
            Unit(5, 11, KEY_RELEASE_UNIT_TYPE),
            Unit(6, 10, KEY_RELEASE_UNIT_TYPE),
        ]
        self.assertEqual(
            remove_intermediate_pressing(l),
            [
                Unit(1, 10, KEY_PRESS_UNIT_TYPE),
                Unit(2, 11, KEY_PRESS_UNIT_TYPE),
                Unit(5, 11, KEY_RELEASE_UNIT_TYPE),
                Unit(6, 10, KEY_RELEASE_UNIT_TYPE),
            ]
        )

class TestGetInputSequence(unittest.TestCase):
    def test_convert_us_raw(self):
        us = [
            Unit(1, 10, KEY_PRESS_UNIT_TYPE),
            Unit(2, 11, KEY_PRESS_UNIT_TYPE),
            Unit(2, 11, KEY_PRESS_UNIT_TYPE),
            Unit(2.3, 11, KEY_PRESS_UNIT_TYPE),
            Unit(3, 10, KEY_RELEASE_UNIT_TYPE),
            Unit(4, 11, KEY_RELEASE_UNIT_TYPE),
        ]
        self.assertEqual(
            get_inputs_sequence(us, True),
            [
                Input(10, 1, 3),
                Input(11, 2, 4)
            ]
        )

    def test_convert_us(self):
        us = [
            Unit(1, 10, KEY_PRESS_UNIT_TYPE),
            Unit(2, 11, KEY_PRESS_UNIT_TYPE),
            Unit(3, 10, KEY_RELEASE_UNIT_TYPE),
            Unit(4, 11, KEY_RELEASE_UNIT_TYPE),
        ]
        self.assertEqual(
            get_inputs_sequence(us, False),
            [
                Input(10, 1, 3),
                Input(11, 2, 4)
            ]
        )