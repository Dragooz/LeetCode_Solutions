class Solution:
    def minimumBuckets(self, street: str) -> int:
        
        street = [0 if i=='.' else -1 for i in street]
        
        if len(street) == 1:
            return 0 if street[0] == 0 else -1
            
        for i in range(len(street)):
            if street[i] == -1: #house
    
                if i == 0:
                    if street[i+1] == -1:
                        return -1
                    else:
                        street[i+1] = 1
                        continue
                    
                if i == len(street)-1:
                    if street[i-1] == -1:
                        return -1
                    else:
                        street[i-1] = 1
                        continue
                    
                if street[i-1]==1 or street[i+1] == 1:
                    continue
                elif street[i+1] == -1:
                    if street[i-1] == -1:
                        return -1
                    else:
                        street[i-1] = 1
                else:
                    street[i+1] = 1

        return sum([i if i>0 else 0 for i in street])