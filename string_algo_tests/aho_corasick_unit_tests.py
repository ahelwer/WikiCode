import unittest
from string_algo.aho_corasick import construct_pattern_trie

class ConstructPatternTrieTests(unittest.TestCase):

    def deconstruct_pattern_trie(self, current, word=[]):
        patterns = []
        for i in current.patterns:
            patterns.append(''.join(word))
        for c, child in current.edges.iteritems():
            word.append(c)
            patterns.extend(self.deconstruct_pattern_trie(child, word))
            word.pop()
        return patterns

    def test_empty_set(self):
        root = construct_pattern_trie([])
        self.assertEqual(0, len(root.edges))
        self.assertEqual(0, len(root.patterns))

    def test_empty_strings(self):
        pattern_list = ['','','','']
        root = construct_pattern_trie(pattern_list)
        self.assertEqual(0, len(root.edges))
        self.assertEqual(0, len(root.patterns))

    def test_single_pattern(self):
        pattern = 'aabaaba'
        root = construct_pattern_trie([pattern])
        current = root
        for c in pattern:
            self.assertTrue(c in current.edges)
            self.assertEqual(1, len(current.edges))
            current = current.edges[c]
        self.assertEqual(1, len(current.patterns))
        self.assertEqual(0, current.patterns[0]) 

    def test_distinct_chars(self):
        pattern_list = ['a', 'b', 'c', 'd']
        root = construct_pattern_trie(pattern_list)
        self.assertEqual(len(pattern_list), len(root.edges))
        for i, c in enumerate(pattern_list):
            self.assertTrue(c in root.edges)
            self.assertEqual(1, len(root.edges[c].patterns))
            self.assertEqual(i, root.edges[c].patterns[0])
            self.assertEqual(0, len(root.edges[c].edges))

    def test_identical_chars(self):
        pattern_list = ['a', 'a', 'a', 'a']
        root = construct_pattern_trie(pattern_list)
        self.assertEqual(1, len(root.edges))
        self.assertTrue('a' in root.edges)
        self.assertEqual([0,1,2,3], root.edges['a'].patterns)
        self.assertEqual(0, len(root.edges['a'].edges))

    def test_prefix_match(self):
        pattern_list = ['ab', 'ac']
        root = construct_pattern_trie(pattern_list)
        self.assertEqual(1, len(root.edges)) 
        self.assertTrue('a' in root.edges)
        branch = root.edges['a']
        self.assertEqual(2, len(branch.edges))
        self.assertTrue('b' in branch.edges)
        self.assertTrue('c' in branch.edges)
        self.assertEqual(0, len(branch.edges['b'].edges))
        self.assertEqual(0, len(branch.edges['c'].edges))
        self.assertEqual(1, len(branch.edges['b'].patterns))
        self.assertEqual(1, len(branch.edges['c'].patterns))
        self.assertEqual(0, branch.edges['b'].patterns[0])
        self.assertEqual(1, branch.edges['c'].patterns[0])

    def test_distinct_patterns(self):
        pattern_list = ['aaba', 'foo', 'bar']
        pattern_list.sort()
        root = construct_pattern_trie(pattern_list)
        self.assertEqual(pattern_list, self.deconstruct_pattern_trie(root))

    def test_eclipsing_patterns(self):
        pattern_list = ['ab', 'a']
        root = construct_pattern_trie(pattern_list)
        self.assertEqual(1, len(root.edges)) 
        self.assertTrue('a' in root.edges)
        nxt = root.edges['a']
        self.assertEqual([1], nxt.patterns)
        self.assertEqual(1, len(nxt.edges)) 
        self.assertTrue('b' in nxt.edges)
        nxt = nxt.edges['b']
        self.assertEqual([0], nxt.patterns)
        self.assertEqual(0, len(nxt.edges)) 

    def test_matching_patterns(self):
        pattern_list = ['aaba', 'aaba']
        root = construct_pattern_trie(pattern_list)
        current = root
        for c in 'aaba':
            self.assertEqual(1, len(current.edges))
            self.assertTrue(c in current.edges)
            current = current.edges[c]
        self.assertEqual([0,1], current.patterns)

    def test_intersecting_patterns(self):
        pattern_list = ['aaba', 'aabaaa', 'abba', 'aba', 'baa', 'bab']
        pattern_list.sort()
        root = construct_pattern_trie(pattern_list)
        self.assertEqual(pattern_list, self.deconstruct_pattern_trie(root))

