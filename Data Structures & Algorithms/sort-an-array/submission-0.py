class Solution:
    def sortArray(self, nums):
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr

            m = len(arr) // 2
            l = merge_sort(arr[:m])
            r = merge_sort(arr[m:])

            i = j = 0
            res = []

            while i < len(l) and j < len(r):
                if l[i] < r[j]:
                    res.append(l[i])
                    i += 1
                else:
                    res.append(r[j])
                    j += 1

            return res + l[i:] + r[j:]

        return merge_sort(nums)