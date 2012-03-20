from string_algo.string_utils import fundamental_preprocess, alphabet_index

"""
Generates R for S, which is an array indexed by the position of some character c in the 
English alphabet. At that index in R is an array of length |S|+1, specifying for each
index i in S (plus the index after S) the next location of character c encountered when
traversing S from right to left starting at i. This is used for a constant-time lookup
for the bad character rule in the Boyer-Moore string search algorithm, although it has
a much larger size than non-constant-time solutions.
"""
def bad_character_table(S):
    R = [[0] for a in range(26)]
    alpha = [0 for a in range(26)]
    for i, c in enumerate(S):
        alpha[alphabet_index(c)] = i
        for j, a in enumerate(alpha):
            R[j].append(a)
    return R

"""
Generates L for S, an array used in the implementation of the strong good suffix rule.
L[i] = k, the largest position in S such that S[i:] (the suffix of S starting at i) matches
a suffix of S[:k] (a substring in S ending at k). Used in Boyer-Moore, L gives an amount to
shift P relative to T such that no instances of P in T are skipped and a suffix of P[:L[i]]
matches the substring of T matched by a suffix of P in the previous match attempt.
Specifically, if the mismatch took place at position i in P, the shift magnitude is given
by the equation len(P) - L[i]. In the case that L[i] = 0, the full shift table is used.
"""
def good_suffix_table(S):
    L = [0 for c in S]
    N = fundamental_preprocess(S[::-1]) # S[::-1] reverses S
    N.reverse()
    for j in range(0, len(S)-1):
        i = len(S) - N[j]
        if i != len(S):
            L[i] = j
    return L

"""
Generates K for S, an array used in a special case of the good suffix rule in the Boyer-Moore
string search algorithm. K[i] is the length of the longest suffix of S[i:] that is also a
prefix of S. In the cases it is used, the shift magnitude of the pattern P relative to the
text T is len(P) - K[i] for a mismatch occurring at i.
"""
def full_shift_table(S):
    K = [0 for c in S]
    Z = fundamental_preprocess(S)
    longest = 0
    for i, zv in enumerate(reversed(Z)):
        longest = max(zv, longest) if zv == i+1 else longest
        K[-i-1] = longest
    K[0] = K[1]
    return K

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
