from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)

        ans = []

        def dfs(src):
            while graph[src]:
                dfs(graph[src].pop())
            ans.append(src)

        dfs("JFK")
        return ans[::-1]