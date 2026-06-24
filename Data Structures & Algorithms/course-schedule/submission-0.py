class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for course, prereq in prerequisites:
            adj[prereq].append(course)
        visited_state = [0] * numCourses
        def dfs(course):
            if visited_state[course] == 1:
                return False
            if visited_state[course] == 2:
                return True
            visited_state[course] = 1
            for neighbor in adj[course]:
                if not dfs(neighbor):
                    return False
            visited_state[course] = 2
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True