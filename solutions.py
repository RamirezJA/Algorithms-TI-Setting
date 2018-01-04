#Question 1
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

#Question 2
#creates an empty dictionary
store = {}
def question2(string):
    if string in store.keys():
        return store[string]
    #returns string if its a palindrome
    if string == string[::-1]:
        return string
    else:
        #goes trough string items from left to right
        left = question2(string[:-1])
        right = question2(string[1:])
        iterate = [left, right]
        #finding max using len
        store[string] = max(iterate, key=len) 
        return store[string]
 
print question2('forgeeksskeegfor')
print question2('alskdjfj laksjd flkajs racecar idk lol')

# http://codegist.net/code/find-longest-palindrome-in-a-store-python/
