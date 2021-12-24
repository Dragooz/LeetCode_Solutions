class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        
        heap = []
        
        for res in restaurants:
            if (res[2] == veganFriendly or veganFriendly==0) and res[3] <= maxPrice and res[4] <= maxDistance:
                heap.append((res[1], res[0]))
                # heappush(heap, (-res[1], -res[0]))
                
        heap.sort(key= lambda x: (x[0], x[1]), reverse=True)
        
        return [res[1] for res in heap]