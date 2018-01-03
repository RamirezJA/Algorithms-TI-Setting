def anagram(s1, s2):
    #converting both strings into lists
    s1 = list(s1)
    s2 = list(s2)
    #sorting the elements of the list
    return sorted(s1) == sorted(s2)

def Question1(t, s):
    #uses built-in any to check if any anagram of t is substring of s
    return any(anagram(s[i: i+len(t)], t)
                 for i in range(len(s)-len(t)+ 1))

# Test case 1 checking for anagram in subject
print Question1("ad", "udacity")
#True

# Test case 2 using words not in subject
print Question1("qwr", "udacity")
#False

# Test case 3 using a word longer than the subject
print Question1("cityadunreal", "udacity")
#False

# Test case 4 using words in subject but not in order
print Question1("uiy", "udacity")
#False

# Test case 5 with empty string
print Question1("", "udacity")
#True
