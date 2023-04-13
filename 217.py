class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashtable = {}

        for x in nums:
            ## check to see if it in hashmap
            if (hashtable.get(x) == None):
                hashtable[x] = 1
            else:
                hashtable[x] += 1

                
            if (hashtable.get(x) >= 2):
                return True
        return False
        

nums = [7, 8, 10, 9, 6]
print(Solution.containsDuplicate(nums, nums))
nums = [7]
print(Solution.containsDuplicate(nums, nums))
nums = [7, 2, 10, 7]
print(Solution.containsDuplicate(nums, nums))
nums = [1,2,3,1]
print(Solution.containsDuplicate(nums, nums))
