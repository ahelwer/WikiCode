from string_algo.z_algorithm import fundamental_preprocess
from string_algo.string_utils import alphabet_index

"""
Generates R for S, which is an array indexed by the position of some character c in the 
English alphabet. At that index in R is an array of length |S|+1, specifying for each
index i in S (plus the index after S) the next location of character c encountered when
traversing S from right to left starting at i. This is used for a constant-time lookup
for the bad character rule in the Boyer-Moore string search algorithm, although it has
a much larger size than non-constant-time solutions.
"""
def bad_character_table(S):
    if len(S) == 0:
        return [[] for a in range(26)]
    R = [[-1] for a in range(26)]
    alpha = [-1 for a in range(26)]
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
Specifically, if the mismatch took place at position i-1 in P, the shift magnitude is given
by the equation len(P) - L[i]. In the case that L[i] = -1, the full shift table is used.
Since only proper suffixes matter, L[0] = -1.
"""
def good_suffix_table(S):
    L = [-1 for c in S]
    N = fundamental_preprocess(S[::-1]) # S[::-1] reverses S
    N.reverse()
    for j in range(0, len(S)-1):
        i = len(S) - N[j]
        if i != len(S):
            L[i] = j
    return L

"""
Generates F for S, an array used in a special case of the good suffix rule in the Boyer-Moore
string search algorithm. F[i] is the length of the longest suffix of S[i:] that is also a
prefix of S. In the cases it is used, the shift magnitude of the pattern P relative to the
text T is len(P) - F[i] for a mismatch occurring at i-1.
"""
def full_shift_table(S):
    F = [0 for c in S]
    Z = fundamental_preprocess(S)
    longest = 0
    for i, zv in enumerate(reversed(Z)):
        longest = max(zv, longest) if zv == i+1 else longest
        F[-i-1] = longest
    return F

"""
Implementation of the Boyer-Moore string search algorithm. This finds all occurrences of P
in T, and incorporates numerous ways of pre-processing the pattern to determine the optimal 
amount to shift the string and skip comparisons. In practice it runs in O(m) (and even 
sublinear) time, where m is the length of T.
"""
def string_search(P, T):
    if len(P) == 0 or len(T) == 0 or len(T) < len(P):
        return []

    matches = []

    # Preprocessing
    R = bad_character_table(P)
    L = good_suffix_table(P)
    F = full_shift_table(P)

    k = len(P) - 1      # Represents alignment of end of P relative to T
    while k < len(T):
        i = len(P) - 1  # Character to compare in P
        h = k           # Character to compare in T
        while i >= 0 and P[i] == T[h]:   # Matches starting from end of P
            i -= 1
            h -= 1
        if i == -1: # Match has been found
            matches.append(k - len(P) + 1)
            k += len(P)-F[1] if len(P) > 1 else 1
        else:   # No match, shift by max of bad character and good suffix rules
            char_shift = i - R[alphabet_index(T[h])][i]
            if i+1 == len(P):   # Mismatch happened on first attempt
                suffix_shift = 1
            elif L[i+1] == -1:   # Matched suffix does not appear anywhere in P
                suffix_shift = len(P) - F[i+1]
            else:               # Matched suffix appears in P
                suffix_shift = len(P) - L[i+1]
            k += max(char_shift, suffix_shift)
    return matches

