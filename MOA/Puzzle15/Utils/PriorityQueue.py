import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._dic = {}

    def empty(self):
        return len(self._queue) == 0

    def put(self, item):
        if str(item) in self._dic and \
                        self._dic[str(item)].fn() > item.fn():
            self._dic[str(item)].to_pop = False

        self._dic[str(item)] = item
        item.to_pop = True
        heapq.heappush(self._queue, item)

    def get(self):
        item = heapq.heappop(self._queue)
        while not item.to_pop:
            item = heapq.heappop(self._queue)
        return item
