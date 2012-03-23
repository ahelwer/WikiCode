import unittest

from string_algo.naive_algorithm import string_search as naive
from string_algo.z_algorithm import string_search as zmatch
from string_algo.boyer_moore import string_search as bm
from string_algo.knuth_morris_pratt import string_search as kmp

class GeneralSimpleMatching(unittest.TestCase):

    def check_all(self, P, T, expected):
        self.longMessage = True
        info = 'P - \"%s\", T - \"%s\", Algorithm - ' %(P, T)
        self.assertEqual(expected, naive(P, T), msg=info+'Naive')
        self.assertEqual(expected, zmatch(P, T), msg=info+'Z-Algorithm')
        self.assertEqual(expected, bm(P, T), msg=info+'Boyer-Moore')
        self.assertEqual(expected, kmp(P, T), msg=info+'Knuth-Morris-Pratt')

    def test_finds_match(self):
        P = 'foo'
        T = 'barfoobar'
        expected = [3]
        self.check_all(P, T, expected)

    def test_no_matches(self):
        P = 'abcdefg'
        T = 'hijklmnopqrstuvwxyz'
        expected = []
        self.check_all(P, T, expected)

    def test_near_matches(self):
        P = 'abcdefg'
        T = 'fooabcdefbcdefgfoo'
        expected = []
        self.check_all(P, T, expected)

    def test_identical_chars(self):
        P = 'aaaa'
        T = 'aaaaaaaa'
        expected = [0,1,2,3,4]
        self.check_all(P, T, expected)

    def test_overlapping_matches(self):
        P = 'aaba'
        T = 'xaabaabaaabax'
        expected = [1,4,8]
        self.check_all(P, T, expected)

    def test_match_at_start_and_end(self):
        P = 'foo'
        T = 'foobarfoo'
        expected = [0,6]
        self.check_all(P, T, expected)

    def test_shorter_text(self):
        P = 'foobar'
        T = 'foo'
        expected = []
        self.check_all(P, T, expected)

    def test_empty_strings(self):
        P = ''
        T = 'foobar'
        expected = []
        self.check_all(P, T, expected)
        P = 'foobar'
        T = ''
        expected = []
        self.check_all(P, T, expected)

    def test_single_char_match(self):
        P = 'a'
        T = 'a'
        expected = [0]
        self.check_all(P, T, expected)

    def test_single_char_mismatch(self):
        P = 'a'
        T = 'b'
        expected = []
        self.check_all(P, T, expected)

    def test_two_char_text(self):
        P = 'a'
        T = 'ab'
        expected = [0]
        self.check_all(P, T, expected)
        P = 'a'
        T = 'ba'
        expected = [1]
        self.check_all(P, T, expected)
        P = 'a'
        T = 'bb'
        expected = []
        self.check_all(P, T, expected)
        P = ''
        T = 'bb'
        expected = []
        self.check_all(P, T, expected)

