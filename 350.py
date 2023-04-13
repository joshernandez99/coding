def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    hashTable = {}
    for i in nums1:
        if i in hashTable.keys():
            hashTable[i] += 1
        else:
            hashTable[i] = 1
    
    for i in nums2:
        if i in hashTable.keys():
            hashTable[i] += 1
        else:
            hashTable[i] = 1
    
    return [k for k, v in hashTable.items() if v > 1]


print(intersect([1,2,2,1],[2,2]))