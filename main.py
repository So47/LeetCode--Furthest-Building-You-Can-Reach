class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []  # Min heap to keep track of the largest jumps covered by bricks
        # heap1 = []
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            print(diff,heap,ladders,bricks)
            if diff > 0:
                #This action doesn't directly use a ladder but prepares for the decision-making on whether to use bricks or ladders.
                heapq.heappush(heap, diff)
                # heap1.append(diff)
            if len(heap) > ladders:  # More jumps than ladders means we need to use bricks
                print(heap)
                bricks -= heapq.heappop(heap)  # Use bricks for the smallest jump
                # min_value = min(heap1)  # Find the smallest element
                # heap1.remove(min_value)  # Remove the smallest element from the list
                # bricks -= min_value
                if bricks < 0:  # If we run out of bricks, return current index
                    return i
        return len(heights) - 1
