l, r = 0, len(nums) - 1

while l <= r:
    mid = (l + r) // 2
    if nums[mid] < target:
        l = mid + 1
    elif nums[mid] > target:
        r = mid - 1
    else:
        return mid
return -1

# As a rule of thumb, use m = l + (r-l)//2 with l = m + 1 and r = m, 
# and use m = r - (r-l)//2 with l = m and r = m - 1. This can prevent m from stucking at r (or l) after the updating step.