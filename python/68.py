class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result = []
        line = []
        line_length = 0

        for word in words:
            if line_length + len(line) + len(word) > maxWidth:
                spaces_to_add = maxWidth - line_length
                if len(line) == 1:
                    result.append(line[0] + ' ' * spaces_to_add)
                else:
                    num_gaps = len(line) - 1
                    spaces_per_gap = spaces_to_add // num_gaps
                    extra_spaces = spaces_to_add % num_gaps
                    justified_line = line[0]

                    for i in range(1, len(line)):
                        spaces = spaces_per_gap + (1 if i <= extra_spaces else 0)
                        justified_line += ' ' * spaces + line[i]
                    result.append(justified_line)

                line = []
                line_length = 0

            line.append(word)
            line_length += len(word)

        last_line = ' '.join(line).ljust(maxWidth)
        result.append(last_line)

        return result
