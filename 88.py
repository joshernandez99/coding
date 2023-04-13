## O(nlogn) Method - Tradition Merge Sort
# def mergesort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2
#         L = arr[:mid]
#         R = arr[mid:]

#         mergesort(L)
#         mergesort(R)

#         i = j = k = 0

#         while i < len(L) and j < len(R):
#             if L[i] > R[j]:
#                 arr[k] = L[i]
#                 i += 1
#             else:
#                 arr[k] = R[j]
#                 j += 1
#             k += 1
        
#         while i < len(L):
#             arr[k] = L[i]
#             i += 1
#             k += 1
#         while j < len(R):
#             arr[k] = R[j]
#             j += 1
#             k += 1
# def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
#     """
#     Do not return anything, modify nums1 in-place instead.
#     """
#     for i in nums2:
#         nums1.append(i)
#     print(nums1)
#     mergesort(nums1)
#     print(nums1)

## O(n + m) Method
def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    
    mainIndex, mIndex, nIndex = m + n - 1, m - 1, n - 1

    while n > 0 and m > 0:
        if nums1[mIndex] > nums2[nIndex]:
            nums1[mainIndex] = nums1[mIndex] 
            mIndex -= 1
            m -= 1
        else:
            nums1[mainIndex] = nums2[nIndex]
            nIndex -= 1
            n -= 1
        mainIndex -= 1
    

    while m > 0:
        nums1[mainIndex] = nums1[mIndex]
        mIndex -= 1
        m -= 1
        mainIndex -= 1

    while n > 0:
        nums1[mainIndex] = nums2[nIndex]
        nIndex -= 1
        n -= 1
        mainIndex -= 1
    

            


nums1 = [1,2,3,0,0,0]
merge(nums1, 3, [2,5,6], 3)
print(nums1)
    

                
    