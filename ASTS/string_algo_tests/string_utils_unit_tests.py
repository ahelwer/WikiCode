import unittest

from string_algo.string_utils import match_length, alphabet_index

class MatchLengthTests(unittest.TestCase):

    def check(self, S, idx1, idx2, expected):
        self.longMessage = True
        info = 'S - \"%s\", idx1 - %d, idx2 - %d' %(S, idx1, idx2)
        self.assertEqual(expected, match_length(S, idx1, idx2), msg=info)

    def test_guaranteed_match(self):
        S = 'foobarfoobar'
        for i in range(len(S)):
            self.check(S, i, i, len(S)-i)

    def test_basic_match(self):
        S = 'afoobfooc'
        self.check(S, 1, 5, 3)

    def test_no_match(self):
        S = 'foobarasdf'
        self.check(S, 0, 6, 0)
        
    def test_suffix_prefix_match(self):
        S = 'foobarfoobar'
        self.check(S, 0, 6, 6)

    def test_overlap_match(self):
        S = 'xaabaabax'
        self.check(S, 1, 4, 4)

class AlphabetIndexTests(unittest.TestCase):

    def setUp(self):
        self.alpha = 'abcdefghijklmnopqrstuvwxyz'

    def test_lowercase(self):
        for i in range(26):
            self.assertEqual(i, alphabet_index(self.alpha[i]))

    def test_uppercase(self):
        for i in range(26):
            self.assertEqual(i, alphabet_index(self.alpha[i].upper()))

