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

        #stage 1: input all data into dictionary count
        for x in s:
            newInput[x] = newInput.get(x,0) + 1
            #print(newInput[x], x)

        #stage 2: deduct the dictionary based on the given input
        if len(s) == len(t):
            for y in t:
                flag = newInput.get(y)
                if flag == None:
                    flag = False
                    break
                else:
                    newInput[y] -= 1
                    flag = True
        else:
            flag = False

        #stage 3: check the dictionary whether any leftover
        if flag == True:
            for x in s:
                if newInput[x] != 0:
                    flag = False
                    break

        #stage 4: flag judgement
        if flag == True:
            return True
        else:
            return False

solution = Solution()
print(solution.isAnagram("ab", "b"))

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