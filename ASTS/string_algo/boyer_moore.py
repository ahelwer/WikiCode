from string_algo.string_utils import fundamental_preprocess, alphabet_index

def build_good_suffix_table(s):
    l = [0 for c in s]
    s_reverse = s[::-1] # This reverses a string in Python. True story.
    n = fundamental_preprocess(s_reverse)
    n.reverse()
    for j in range(0, len(s)-1):
        i = len(s) - n[j]
        if i != len(s):
            l[i] = j + 1
    return l

def build_match_table(s):
    l = [0 for c in s]
    z = fundamental_preprocess(s)
    longest = 0
    for i in range(len(z)-1, -1, -1):
        longest = max(z[i], longest) if z[i] + i == len(z) else longest
        l[i] = longest
    return longest

def build_character_table(s):
    r = [[] for c in ALPHABET]
    for i, c in enumerate(s):
        r[alphabet_index(c)].append(i)
    return r

"""
Implementation of the Boyer-Moore string search algorithm. This finds all occurrences of P
in T, and incorporates numerous ways of pre-processing the pattern to determine the optimal 
amount to shift the string and skip comparisons. In practice it runs in O(m) (and even 
sublinear) time, where m is the length of T.
"""
def string_search(p, t):
    matches = []
    # Preprocessing
    L = build_good_suffix_table(p)
    l = build_match_table(p)
    R = build_character_table(p)

    k = len(p) - 1 # Represents shift position of p relative to t
    while k < len(t):
        i = len(p) - 1
        h = k
        while i > 0 and p[i] == t[h]: # Matches p and t from end of p
            i -= 1
            h -= 1
        if i == 0: # Match has been found
            matches.append(k - (len(p) - 1))
            k += len(p) - l[1]
        else: # No match, shift by max of bad character and good suffix rules
            char_matches = [idx for idx in R[alphabet_index(t[h])] if idx < i]
            char_shift = i - char_matches[-1] if char_matches != [] else 1
            suffix_shift = L[i] 
            k += max(char_shift, suffix_shift)
