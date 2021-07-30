#first attempt
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1
        for i in range(1, len(arr)):
            if abs(arr[i] - arr[i-1]) <= 1:
                pass
            else:
                arr[i] = arr[i-1] + 1

        return max(arr)

#reference attempt:
#https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/discuss/1185804/JavaC%2B%2BPython-Sort-and-One-pass by lee215
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        pre = 0
        for i in range(len(arr)):
            pre = min(pre+1, arr[i])

        return pre