"""
Question: Find the longest common prefix string amongst an array of strings
Input: a list of strings
Output: a longest common prefix
Example:
Input: ['leet', 'leetcode', 'lete']
Output: 'le'
"""
input = ['leet', 'leetcod', 'lete']
def longest_common_prefix(l):
    if len(l) == 0:
        return ""
    prefix = l[0]
    for strs in l[1:]:
        index = min(len(prefix), len(strs))
        i = 0
        while i < index:
            if prefix[i] != strs[i]:
                prefix = prefix[:i]
                break
            i += 1
        if len(prefix) > index:
            prefix = prefix[:index]
    return prefix

output = 'le'
res = print(longest_common_prefix(input))

