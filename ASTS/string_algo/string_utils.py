"""
Returns the index of the given character in the English alphabet, counting from 0.
"""
def alphabet_index(c):
    return ord(c.lower()) - 97 # 'a' is ASCII character 97

"""
Returns the length of the match of the substrings of S beginning at idx1 and idx2.
"""
def match_length(S, idx1, idx2):
    if idx1 == idx2:
        return len(S)
    match_count = 0
    while idx1 < len(S) and idx2 < len(S) and S[idx1] == S[idx2]:
        match_count += 1
        idx1 += 1
        idx2 += 1
    return match_count

"""
Returns Z, the Fundamental Preprocessing of S. Z[i] is the length of the substring 
beginning at i which is also a prefix of S. This pre-processing is done in O(n) time,
where n is the length of S.
"""
def fundamental_preprocess(S):
    z = [0 for x in S]
    z[0] = len(S)
    z[1] = match_length(S, 0, 1)
    for i in range(2, 2+z[1]): # Optimization from exercise 1-5
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
                z[i] = b
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
