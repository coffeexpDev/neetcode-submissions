class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0
        
        # create a map for pattern -> word matching pattern
        nei = defaultdict(list)
        # add the beginWord to the wordList
        wordList.append(beginWord)
        # add all words in wordList to respective pattern in nei hashmap
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                nei[pattern].append(word)
        
        visited = set()
        q = deque([beginWord])
        res = 1

        while q:
            # iterate through all words in q
            for i in range(len(q)):
                word = q.popleft()
                # if word == endWord, return res -> least number of transformations required
                if word == endWord:
                    return res
                # iterate through the characters of the word
                for j in range(len(word)):
                    # create pattern key to get matching words
                    pattern = word[:j] + "*" + word[j + 1:]
                    # iterate through matching pattern words
                    for neiWord in nei[pattern]:
                        # if word is not visited, add to visited set and q
                        if neiWord not in visited:
                            visited.add(neiWord)
                            q.append(neiWord)

            res += 1
        
        return 0
        