class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        low = 0
        high = m

        while low <= high:

            partition1 = low + (high - low) // 2
            partition2 = (m + n + 1) // 2 - partition1

            left1 = nums1[partition1 - 1] if partition1 > 0 else float('-inf')
            right1 = nums1[partition1] if partition1 < m else float('inf')

            left2 = nums2[partition2 - 1] if partition2 > 0 else float('-inf')
            right2 = nums2[partition2] if partition2 < n else float('inf')

            left = max(left1, left2)
            right = min(right1, right2)

            if left <= right:

                if (m + n) % 2 == 1:
                    return left
                else:
                    return (left + right) / 2

            elif left1 > right2:
                high = partition1 - 1

            else:
                low = partition1 + 1