# Returns the length of the prefix match of s[idx1:] and s[idx2:]
def match_length(s, idx1, idx2):
    if idx1 == idx2:
        return len(s)
    match_count = 0
    while idx1 < len(s) and idx2 < len(s):
        if s[idx1] != s[idx2]:
            return match_count
        match_count += 1
        idx1 += 1
        idx2 += 1
    return match_count

# Performs the fundamental pre-processing on s
def pre_process(s):
    z = [0 for x in s]
    z[0] = len(s)
    z[1] = match_length(s, 0, 1)
    for i in range(2, 2+z[1]): # Optimization from exercise 1-5
        z[i] = z[1]-i+1
    l = 0
    r = 0
    for i in range(2+z[1], len(s)):
        if i <= r:
            k = i-l
            b = z[k]
            a = r-i+1
            if b < a:
                z[i] = b
            elif b > a: # Optimization from exercise 1-6
                z[i] = b
                l = i
                r = i+z[i]-1
            else:
                z[i] = b+match_length(s, a, r+1)
                l = i
                r = i+z[i]-1
        else:
            z[i] = match_length(s, 0, i)
            if z[i] > 0:
                l = i
                r = i+z[i]-1
    return z
