import heapq


class MinHeap:

    def __init__(self):
        self.heap = []

    def push(self, quantity, product_id):
        heapq.heappush(self.heap, (quantity, product_id))

    def pop(self):
        if not self.heap:
            return None
        return heapq.heappop(self.heap)

    def get_top_k(self, k):
        return heapq.nsmallest(k, self.heap)