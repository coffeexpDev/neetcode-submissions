class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pairs = [(position[i], speed[i]) for i in range(len(position)-1, -1, -1)]
        pairs.sort(reverse = True)

        stack = []

        for p, s in pairs:
            stack.append((target - p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
        