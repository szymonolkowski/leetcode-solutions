class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        quieres_with_indexes_sorted = [(query, index) for index, query in enumerate(queries)]
        quieres_with_indexes_sorted.sort(key=lambda x: x[0])
        
        logs.sort(key=lambda x: x[1])
        arr = [n] * len(queries)
        servers = [0]*n
        index_first = 0
        index_last = 0
        active_servers = 0
        for query, original_index in quieres_with_indexes_sorted:
            while index_last < len(logs) and logs[index_last][1] <= query:
                if servers[logs[index_last][0]-1] == 0:
                    active_servers += 1
                servers[logs[index_last][0]-1] += 1
                index_last += 1

            while index_first < len(logs) and logs[index_first][1] < (query-x):
                if servers[logs[index_first][0]-1] == 1:
                    active_servers -= 1
                servers[logs[index_first][0]-1] -= 1
                index_first += 1

            arr[original_index] -= active_servers
        return arr