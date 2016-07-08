import heapq
import sys

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._dic = {}
        self._index = 0

    def empty(self):
        return len(self._queue) == 0

    def put(self, item):
        if str(item) in self._dic and \
                        self._dic[str(item)].fn() > item.fn():
            self._dic[str(item)].to_pop = False

        self._dic[str(item)] = item
        item.to_pop = True
        heapq.heappush(self._queue, item)
        self._index += 1

    def get(self):
        item = heapq.heappop(self._queue)
        while not item.to_pop:
            item = heapq.heappop(self._queue)
        return item
