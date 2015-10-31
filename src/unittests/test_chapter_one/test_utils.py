__author__ = 'vasiliy'
from chapter_one.utils import get_key_activation_sequence, get_average_key_activation, get_average_distance, \
    get_distance_sequence, get_key_activation_dispersion, get_distance_dispersion
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
            KeyActivation(1, 1),
            KeyActivation(2, 2),
            KeyActivation(3, 4),
            KeyActivation(2, 2),
            KeyActivation(2, 2),
            KeyActivation(1, 2),
            KeyActivation(1, 2)
        ]
        self.assertEqual(
            get_average_key_activation(kas),
            [
                KeyActivation(1, 5/3.0),
                KeyActivation(2, 2),
                KeyActivation(3, 4)
            ]
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
        for item in get_average_distance(dists):
            self.assertIn(
                item,
                [
                    Distance(10,11,3),
                    Distance(12,11,3),
                    Distance(1,2,2)
                ]
            )
    def test_get_a_count(self):
        dists = [
            Distance(10, 11, 2),
            Distance(10, 11, 4),
            Distance(12, 11, 2),
            Distance(12, 11, 4),
            Distance(1, 2, 2),
        ]
        self.assertEqual(3 , len(get_average_distance(dists)))

class TestGetKeyActivationDispersion(unittest.TestCase):
    def test_get_d(self):
        kas = [
            KeyActivation(1, 1),
            KeyActivation(2, 2),
            KeyActivation(3, 4),
            KeyActivation(2, 2),
            KeyActivation(2, 2),
            KeyActivation(1, 2),
            KeyActivation(1, 2)
        ]
        self.assertEqual(
            get_key_activation_dispersion(kas),
            [
                KeyActivation(1, ( (1-5/3.0)**2 + (2-5/3.0)**2 + (2-5/3.0)**2 )/3.0),
                KeyActivation(2, 0),
                KeyActivation(3, 0)
            ]
        )

class TestGetDistanceDispersion(unittest.TestCase):
    def test_get_d(self):
        dists = [
            Distance(10, 11, 1),
            Distance(10, 11, 4),
            Distance(12, 11, 2),
            Distance(12, 11, 4),
            Distance(1, 2, 2),
        ]
        for ad in get_distance_dispersion(dists):
            self.assertIn(ad,
                [
                    Distance(10,11, (1.5**2 + 1.5**2) / 2.0),
                    Distance(12,11, 1),
                    Distance(1,2, 0)
                ]
            )

    def test_get_d_count(self):
        dists = [
            Distance(10, 11, 1),
            Distance(10, 11, 4),
            Distance(12, 11, 2),
            Distance(12, 11, 4),
            Distance(1, 2, 2),
        ]
        self.assertEqual(3, len(get_distance_dispersion(dists)))