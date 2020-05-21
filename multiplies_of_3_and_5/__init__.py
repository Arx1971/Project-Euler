class Solution(object):
    def multiplies_of_three_and_fives(self) -> int:
        sum_of_multipliers = 0
        for i in range(1, 1000):
            if i % 3 == 0 or i % 5 == 0:
                sum_of_multipliers += i

        return sum_of_multipliers


obj = Solution()

print(obj.multiplies_of_three_and_fives())
