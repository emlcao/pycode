"""
Q: return the index of the first occurrence of needle in haystack, or -1 if needle is not part of the haystack
Input: string
Output: int
Idea: match needle with stack
Edge cases:
haystack = '', needle = '' => return 0
"""
def locate_str(haystack, needle):
    m = len(needle)
    n = len(haystack)
    i = 0
    if haystack == '' and needle == '':
        return 0
    if needle in haystack:
        while i < n:
            if haystack[i:i + m] != needle:
                i += 1
            else:
                return i
    return -1
# Second solution
def substr(haystack, needle):
    if needle not in haystack:
        return -1
    else:
        return haystack.index(needle)
