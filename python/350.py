## O(n + m) Method using Hashmap
# def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
#     if len(nums2) > len(nums1):
#         return intersect(nums2, nums1)
#     hashTable = {}
#     interArr = []
#     for i in nums1:
#         if i in hashTable.keys():
#             hashTable[i] += 1
#         else:
#             hashTable[i] = 1
    
#     for i in nums2:
#         if i in hashTable.keys():
#             if hashTable[i] > 0:
#                 interArr.append(i)
#                 hashTable[i] -= 1
    
#     return interArr

## O(mlogm + nlogn) Method using two pointers and Merge Sort
def mergesort(arr):
    if len(arr) > 1:

        mid = len(arr) // 2 
        left = arr[:mid]
        right = arr[mid:]

        mergesort(left)
        mergesort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    mergesort(nums1)
    mergesort(nums2)
    
    interArr = []
    i = j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            interArr.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1
    
    return interArr
print(intersect([1,2,2,1],[2,2]))
print(intersect([4,9,5],[9,4,9,8,4]))