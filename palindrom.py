from functools import lru_cache

class Solution:
    def minInsertions(self, palindrome_string):
        @lru_cache(maxsize=None)
        def recursion_func(palindrome_string, left, right):
            if left >= right:
                return 0
            if palindrome_string[left] == palindrome_string[right]:
                return recursion_func(palindrome_string, left + 1, right - 1)
            return min(recursion_func(palindrome_string, left, right - 1), recursion_func(palindrome_string, left + 1, right)) + 1

        return recursion_func(palindrome_string, 0, len(palindrome_string) - 1)


obj = Solution()
print(obj.minInsertions('aabbbbbd'))

