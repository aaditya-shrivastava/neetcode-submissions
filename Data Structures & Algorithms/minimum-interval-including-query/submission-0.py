class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        indexed_queries = sorted([(q, i) for i, q in enumerate(queries)])
        result = [-1] * len(queries)
        min_heap = []
        interval_pointer = 0
        for query_value, query_index in indexed_queries:
            while interval_pointer < len(intervals) and intervals[interval_pointer][0] <= query_value:
                left, right = intervals[interval_pointer]
                heapq.heappush(min_heap, (right - left + 1, right))
                interval_pointer += 1
            while min_heap and min_heap[0][1] < query_value:
                heapq.heappop(min_heap)
            if min_heap:
                result[query_index] = min_heap[0][0]
                
        return result
