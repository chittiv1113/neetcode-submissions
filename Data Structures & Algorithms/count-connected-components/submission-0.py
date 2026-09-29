class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        def edgetograph(edges):
            hmap = {}
            for i in range(n):
                hmap[i] = []
            for a,b in edges:
                hmap[a].append(b)
                hmap[b].append(a)
            return hmap

        def dfs(src, visited, graph):
            if src in visited:
                return False
            visited.add(src)

            for nei in graph[src]:
                dfs(nei, visited, graph)
            return True 
            

        graph = edgetograph(edges)
        count = 0 
        visited = set()
        for node in graph.keys():
            if dfs(node, visited, graph):
                count += 1

        return count 
        
