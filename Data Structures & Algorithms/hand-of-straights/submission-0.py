from collections import Counter

class Solution:
    def isNStraightHand(self, hand, groupSize):
        n = len(hand)

        if n % groupSize:
            return False

        count = Counter(hand)

        for x in sorted(count):
            while count[x] > 0:
                for num in range(x, x + groupSize):
                    if count[num] == 0:
                        return False
                    count[num] -= 1

        return True