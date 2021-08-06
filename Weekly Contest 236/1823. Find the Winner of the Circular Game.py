class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = [i for i in range(1, n+1)] #friends with numbering
        index_to_remove = 0 #which index to remove
        while len(friends) >1: #loop until winner
            index_to_remove += (k-1) #which to pop (-1 because for example, index 0 and 1 count as 2)
            index_to_remove = index_to_remove % len(friends)  #prevent out of range
            friends.pop(index_to_remove) #everytime its pop, the index_to_remove will become the next person automatically

        return friends[0]