from string_algo.z_algorithm import fundamental_preprocess

"""
Returns sp, where the ith element of sp is the length of the longest substring ending
at i which is also a prefix of P. This is useful to determine the amount to shift the
pattern in the Knuth-Morris-Pratt string search algorithm.
"""
def build_sp(P):
    sp = [0 for x in P]
    Z = fundamental_preprocess(P)
    for j in range(len(P)-1, 0, -1):
        i = j + Z[j] - 1
        sp[i] = Z[j]
    return sp

"""
Implementation of the Knuth-Morris-Pratt string search algorithm. This finds all
occurrences of P in T in O(n + m) time, where n is the length of P and m is the length
of T. This is not the real-time version of the algorithm; some indices in T (specifically,
the indices at which a mismatch occurs) will be checked twice, leading to at most 2m 
comparisons in the worst case.
"""
def string_search(P, T):
    matches = []
    if len(P) == 0 or len(T) < len(P):
        return matches
    sp = build_sp(P)
    c = 0 # Character to inspect in T
    p = 0 # Character to start matching at in P
    while c + len(P)-p-1 < len(T):
        # Matches alignment of P to T until failure or end of P
        while p < len(P) and P[p] == T[c]:
            c += 1
            p += 1
        if p == len(P): # Match found
            matches.append(c - len(P))
        if p == 0:
            c += 1 # Shifts c in case of immediate match failure
        else:  
            p = sp[p-1] # Sets p so prefix is not redundantly checked
    return matches

