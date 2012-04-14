import unittest

from string_algo.z_algorithm import fundamental_preprocess

class FundamentalPreprocessTests(unittest.TestCase):

    def test_no_prefix_matches(self):
        S = 'abcdefgh'
        expected = [8,0,0,0,0,0,0,0]
        self.assertEqual(expected, fundamental_preprocess(S))

    def test_single_prefix_match(self):
        S = 'abab'
        expected = [4,0,2,0]
        self.assertEqual(expected, fundamental_preprocess(S))

    def test_multiple_prefix_match(self):
        S = 'aabaacaab'
        expected = [9,1,0,2,1,0,3,1,0]
        self.assertEqual(expected, fundamental_preprocess(S))

    def test_overlapping_prefix_match(self):
        S = 'aabaabaaba'
        expected = [10,1,0,7,1,0,4,1,0,1]
        self.assertEqual(expected, fundamental_preprocess(S))

    def test_character_repeated(self):
        S = 'aaaaaaaa'
        expected = [8,7,6,5,4,3,2,1]
        self.assertEqual(expected, fundamental_preprocess(S))

    def test_empty_string(self):
        self.assertEqual([], fundamental_preprocess(''))

    def test_single_char(self):
        self.assertEqual([1], fundamental_preprocess('a'))

