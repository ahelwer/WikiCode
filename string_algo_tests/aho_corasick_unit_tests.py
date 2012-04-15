import unittest
from string_algo.aho_corasick import construct_pattern_trie
from string_algo.aho_corasick import link_pattern_trie

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

class LinkPatternTrieTests(unittest.TestCase):

    def follow_path(self, root, string):
        current = root
        for c in string:
            current = current.edges[c]
        return current

    def test_base_case(self):
        pattern_list = ['a', 'b', 'c']
        root = link_pattern_trie(construct_pattern_trie(pattern_list))
        self.assertEqual(root, root.failure_link)
        self.assertEqual(None, root.output_link)
        for c in pattern_list:
            self.assertEqual(root, root.edges[c].failure_link)
            self.assertEqual(None, root.edges[c].output_link)

    def test_repeated_char(self):
        pattern = 'aaaaaa'
        root = link_pattern_trie(construct_pattern_trie([pattern]))
        current = root
        for c in pattern:
            nxt = current.edges[c]
            self.assertEqual(None, current.output_link)
            self.assertEqual(current, nxt.failure_link)
        
    def test_eclipsing_patterns(self):
        pattern_list = ['aaaaa', 'aaaa', 'aaa', 'aa', 'a']
        root = link_pattern_trie(construct_pattern_trie(pattern_list))
        current = root.edges['a']
        self.assertEqual(root, current.failure_link)
        self.assertEqual(None, current.output_link)
        for c in 'aaaa':
            nxt = current.edges[c]
            self.assertEqual(current, nxt.failure_link)
            self.assertEqual(current, nxt.output_link)

    def test_split_patterns(self):
        pattern_list = ['ab', 'b']
        root = link_pattern_trie(construct_pattern_trie(pattern_list))
        a_node = root.edges['a']
        b_node = root.edges['b']
        self.assertEqual(b_node, a_node.edges['b'].failure_link)
        self.assertEqual(b_node, a_node.edges['b'].output_link)

    def test_long_output_path(self):
        pattern_list = ['b', 'abb', 'aab']
        root = link_pattern_trie(construct_pattern_trie(pattern_list))
        end_node = self.follow_path(root, 'aab')
        mid_node = self.follow_path(root, 'ab')
        start_node = self.follow_path(root, 'b')
        self.assertEqual(mid_node, end_node.failure_link)
        self.assertEqual(start_node, mid_node.failure_link)
        self.assertEqual(start_node, mid_node.output_link)
        self.assertEqual(start_node, end_node.output_link)

