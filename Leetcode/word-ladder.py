class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
  
        wordList = set(wordList)
        queue = deque((beginWord,))
        level = 0
        visited = {beginWord,}
        while queue:

            for _ in range(len(queue)):
                src = queue.popleft()


                if src == endWord:
                    return level + 1



                childrens = self.generate(src)

                for child in childrens:
                    if child not in visited and child in wordList:
                        visited.add(child)
                        queue.append(child)
            level += 1

        return 0




    def generate(self, word):

        childrens = []
        for i, char in enumerate(word):

            for ordL in range(ord("a"), ord("z") + 1):
                if ord(char) != ordL:
                    cur = word[:i] + chr(ordL) + word[i + 1:]
                    childrens.append(cur)
        return childrens







