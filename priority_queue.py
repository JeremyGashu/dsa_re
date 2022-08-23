import queue

pq = queue.PriorityQueue()
pq.put((2, 'Gashu'))
pq.put((1, 'Ermias'))
pq.put((3, 'Adane'))
print(list(pq.get_nowait()))
print(list(pq.get_nowait()))
print(list(pq.get_nowait()))
print(list(pq.get_nowait()))
