class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not len(t): return ""

        # maintain hashmap to contain characters count
        count, window = {}, {}

        # update need hashmap (count) with character frequencies from string t
        for c in t:
            count[c] = 1 + count.get(c,0)

        have, need = 0, len(count)
        res, resLen = [-1, -1], float("infinity")
        # 2 pointer approach - sliding window
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            # check if c is in need hashmap and frequency matches required frequency, update have
            if c in count and window[c] == count[c]:
                have += 1
            
            while have == need:
                # compare lengths of substring and current resLen to find minimum
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                # start moving left pointer till have == need condition is invalidated
                window[s[l]] -= 1
                if s[l] in count and window[s[l]] < count[s[l]]:
                    have -= 1
                
                l += 1
        l, r = res

        return s[l: r + 1] if resLen != float("infinity") else ""
            
        