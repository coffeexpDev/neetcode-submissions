class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        maxArea = 0

        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                stackIdx, stackHeight = stack.pop()
                maxArea = max(maxArea, (i - stackIdx)*stackHeight)
                start = stackIdx
            stack.append((start, h))

        while stack:
            stackIdx, stackHeight = stack.pop()
            maxArea = max(maxArea, (n - stackIdx)*stackHeight)

        return maxArea

            

        