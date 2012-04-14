from string_algo.boyer_moore import bad_character_table
from string_algo.boyer_moore import good_suffix_table
from string_algo.boyer_moore import full_shift_table
from string_algo.z_algorithm import fundamental_preprocess
from string_algo.string_utils import alphabet_index

"""
Implementation of the Apostolico-Giancarlo string search algorithm. This algorithm emulates
the functionality of the Boyer-Moore algorithm exactly, but has a simple proof for a linear
time bound due to the inclusion of an extra table which records for each index in T the
length of the suffix match with P ending at that point. With this data in conjunction with
extra data recorded during the preprocessing of P, many of the actual character comparisons
can be skipped when checking whether an alignment of P to T results in a match.
"""
def string_search(P, T):
    if len(P) == 0 or len(T) < len(P):
        return []

    matches = []

    # Preprocessing
    N = fundamental_preprocess(T[::-1]) # S[::-1] reverses S
    N.reverse()
    R = bad_character_table(P)
    L = good_suffix_table(P)
    F = full_shift_table(P)
    M = [-1 for c in T]

    k = len(P) - 1      # Represents alignment of end of P relative to T
    i = len(P) - 1      # Character to compare in P
    h = k               # Character to compare in T
    match = False       # Indicates whether an exact match has been found in this phase
    mismatch = False    # Indicates whether a mismatch has occurred

    while k < len(T):
        if M[h] == -1 or M[h] == 0 or N[i] == 0:    # Phase case 1
            #print 'Case 1'
            if T[h] == P[i]: 
                if i == 0:  # Case 1a
                    match = True
                    mismatch = False
                else:       # Case 1b
                    i -= 1
                    h -= 1
                    match = False
                    mismatch = False
            else:           # Case 1c
                match = False
                mismatch = True
        elif (M[h] < N[i] and M[h] != -1) or (M[h] == N[i] and 0 < N[i] < i+1): # Case 2 & 5
            #print 'Case 2 & 5'
            i -= M[h]
            h -= M[h]
            match = False
            mismatch = False
        elif M[h] >= N[i] and N[i] == i+1 > 0:  # Phase case 3
            #print 'Case 3'
            match = True 
            mismatch = False
        elif M[h] > N[i] and N[i] < i+1:    # Phase case 4
            #print 'Case 4'
            i -= N[i]
            h -= N[i]
            match = False
            mismatch = True
        if match:
            matches.append(k - len(P) + 1)
            M[k] = k - h
            k += len(P)-F[1] if len(P) > 1 else 1
            i = len(P) - 1
            h = k
            match = False
            mismatch = False
        if mismatch:
            char_shift = i - R[alphabet_index(T[h])][i]
            if i+1 == len(P):   # Mismatch happened on first attempt
                suffix_shift = 1
            elif L[i+1] == -1:   # Matched suffix does not appear anywhere in P
                suffix_shift = len(P) - F[i+1]
            else:               # Matched suffix appears in P
                suffix_shift = len(P) - L[i+1]
            M[k] = k - h
            k += max(char_shift, suffix_shift)
            i = len(P) - 1
            h = k
            match = False
            mismatch = False
    return matches

