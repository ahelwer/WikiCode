# Algorithms on Strings, Trees, and Sequences
# Computer Science and Computational Biology
# By Dan Gusfield
# Chapter 1 - Exact Matching: Fundamental Preprocessing and First Algorithms
# Andrew Helwer, March 2012

from string_algo.z_algorithm import fundamental_preprocess

# Returns indices of exact matches of p in t
def ExactMatchSearch(p, t):
    s = p + '$' + t
    z = fundamental_preprocess(s)
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
    z = fundamental_preprocess(s)
    return any(x == len(p) for x in z)

# [EXERCISE 1-2]
# Returns whether p is a substring of a rotation of t
def IsCyclicSubstring(p, t):
    s = p + '$' + t + t
    z = fundamental_preprocess(s)
    return any(x == len(p) for x in z)

# [EXERCISE 1-3]
# Returns the longest suffix of t that matches a prefix of p
def LongestPrefixSuffixMatch(p, t):
    s = p + '$' + t
    z = fundamental_preprocess(s)
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

