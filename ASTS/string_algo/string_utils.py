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
        return len(S) - idx1
    match_count = 0
    while idx1 < len(S) and idx2 < len(S) and S[idx1] == S[idx2]:
        match_count += 1
        idx1 += 1
        idx2 += 1
    return match_count

