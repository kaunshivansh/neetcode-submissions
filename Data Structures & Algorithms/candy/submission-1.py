class Solution:
    def candy(self, ratings):
        n = len(ratings)
        
        # Step 1: Give each child 1 candy
        candies = [1] * n
        
        # Step 2: Left to Right
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        
        # Step 3: Right to Left
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        
        return sum(candies)