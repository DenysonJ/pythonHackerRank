from collections import Counter

def couldBePalindrome(s):
    add = sum([i%2 for i in  Counter(s).values()])
    return "NO" if add > 1 else "YES"


