def anagram(s1, s2):
    s1 = list(s1)
    s2 = list(s2)
    s1.sort()
    s2.sort()
    return sorted(s1) == sorted(s2)

def Question1(t, s):
    t_len = len(t)
    s_len = len(s)
    t_sort = sorted(t)
    return any(anagram(s[i: i+len(t)], t)
                 for i in range(len(s)-len(t)+ 1))

print Question1("ad", "udacity")
