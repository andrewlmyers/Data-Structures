import heapq

class PriorityQueue:
    def __init__(self) -> None:
        self.data = []
    def push(self, value):
        heapq.heappush(self.data, -value)
    def pop(self):
        return -heapq.heappop(self.data)

pq = PriorityQueue()
pq.push(7)
pq.push(1)
pq.push(4)
print(pq.pop()) # Output: 7
print(pq.pop())
print(pq.data)  # Output: [-4, -1]