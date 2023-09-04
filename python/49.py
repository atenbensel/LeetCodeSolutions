class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_groups = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagram_groups:
                anagram_groups[sorted_word].append(word)
            else:
                anagram_groups[sorted_word] = [word]

        result = list(anagram_groups.values())

        return result
