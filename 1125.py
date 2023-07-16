class Solution(object):
    def smallestSufficientTeam(self, req_skills, people):
        """
        :type req_skills: List[str]
        :type people: List[List[str]]
        :rtype: List[int]
        """
        n = len(req_skills)
        skill_to_index = {skill: i for i, skill in enumerate(req_skills)}

        people_skills = [0] * len(people)
        for i, person in enumerate(people):
            for skill in person:
                people_skills[i] |= 1 << skill_to_index[skill]

        dp = {}
        dp[0] = []

        for i in range(len(people_skills)):
            for subset, team in list(dp.items()):
                new_subset = subset | people_skills[i]
                if new_subset not in dp or len(dp[new_subset]) > len(team) + 1:
                    dp[new_subset] = team + [i]

        return dp[(1 << n) - 1]
