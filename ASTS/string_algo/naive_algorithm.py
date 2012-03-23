"""
Implements the naive algorithm for finding all occurrences of P in T. This simply aligns
P with a certain index of T, checks if a match occurs, then shifts the alignment to the
right by a single character.
"""
def string_search(P, T):
    if len(P) == 0 or len(T) == 0 or len(T) < len(P):
        return []
    matches = []
    k = 0 # Alignment of P relative to T
    while k+len(P) <= len(T):
        i = 0 # Index to be compared
        while i < len(P) and P[i] == T[k+i]: 
            i += 1
        if i == len(P): # Match found
            matches.append(k)
        k += 1
    return matches

