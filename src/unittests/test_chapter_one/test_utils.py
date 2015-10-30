__author__ = 'vasiliy'
from chapter_one.utils import get_key_activation_sequence, get_average_key_activation, get_average_distance, get_distance_sequence
from chapter_one.models import KeyActivation, Distance
from models import Input
import unittest

class TestGetKeyActivationSequence(unittest.TestCase):
    def test_get_ka(self):
        inputs = [
            Input(10, 1, 3),
            Input(11, 2.1, 4)
        ]
        self.assertEqual(
            get_key_activation_sequence(inputs),
            [
                KeyActivation(10, 2),
                KeyActivation(11, 1.9)
            ]
        )

class TestGetAverageKeyActivation(unittest.TestCase):
    def test_get_a(self):
        kas = [
            KeyActivation(1, 2),
            KeyActivation(2, 2),
            KeyActivation(3, 4),
            KeyActivation(2, 2),
            KeyActivation(2, 2),
            KeyActivation(1, 2),
            KeyActivation(1, 2)
        ]
        self.assertDictEqual(
            get_average_key_activation(kas),
            {
                1: 2,
                2: 2,
                3: 4
            }
        )
class TestGetDistanceSequence(unittest.TestCase):
    def test_get_dist(self):
        inputs = [
            Input(10, 1, 3),
            Input(11, 2, 4),
            Input(12, 6, 8)
        ]
        self.assertEqual(
            get_distance_sequence(inputs),
            [
                Distance(10, 11, -1),
                Distance(11, 12, 2)
            ]
        )

class TestGetAverageDistance(unittest.TestCase):
    def test_get_a(self):
        dists = [
            Distance(10, 11, 2),
            Distance(10, 11, 4),
            Distance(12, 11, 2),
            Distance(12, 11, 4),
            Distance(1, 2, 2),
        ]
        self.assertDictEqual(
            get_average_distance(dists),
            {
                (10,11):3,
                (12,11):3,
                (1,2):2
            }
        )