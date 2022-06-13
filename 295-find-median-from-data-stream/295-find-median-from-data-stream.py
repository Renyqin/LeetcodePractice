import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        
        self.max_heap = []
        self.min_heap = []
        

    def addNum(self, num: int) -> None:
        if not self.max_heap:
            heapq.heappush(self.max_heap, (-num, num))
        
        elif num > self.max_heap[0][1]:
            heapq.heappush(self.min_heap, (num, num))
            if len(self.min_heap) > len(self.max_heap)+1:
                ele = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, (-ele[0], ele[1]))
            
        else:
            heapq.heappush(self.max_heap, (-num, num))
            if len(self.max_heap) > len(self.min_heap)+1:
                ele = heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, (-ele[0], ele[1]))
                
        
        return num
        

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return self.max_heap[0][1]
        elif len(self.max_heap) < len(self.min_heap):
            return self.min_heap[0][1]
        else:
            return (self.max_heap[0][1] + self.min_heap[0][1]) /2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()