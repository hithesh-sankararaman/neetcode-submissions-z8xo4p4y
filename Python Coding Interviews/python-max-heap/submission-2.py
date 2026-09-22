import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    
    #return sorted(nums,reverse=True)
    # heapq.heapify_max(nums)
    # return [heapq.heappop_max(nums) for _ in range(len(nums))]
    heap=[]
    top=[]
    for num in nums:
        heapq.heappush(heap,-num)
    while heap:
        top.append(-heapq.heappop(heap))
    return top




# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
