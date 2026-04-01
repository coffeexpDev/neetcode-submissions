class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            # check if total = target
            if total == target:
                # append to res if true
                res.append(cur.copy())
                return
            # check for invalidating conditions 
            if i >= len(nums) or total > target:
                return
            # branch into 2 possibilities - with duplicates and without duplicates
            cur.append(nums[i])
            dfs(i, cur, total+nums[i])
            cur.pop()
            dfs(i + 1, cur, total)

        
        dfs(0, [], 0)

        return res
            

        