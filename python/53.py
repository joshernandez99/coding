### O(n^2) time (Brute Force)
# def maxSubArray(nums: list[int]) -> int:
#     largeSum = float('-inf')
#     for x in range(len(nums)):
#         sum = nums[x]

#         if (sum > largeSum or largeSum == float('-inf')):
#                 largeSum = sum

#         for y in range(len(nums) - x - 1):
#             sum += nums[y + x + 1]
#             if (sum > largeSum):
#                 largeSum = sum

#     return largeSum

### Divide and Conquer Method O(nlogn)
# def DAC(nums, start, end):
#     if start > end:
#         return float('-inf')
    
#     currsum, rightsum, leftsum, mid = 0, 0, 0, (start + end) // 2
#     for i in range(mid - 1, start - 1, -1):
#         currsum = currsum + nums[i]
#         leftsum = max(leftsum, currsum)
#     currsum = 0
#     for i in range(mid + 1, end + 1):
#         currsum = currsum + nums[i]
#         rightsum = max(rightsum, currsum)

#     return max(DAC(nums, start, mid - 1), DAC(nums, mid + 1, end), leftsum + nums[mid] + rightsum )
    
# def maxSubArray(nums: list[int]) -> int:
#     return(DAC(nums, 0, len(nums) - 1))

## O(n) time
def maxSubArray(nums: list[int]) -> int:
    largesum = float('-inf')
    tempSum = 0
    for x in nums:
        tempSum = max(x, tempSum + x)
        largesum = max(largesum, tempSum)
    return largesum
        




# a = [2,1]
# print(a[1:2])
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(maxSubArray([-2,1]))
print(maxSubArray([5,4,-1,7,8]))
