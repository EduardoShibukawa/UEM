import heapq


class Puzzle15PriorityQueue:
    def __init__(self):
        self._queue = []

    def empty(self):
        return len(self._queue) == 0

    def put(self, item):
        heapq.heappush(self._queue, item)

    def get(self):
        return heapq.heappop(self._queue)
