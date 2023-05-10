## O(n^2) Method
# def twoSum( nums: list[int], target: int) -> list[int]:
#         for i in range(len(nums) - 1):
#             for j in range(len(nums) - 1 - i):
#                 if nums[j + 1 + i] == target - nums[i]:
#                     return [i, j + i + 1]
        
#         return []

## O(n) Method
def twoSum( nums: list[int], target: int) -> list[int]:
    hashTable = {}
    for i in range(len(nums)):
        if nums[i] in hashTable.values():
            return [(list(hashTable.values())).index(nums[i]), i]
        else:
            hashTable[i] = target - nums[i]
    print(hashTable)
    return []

print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))
print(twoSum([3,3], 6))
print(twoSum([2,5,5,11], 10))