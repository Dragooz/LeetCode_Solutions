class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        n = len(nums[0])
        
        nums = [int(num, 2) for num in nums]
        
        binary_list = [i for i in range(2**n)]
        
        for i in binary_list:
            if i not in nums:
                binary_ans =  str(bin(i)[2:])
                
                return '0'*(n - len(binary_ans)) + binary_ans