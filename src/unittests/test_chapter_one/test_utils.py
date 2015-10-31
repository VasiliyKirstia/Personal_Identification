__author__ = 'vasiliy'
from chapter_one.utils import get_average_outer_distance, get_average_inner_distance, get_inner_distance_dispersion, \
    get_outer_distance_sequence, get_outer_distance_dispersion, get_inner_distance_sequence
from chapter_one.models import InnerDistance, OuterDistance
from models import Input
import unittest

class TestGetInnerDistanceSequence(unittest.TestCase):
    def test_get_i_d(self):
        inputs = [
            Input(10, 1, 3),
            Input(11, 2.1, 4)
        ]
        self.assertEqual(
            get_inner_distance_sequence(inputs),
            [
                InnerDistance(10, 2),
                InnerDistance(11, 1.9)
            ]
        )

class TestGetAverageInnerDistance(unittest.TestCase):
    def test_get_a(self):
        ids = [
            InnerDistance(1, 1),
            InnerDistance(2, 2),
            InnerDistance(3, 4),
            InnerDistance(2, 2),
            InnerDistance(2, 2),
            InnerDistance(1, 2),
            InnerDistance(1, 2)
        ]
        self.assertEqual(
            get_average_inner_distance(ids),
            [
                InnerDistance(1, 5/3.0),
                InnerDistance(2, 2),
                InnerDistance(3, 4)
            ]
        )
class TestGetOuterDistanceSequence(unittest.TestCase):
    def test_get_dist(self):
        inputs = [
            Input(10, 1, 3),
            Input(11, 2, 4),
            Input(12, 6, 8)
        ]
        self.assertEqual(
            get_outer_distance_sequence(inputs),
            [
                OuterDistance(10, 11, -1),
                OuterDistance(11, 12, 2)
            ]
        )

class TestGetAverageOuterDistance(unittest.TestCase):
    def test_get_a(self):
        dists = [
            OuterDistance(10, 11, 2),
            OuterDistance(10, 11, 4),
            OuterDistance(12, 11, 2),
            OuterDistance(12, 11, 4),
            OuterDistance(1, 2, 2),
        ]
        for item in get_average_outer_distance(dists):
            self.assertIn(
                item,
                [
                    OuterDistance(10,11,3),
                    OuterDistance(12,11,3),
                    OuterDistance(1,2,2)
                ]
            )
    def test_get_a_o_d_count(self):
        dists = [
            OuterDistance(10, 11, 2),
            OuterDistance(10, 11, 4),
            OuterDistance(12, 11, 2),
            OuterDistance(12, 11, 4),
            OuterDistance(1, 2, 2),
        ]
        self.assertEqual(3 , len(get_average_outer_distance(dists)))

class TestGetInnerDistanceDispersion(unittest.TestCase):
    def test_get_i_d(self):
        ids = [
            InnerDistance(1, 1),
            InnerDistance(2, 2),
            InnerDistance(3, 4),
            InnerDistance(2, 2),
            InnerDistance(2, 2),
            InnerDistance(1, 2),
            InnerDistance(1, 2)
        ]
        self.assertEqual(
            get_inner_distance_dispersion(ids),
            [
                InnerDistance(1, ( (1-5/3.0)**2 + (2-5/3.0)**2 + (2-5/3.0)**2 )/3.0),
                InnerDistance(2, 0),
                InnerDistance(3, 0)
            ]
        )

class TestGetOuterDistanceDispersion(unittest.TestCase):
    def test_get_odd(self):
        dists = [
            OuterDistance(10, 11, 1),
            OuterDistance(10, 11, 4),
            OuterDistance(12, 11, 2),
            OuterDistance(12, 11, 4),
            OuterDistance(1, 2, 2),
        ]
        for odd in get_outer_distance_dispersion(dists):
            self.assertIn(odd,
                [
                    OuterDistance(10,11, (1.5**2 + 1.5**2) / 2.0),
                    OuterDistance(12,11, 1),
                    OuterDistance(1,2, 0)
                ]
            )

    def test_get_odd_count(self):
        dists = [
            OuterDistance(10, 11, 1),
            OuterDistance(10, 11, 4),
            OuterDistance(12, 11, 2),
            OuterDistance(12, 11, 4),
            OuterDistance(1, 2, 2),
        ]
        self.assertEqual(3, len(get_outer_distance_dispersion(dists)))