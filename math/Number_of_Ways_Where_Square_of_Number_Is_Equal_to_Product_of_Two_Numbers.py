class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def count(l1, l2):
            l2_squared = Counter([e ** 2 for e in l2]) 
            co = 0
            n = len(l1)
            for i in range(n):
                for j in range(i + 1, n):
                    if l1[i] * l1[j] in l2_squared:
                        co += l2_squared[l1[i] * l1[j]]
            return co            
        return count(nums1, nums2) + count(nums2, nums1)
