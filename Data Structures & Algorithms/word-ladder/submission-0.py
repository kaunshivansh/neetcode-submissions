from collections import deque
from typing import List

class Solution:
    def ladderLength(
        self,
        beginWord: str,
        endWord: str,
        wordList: List[str]
    ) -> int:

        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0

        q = deque([(beginWord, 1)])
        visited = {beginWord}

        while q:
            word, steps = q.popleft()

            if word == endWord:
                return steps

            word_chars = list(word)

            for i in range(len(word)):
                original = word_chars[i]

                for ch in "abcdefghijklmnopqrstuvwxyz":
                    if ch == original:
                        continue

                    word_chars[i] = ch
                    nxt = "".join(word_chars)

                    if nxt in wordSet and nxt not in visited:
                        visited.add(nxt)
                        q.append((nxt, steps + 1))

                word_chars[i] = original

        return 0