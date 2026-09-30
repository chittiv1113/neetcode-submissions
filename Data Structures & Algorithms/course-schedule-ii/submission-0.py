class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = {}
        for i in range(numCourses):
            graph[i] = []
        for a,b in prerequisites:
            graph[a].append(b)

        def dfs(src, visited, path, output):
            if src in path:
                return False 
            if src in visited:
                return True 
            path.add(src)
            visited.add(src)
            for nei in graph[src]:
               if not dfs(nei, visited, path, output):
                return False
            path.remove(src)
            output.append(src)
            return True 
        
        output = []
        visited = set()
        path = set()
        for node in graph.keys():
            if not dfs(node, visited, path, output):
                return []
        return output

