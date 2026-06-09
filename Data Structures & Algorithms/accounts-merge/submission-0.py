from collections import defaultdict
from typing import List

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)

        parent = list(range(n))
        rank = [1] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            pa, pb = find(a), find(b)

            if pa == pb:
                return

            if rank[pa] < rank[pb]:
                pa, pb = pb, pa

            parent[pb] = pa
            rank[pa] += rank[pb]

        email_to_account = {}

        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_account:
                    union(i, email_to_account[email])
                else:
                    email_to_account[email] = i

        groups = defaultdict(list)

        for email, acc_idx in email_to_account.items():
            root = find(acc_idx)
            groups[root].append(email)

        res = []

        for root, emails in groups.items():
            res.append(
                [accounts[root][0]] + sorted(emails)
            )

        return res
        