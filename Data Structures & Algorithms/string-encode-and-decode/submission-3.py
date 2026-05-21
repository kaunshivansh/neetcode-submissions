class Solution:

    def encode(self, strs):
        return ''.join(f'{len(s)}#{s}' for s in strs)

    def decode(self, s):
        res, i = [], 0

        while i < len(s):
            j = s.find('#', i)
            l = int(s[i:j])
            j += 1

            res.append(s[j:j + l])
            i = j + l

        return res