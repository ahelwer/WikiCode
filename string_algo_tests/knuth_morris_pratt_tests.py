import unittest

from string_algo.knuth_morris_pratt import build_sp

class SpTests(unittest.TestCase):

    def test_no_suffix_prefix_match(self):
        S = 'abcdefgh'
        expected = [0,0,0,0,0,0,0,0]
        self.assertEqual(expected, build_sp(S))

    def test_single_suffix_prefix_match(self):
        S = 'abcdabcd'
        expected = [0,0,0,0,0,0,0,4]
        self.assertEqual(expected, build_sp(S))

    def test_multiple_suffix_match(self):
        S = 'abxabyab'
        expected = [0,0,0,0,2,0,0,2]
        self.assertEqual(expected, build_sp(S))

    def test_overlapping_match(self):
        S = 'aabaxaabaaba'
        expected = [0,1,0,1,0,0,1,0,4,1,0,4]
        self.assertEqual(expected, build_sp(S))

    def test_empty_string(self):
        self.assertEqual([], build_sp(''))

    def test_single_character(self):
        self.assertEqual([0], build_sp('a'))

