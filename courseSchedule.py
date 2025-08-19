class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indeg = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            indeg[a] += 1

        # Start with courses that have no prerequisites
        q = deque([i for i in range(numCourses) if indeg[i] == 0])

        taken = 0  # how many courses we can complete
        while q:
            u = q.popleft()
            taken += 1
            # "Take" u, so its outgoing edges reduce neighbors' indegree
            for v in graph[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        # If we processed all courses, there was no cycle
        return taken == numCourses

# Problem: Course Schedule (LeetCode 207)

# Approach: Kahn's Algorithm (BFS Topological Sort)

# Time Complexity : O(N + M)
#   N = numCourses, M = number of prerequisite pairs.
#   We build the graph once and process each edge/node once.

# Space Complexity : O(N + M)
#   Adjacency list + in-degree array + queue.

# Did this code successfully run on LeetCode : Yes (207)

# Any problem you faced while coding this :
#   - Getting edge direction wrong. For [a, b] meaning "b before a", add edge b -> a.
#   - Forgetting to count how many courses are "taken" (processed). Must compare with numCourses.
#   - Not initializing queue with ALL zero in-degree nodes.