from fundamental_preprocessing import pre_process

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def build_good_suffix_table(s):
    l = [0 for c in s]
    s_reverse = s[::-1] # This reverses a string in Python. True story.
    n = pre_process(s_reverse)
    n.reverse()
    for j in range(0, len(s)-1):
        i = len(s) - n[j] + 1
        l[i] = j
    return l

def build_match_table(s):
    l = [0 for c in s]
    z = pre_process(s)
    longest = 0
    for i in range(len(z)-1, -1, -1):
        longest = max(z[i], longest) if z[i] + i == len(z) else longest
        l[i] = longest
    return longest

def build_character_table(s):
    r = [[] for c in ALPHABET]
    for i, c in enumerate(s):
        r[ALPHABET.index(c)].append(i)
    return r

