class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        i = 0
        while i < len(asteroids):
            if i > 0 and asteroids[i] < 0 and asteroids[i - 1] > 0:
                if abs(asteroids[i]) > asteroids[i - 1]:
                    asteroids.pop(i - 1)
                    i -= 1
                elif abs(asteroids[i]) == asteroids[i - 1]:
                    asteroids.pop(i)
                    asteroids.pop(i - 1)
                    i -= 2
                else:
                    asteroids.pop(i)
                    i -= 1
            else:
                i += 1

        return asteroids
