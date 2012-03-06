# Algorithms on Strings, Trees, and Sequences
# (Computer Science and Computational Biology)
# By Dan Gusfield
# CHAPTER 1 CONCEPTS AND EXERCISES 
# Andrew Helwer, March 2012

def MatchLength(s1, s2):
    count = 0
    for a, b in zip(s1, s2):
        if a != b:
            return count
        count += 1
    return count

def PreProcessString(s):
    z = [0 for x in s]
    l = 0
    r = 0
    z[0] = len(s)
    z[1] = MatchLength(s, s[1:])
    if z[1] > 0:
        l = 1
        r = z[1]
    for i in range(2, len(s)):
        if i <= r:
            b = z[i-l]
            if b < r-i+1 or r == len(s)-1:
                z[i] = min(b, len(s)-i)
            else:
                q = MatchLength(s[b:], s[r+1:])
                z[i] = b + q
                l = i
                r = i + q - 1
        else:
            q = MatchLength(s, s[i:])
            z[i] = q
            if q > 0:
                l = i
                r = i + q - 1
    return z

# Returns indices of exact matches of p in t
def ExactMatchSearch(p, t):
    s = p + '$' + t
    z = PreProcessString(s)
    matches = []
    for i, x in enumerate(z[len(p)+1:]):
        if x == len(p):
            matches.append(i)
    return matches

# [EXERCISE 1-1]
# Returns whether p is a cyclic rotation of t
def IsCyclicRotation(p, t):
    if len(p) != len(t):
        return False
    s = p + '$' + t + t
    z = PreProcessString(s)
    return any(x == len(p) for x in z)

# [EXERCISE 1-2]
# Returns whether p is a substring of a rotation of t
def IsCyclicSubstring(p, t):
    s = p + '$' + t + t
    z = PreProcessString(s)
    return any(x == len(p) for x in z)

# [EXERCISE 1-3]
# Returns the longest suffix of t that matches a prefix of p
def LongestPrefixSuffixMatch(p, t):
    s = p + '$' + t
    z = PreProcessString(s)
    suffixMatches = []
    for i, x in enumerate(z[len(p)+1:]):
        if x == len(t) - i:
            suffixMatches.append(i)
    return t[min(suffixMatches):]

# [EXERCISE 1-4]
# Returns a list of maximal tandem arrays in t with base p
def MaximalTandemSubarrays(p, t):
    matches = ExactMatchSearch(p, t)
    tandems = []
    while matches != []:
        start = matches[0]
        inTandem = []
        notInTandem = []
        for x in matches:
            if (x - start) % len(p) == 0:
                inTandem.append(x)
            else:
                notInTandem.append(x)
        end = inTandem[-1] + len(p)
        tandems.append((start, end))
        matches = notInTandem
    return tandems

"""
# Preprocessing test
s = 'aabxaacxaabxa'
print 'Pre-processing \"%s\":' %s
print PreProcessString(s)
s = 'aaaaaaaaaaaaaa'
print 'Pre-processing \"%s\":' %s
print PreProcessString(s)

# Matching test
p = 'abxyabxz' 
t = 'xabxyabxyabxzabxyabxz'
print 'Searching for instances of \"%s\" in \"%s\":' %(p, t)
print ExactMatchSearch(p, t)
"""

print '---------------------------------------------------------------------------------'

# Exercise 1-1 - determine if p is a cyclic rotation of t
print '[EXERCISE 1-1] - cyclic rotation equivalence'
p = 'abcdef'
t = 'defabc'
isCyclicRotation = IsCyclicRotation(p, t)
print 'Is \"%s\" a cyclic rotation of \"%s\"? %s' %(t, p, isCyclicRotation)
p = 'abcdeg'
t = 'defabc'
isCyclicRotation = IsCyclicRotation(p, t)
print 'Is \"%s\" a cyclic rotation of \"%s\"? %s' %(t, p, isCyclicRotation)

print '---------------------------------------------------------------------------------'

# Exercise 1-2 - determine if p is a substring of a rotation of t
print '[EXERCISE 1-2] - substring of a cyclic rotation'
p = 'aba'
t = 'adfsdab'
isCyclicSubstring = IsCyclicSubstring(p, t)
print 'Is \"%s\" a substring of a cyclic rotation of \"%s\"? %s' %(p, t, isCyclicSubstring)
p = 'aba'
t = 'dfsdab'
isCyclicSubstring = IsCyclicSubstring(p, t)
print 'Is \"%s\" a substring of a cyclic rotation of \"%s\"? %s' %(p, t, isCyclicSubstring)

print '---------------------------------------------------------------------------------'

# Exercise 1-3 suffix-prefix matching
print '[EXERCISE 1-3] - longest suffix matching a prefix'
p = 'aardvark'
t = 'blahaard'
suffix = LongestPrefixSuffixMatch(p, t)
print 'Longest suffix of \"%s\" that is a prefix of \"%s\": \"%s\"' %(t, p, suffix)
p = 'asdfasdfblah'
t = 'foobarasdfasdf'
suffix = LongestPrefixSuffixMatch(p, t)
print 'Longest suffix of \"%s\" that is a prefix of \"%s\": \"%s\"' %(t, p, suffix)

print '---------------------------------------------------------------------------------'

# Exercise 1-4 - find the maximal tandem subarrays in a text with a given base
print '[EXERCISE 1-4] - maximal tandem subarrays'
p = 'abc'
t = 'xyzabcabcxabcabcpq'
tandems = MaximalTandemSubarrays(p, t)
print 'Maximal tandem subarrays in \"%s\" with base \"%s\": %s' %(t, p, tandems)
p = 'aaba'
t = 'xdaabaaabaabaaabafj'
tandems = MaximalTandemSubarrays(p, t)
print 'Maximal tandem subarrays in \"%s\" with base \"%s\": %s' %(t, p, tandems)

print '---------------------------------------------------------------------------------'

# Exercise 1-5 - special properties of the initial case of the Z algorithm

"""
If Z_{2} = q > 0, then the first q + 1 characters of S must be the same character,
as this is the only string that matches itself when shifted to the right by one place.
Thus Z_{3} .. Z_{q+2} are q-1 .. 0 respectively.
"""


