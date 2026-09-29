class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def edgetograph(prereq):
            hmap = {}
            for a,b in prereq:
                if a not in hmap:
                    hmap[a] = []
                if b not in hmap:
                    hmap[b] = []
                hmap[b].append(a)

            return hmap 
             
        def dfs(src, graph, visited, path):
            if src in path:
                return False 
            if src in visited:
                return True 
            visited.add(src)
            path.add(src)
            for nei in graph[src]:               
                if not dfs(nei, graph, visited, path):
                    return False 
            path.remove(src)
            return True 

        graph = edgetograph(prerequisites)
        path = set()
        visited = set() 
        for node in graph.keys():
            if not dfs(node, graph, visited, path):
                return False 
        return True  
        

        