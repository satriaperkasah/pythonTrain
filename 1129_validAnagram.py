"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""
class Solution(object):
    def isAnagram(self, s, t):
        newInput = {}
        for x in s:
            newInput[x] = newInput.get(x,0) + 1
            #print(newInput[x], x)

        for y in t:
            flag = newInput.get(y)
            if flag == None:
                flag = False
                break
            else:
                newInput[y] -= 1
                flag = True

        if flag == True:
            return True
        else:
            return False

solution = Solution()
print(solution.isAnagram("rat", "cat"))

"""
for x in s:
    newInput[x] = newInput.get(x,0) + 1
    #print(newInput[x], x)

for y in t:
    flag = newInput.get(y)
    if flag == None:
        print(False)
        break
    else:
        newInput[y] -= 1
        print(True)
"""