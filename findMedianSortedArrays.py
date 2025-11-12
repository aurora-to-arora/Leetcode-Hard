class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j = 0, 0
        merged = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        
        merged.extend(nums1[i:])
        merged.extend(nums2[j:])

        total = len(merged)
        half = total // 2

        if total % 2 == 0:
            return (merged[half - 1] + merged[half]) / 2
        else:
            return merged[half]
