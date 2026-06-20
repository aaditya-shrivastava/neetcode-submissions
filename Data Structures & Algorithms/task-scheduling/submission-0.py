class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)    
        max_freq = 0
        num_max_freq = 0
        for count in task_counts.values():
            if count > max_freq:
                max_freq = count
                num_max_freq = 1
            elif count == max_freq:
                num_max_freq += 1
        min_cycles = (max_freq - 1) * (n + 1) + num_max_freq
        return max(min_cycles, len(tasks))