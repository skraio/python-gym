import collections
import heapq
import math


class Solution:

    def dfs_approach(self,
                     maze: list[list[int]],
                     start: list[int],
                     destination: list[int]
                     ) -> int:
        print("[DFS]")
        print("space complexity: O(m*n)")
        print("time complexity: O(4^(m*n)*max(m,n))") #not sure
        
        num_rows = len(maze)
        num_cols = len(maze[0])
        dists = [[math.inf for _ in range(num_cols)] for _ in range(num_rows)]
        dists[start[0]][start[1]] = 0

        #my idea for small optimization
        x1, y1 = start
        x2, y2 = destination
        if x2 < x1:
            if y2 > y1:
                dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
            else:
                dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        else:
            if y2 > y1:
                dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            else:
                dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(cur_node: list[int]) -> None:
            i, j = cur_node
            buf = []
            for dir in dirs:

                tmp_i, tmp_j = i + dir[0], j + dir[1]
                steps = 0
                
                while 0 <= tmp_i < num_rows and \
                        0 <= tmp_j < num_cols and \
                        maze[tmp_i][tmp_j] == 0:
                    tmp_i = tmp_i + dir[0]
                    tmp_j = tmp_j + dir[1]
                    steps = steps + 1

                if steps == 0:
                    continue
                next_i = tmp_i - dir[0]
                next_j = tmp_j - dir[1]

                new_cost = dists[i][j] + steps
                if new_cost < dists[next_i][next_j]:
                    dists[next_i][next_j] = new_cost
                    if [next_i, next_j] == destination:
                        continue
                    buf.append([next_i, next_j])
            for next_node in buf:
                dfs(next_node)
        
        dfs(start)
        
        i, j = destination
        return dists[i][j] if dists[i][j] != math.inf else -1

    def bfs_approach(self,
                     maze: list[list[int]],
                     start: list[int],
                     destination: list[int]
                     ) -> int:
        print("[BFS]")
        print("space complexity: O(m*n)")
        print("time complexity: O(m*n*max(m,n))")
        
        num_rows = len(maze)
        num_cols = len(maze[0])
        dists = [[math.inf for _ in range(num_cols)] for _ in range(num_rows)]
        dists[start[0]][start[1]] = 0
        
        queue = collections.deque()
        queue.append(start)

        while queue:
            i, j = queue.popleft()

            for dir in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                tmp_i, tmp_j = i + dir[0], j + dir[1]
                steps = 0

                while 0 <= tmp_i < num_rows and \
                        0 <= tmp_j < num_cols and \
                        maze[tmp_i][tmp_j] == 0:
                    tmp_i = tmp_i + dir[0]
                    tmp_j = tmp_j + dir[1]
                    steps = steps + 1

                if steps == 0:
                    continue
                next_i = tmp_i - dir[0]
                next_j = tmp_j - dir[1]

                new_cost = dists[i][j] + steps
                if new_cost < dists[next_i][next_j]:
                    dists[next_i][next_j] = new_cost
                    if [next_i, next_j] == destination:
                        continue
                    queue.append([next_i, next_j])
                    
        i, j = destination
        return dists[i][j] if dists[i][j] != math.inf else -1

    def dijkstra_approach(self,
                          maze: list[list[int]],
                          start: list[int],
                          destination: list[int]
                          ) -> int:
        print("[Dijkstra]")
        print("space complexity: O(m*n)")
        print("time complexity: O(m*n*log(m*n)")
        
        num_rows = len(maze)
        num_cols = len(maze[0])
        dists = [[math.inf for _ in range(num_cols)] for _ in range(num_rows)]
        dists[start[0]][start[1]] = 0
        
        pq = []
        heapq.heappush(pq, [0, start])

        while pq:
            cur_cost, cur_node = heapq.heappop(pq)
            i, j = cur_node
            if cur_node == destination:
                return cur_cost

            for dir in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                tmp_i, tmp_j = i + dir[0], j + dir[1]

                steps = 0
                while 0 <= tmp_i < num_rows and \
                        0 <= tmp_j < num_cols and \
                        maze[tmp_i][tmp_j] == 0:
                    tmp_i += dir[0]
                    tmp_j += dir[1]
                    steps += 1

                if steps == 0:
                    continue

                next_i = tmp_i - dir[0]
                next_j = tmp_j - dir[1]

                new_cost = cur_cost + steps
                if new_cost < dists[next_i][next_j]:
                    dists[next_i][next_j] = new_cost
                    heapq.heappush(pq, [new_cost, [next_i, next_j]])
                    
        i, j = destination
        return dists[i][j] if dists[i][j] != math.inf else -1