class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i not in range(len(nums)):
                res.append(subset.copy())
                return
            
            # branch which includes element value
            subset.append(nums[i])
            dfs(i + 1)

            # branch which excludes element value
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res
        