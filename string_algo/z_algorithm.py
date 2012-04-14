from string_algo.string_utils import match_length

"""
Returns Z, the Fundamental Preprocessing of S. Z[i] is the length of the substring 
beginning at i which is also a prefix of S. This pre-processing is done in O(n) time,
where n is the length of S.
"""
def fundamental_preprocess(S):
    if len(S) == 0: # Handles case of empty string
        return []
    if len(S) == 1: # Handles case of single-character string
        return [1]
    z = [0 for x in S]
    z[0] = len(S)
    z[1] = match_length(S, 0, 1)
    for i in range(2, 1+z[1]): # Optimization from exercise 1-5
        z[i] = z[1]-i+1
    # Defines lower and upper limits of z-box
    l = 0
    r = 0
    for i in range(2+z[1], len(S)):
        if i <= r: # i falls within existing z-box
            k = i-l
            b = z[k]
            a = r-i+1
            if b < a: # b ends within existing z-box
                z[i] = b
            elif b > a: # Optimization from exercise 1-6
                z[i] = min(b, len(S)-i)
                l = i
                r = i+z[i]-1
            else: # b ends exactly at end of existing z-box
                z[i] = b+match_length(S, a, r+1)
                l = i
                r = i+z[i]-1
        else: # i does not reside within existing z-box
            z[i] = match_length(S, 0, i)
            if z[i] > 0:
                l = i
                r = i+z[i]-1
    return z

"""
Searches for all instances of P in T, using the Z algorithm. By calculating the fundamental
preprocess of the string P$T, where $ is some character assumed not to be in P and T, matches
of P are easily found. The Z-values corresponding to T in P$T are considered, and if their
value is equivalent to the length of P then a match is found at that index.
"""
def string_search(P, T):
    matches = []
    if len(P) == 0 or len(T) < len(P):
        return matches
    S = P + '$' + T
    Z = fundamental_preprocess(S)
    for i in range(len(P)+1, len(S)):
        if Z[i] == len(P):
            matches.append(i-(len(P)+1))
    return matches

