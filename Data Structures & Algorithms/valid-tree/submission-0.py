class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:   # do this check once, up top
            return False

        def edgetograph(edges):
            hmap = {}
            for i in range(n):
                hmap[i] = []
            for a,b in edges:
                hmap[a].append(b)
                hmap[b].append(a)
            return hmap
        
        def dfs(src, graph, visited) -> bool:
            if src in visited:
                return False 
            visited.add(src)
            for nei in graph[src]:
                dfs(nei, graph, visited)
            return True 


        graph = edgetograph(edges)
        visited, path = set(), set()
        return dfs(0,graph,visited) and len(visited) == n


