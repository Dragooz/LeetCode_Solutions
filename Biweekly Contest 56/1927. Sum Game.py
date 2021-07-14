class Solution(object):
    def sumGame(self, num):
        """
        :type num: str
        :rtype: bool
        """
        #false = bob win (both side equal)
        #true = alice win (both side not equal) (start first)
        
        num_length = len(num)
        
        first_half = [str(i) for i in num[:num_length/2]]
        second_half = [str(i) for i in num[num_length/2:]]
        
        first_half_q = sum([1 for i in first_half if i=='?'])
        second_half_q = sum([1 for i in second_half if i=='?'])
        
        fh_total = sum([int(i) for i in first_half if i!='?'])
        sh_total = sum([int(i) for i in second_half if i!='?'])
        
        if first_half_q == second_half_q: #if they have same nums
            if fh_total == sh_total:
                return False
            else:
                return True
        elif abs(first_half_q-second_half_q) == 1: #alice win as she start first
            return True
        else: #complex condition
            q_left = abs(first_half_q - second_half_q)

            #2? -> 9max(bob), 3? -> 9max (bob) 
            if abs(fh_total - sh_total) != (9*q_left//2): #not possible to equal
                return True
            else:
                 #a side is already overwhelm the other side
                if (fh_total>sh_total and first_half_q >second_half_q) or (sh_total>fh_total and second_half_q >first_half_q):
                    return True
                else:
                    return False