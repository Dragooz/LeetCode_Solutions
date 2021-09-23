#the idea here is to find sub array that is = goal, where goal = sum of nums - x

cum_sum = [0] + list(accumulate(nums))
dic = {c:i for i, c in enumerate(cum_sum)}

goal = cum_sum[-1] - x
ans = -float("inf") #as the results may be 0 too

if goal<0:
    return -1
print(dic)
for num in dic:
    if num+goal in dic:
        ans = max(ans, dic[num+goal] - dic[num])
        
if ans != -float("inf"):
    return len(nums) - ans
else:
    return -1