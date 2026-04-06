class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i, intrvl in enumerate(intervals):
            if newInterval[1] < intrvl[0]:
                res.append(newInterval)
                return res + intervals[i:]
            if newInterval[0] > intrvl[1]:
                res.append(intrvl)
            else:
                newInterval = [min(intrvl[0], newInterval[0]), max(intrvl[1], newInterval[1])]
        
        res.append(newInterval)
        return res
        