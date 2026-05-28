class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        l = 0
        # Left to Right
        for r in range(1, len(height)):
            if height[r] >= height[l]:
                bounded = min(height[l], height[r])
                for i in range(l + 1, r):
                    water += bounded - height[i]
                l = r
        # Right to Left (for remaining part)
        r = len(height) - 1
        for l in range(len(height) - 2, -1, -1):
            if height[l] > height[r]:
                bounded = min(height[l], height[r])
                for i in range(l + 1, r):
                    water += bounded - height[i]
                r = l
        return water