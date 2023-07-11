class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digit_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        combinations = []
        
        if digits:
            self.generateCombinations(digits, '', digit_letters, combinations)
        
        return combinations
    
    def generateCombinations(self, digits, current_combination, digit_letters, combinations):
        if not digits:
            combinations.append(current_combination)
            return
        
        current_digit = digits[0]
        
        for letter in digit_letters[current_digit]:
            self.generateCombinations(
                digits[1:], 
                current_combination + letter, 
                digit_letters, 
                combinations
            )
