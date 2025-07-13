# 3163. String Compression III
#
# Medium
#
# Given a string word, compress it using the following algorithm:
#
# Begin with an empty string comp. While word is not empty, use the following operation:
#     Remove a maximum length prefix of word made of a single character c repeating at most 9 times.
# Append the length of the prefix followed by c to comp.
# Return the string comp.
#
#
#
# Example 1:
#
# Input: word = "abcde"
#
# Output: "1a1b1c1d1e"
#
# Explanation:
#
# Initially, comp = "". Apply the operation 5 times, choosing "a", "b", "c", "d", and "e" as the prefix in each operation.
#
# For each prefix, append "1" followed by the character to comp.
#
# Example 2:
#
# Input: word = "aaaaaaaaaaaaaabb"
#
# Output: "9a5a2b"
#
# Explanation:
#
# Initially, comp = "". Apply the operation 3 times, choosing "aaaaaaaaa", "aaaaa", and "bb" as the prefix in each operation.
#
# For prefix "aaaaaaaaa", append "9" followed by "a" to comp.
# For prefix "aaaaa", append "5" followed by "a" to comp.
# For prefix "bb", append "2" followed by "b" to comp.
#
#
# Constraints:
#
# 1 <= word.length <= 2 * 105
# word consists only of lowercase English letters.





# Time Limit Exceeded 738 / 744 testcases passed
# class Solution(object):
#     def compressedString(self, word):
#         """
#         :type word: str
#         :rtype: str
#         """
#         count = 1
#         string = ""
#         word_len =  len(word)
#         j = 1
#         for i in range(0,word_len-1):
#             if word[i] == word[j] and count != 9:
#                 count += 1
#                 if j != word_len:
#                     j += 1
#             else:
#                 string += str(count) + word[i]
#                 count = 1
#                 j += 1
#         string += str(count) + word[-1]
#         return string



# 206 ms Beats 71.52% with GPT
class Solution(object):
    def compressedString(self, word):
        """
        :type word: str
        :rtype: str
        """
        count = 1
        comp = []
        for i in range(1, len(word)):
            if word[i] == word[i - 1] and count < 9:
                count += 1
            else:
                comp.append(f"{count}{word[i - 1]}")
                count = 1

        comp.append(f"{count}{word[-1]}")

        return ''.join(comp)

obj = Solution()

print(obj.compressedString("aaaaaaaaaaaaaabb"))