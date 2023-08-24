class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []

        word_len = len(words[0])
        total_len = len(words) * word_len
        words_count = {}
        for word in words:
            words_count[word] = words_count.get(word, 0) + 1

        result = []
        for i in range(word_len):
            left, right, formed = i, i, 0
            current_words = {}

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len

                if word in words_count:
                    current_words[word] = current_words.get(word, 0) + 1
                    formed += 1

                    while current_words[word] > words_count[word]:
                        current_words[s[left:left + word_len]] -= 1
                        formed -= 1
                        left += word_len

                    if formed == len(words):
                        result.append(left)

                else:
                    current_words.clear()
                    formed = 0
                    left = right

        return result
