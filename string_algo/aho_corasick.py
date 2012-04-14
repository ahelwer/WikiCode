
"""
Trie node class for Aho-Corasick algorithm.
    edges - dictionary for storing edges to other nodes
    patterns - list of patterns ending at this node
    failure_link - see definition given in link_pattern_trie function documentation
    output_link - see definition given in link_pattern_trie function documentation
"""
class Node():
    def __init__(self):
        self.edges = {}
        self.patterns = []
        self.failure_link = None
        self.output_link = None

"""
Constructs a trie out of the given pattern list. A trie is a tree data structure with
a single character on each edge. It is implemented using the Node class above. No node may 
have two edges coming from it both labelled with the same character, so patterns which
share a prefix also share an edge path equivalent to that prefix. Apart from its use in
the Aho-Corasick algorithm, constructing such a trie for a set of strings provides for
very efficient determination of membership in that set of strings.
"""
def construct_pattern_trie(pattern_list):
    root = Node()
    for i, P in enumerate(pattern_list):
        current = root
        for c in P:
            if c not in current.edges:
                current.edges[c] = Node()
            current = current.edges[c]
        if len(P) != 0:     # Skips adding the empty string
            current.patterns.append(i)
    return root

"""
Let the function lv(N) return the string formed by the concatenation of the characters
along the path from the root to node N. Given the root of a constructed pattern trie, 
link_pattern_trie adds failure and output links to all nodes in the trie. A node U's 
failure link is a reference to a second node V in the trie such that lv(V) is a suffix 
of lv(U), and furthermore is the longest suffix of U among all lv() values in the trie. 
A node U's output link is a reference to the first node ending a pattern that is encountered 
when iteratively following the path of failure links starting at U. If no such node ending 
a pattern exists, U's output link is None.
"""
def link_pattern_trie(root):
    Q = []
    # Base case - root and children of root all link to root
    root.failure_link = root
    for current in root.edges.values():
        current.failure_link = root
        Q.append(current)
    while Q != []:      # Performs a breadth-first search of the trie
        parent = Q.pop(0)
        for c, current in parent.edges.iteritems():
            # Finds failure_link
            failure_node = parent.failure_link
            while c not in failure_node.edges and failure_node != root:
                failure_node = failure_node.failure_link
            current.failure_link = failure_node.edges[c] if c in failure_node.edges else root
            # Finds output_link
            if current.failure_link.patterns != []:
                current.output_link = current.failure_link
            else:
                current.ouput_link = current.failure_link.output_link
            Q.append(current)
    return root

"""
Implementation of the Aho-Corasick multi-pattern string matching algorithm. Given a set
of patterns and a text T, this function will find all occurrences of the patterns in T
in O(n+m+k) time, where n is the summed length of the patterns, m is the length of T, and
k is the number of occurrences of the patterns in T. Aho-Corasick works by building a 
trie out of the patterns, then adding failure links to the trie as a generalization of
the failure function found in Knuth-Morris-Pratt. Output links are also added so that
patterns ending in different branches of the trie are not missed when matching.
"""
def pattern_search(pattern_list, T):
    matches = [[] for P in pattern_list]
    if len(T) == 0:
        return matches

    # Preprocessing
    root = link_pattern_trie(construct_pattern_trie(pattern_list))
    idx = 0         # Index in T to be compared
    current = root  # Node in trie to be considered
    while idx < len(T):
        if T[idx] in current.edges:     # Comparison succeeded
            nxt = current.edges[T[idx]]
            output_node = nxt
            # Searches for matches using output_links
            while output_node != None:
                for i in output_node.patterns:
                    matches[i].append(idx - len(pattern_list[i]) + 1)
                output_node = output_node.output_link
            # Moves to next comparison
            current = nxt
            idx += 1
        elif current == root:       # Comparison failed on first character
            idx += 1
        else:                       # Comparison failed - follow failure_link
            current = current.failure_link
    return matches

