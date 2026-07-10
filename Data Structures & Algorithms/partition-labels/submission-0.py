class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastOcc = {}
        for i, char in enumerate(s):
            lastOcc[char] = i

        parts = []
        start = 0
        end = 0
        for i, char in enumerate(s):
            end = max(end, lastOcc[char])
            if i == end:
                parts.append(end - start + 1)
                start = i + 1
        return parts