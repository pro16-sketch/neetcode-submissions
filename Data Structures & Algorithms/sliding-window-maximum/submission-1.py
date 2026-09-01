from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:


        result = []
        dq = deque()

        left = 0
        right = 0

        while right < len(nums):

            # Back se chhote elements hatao
            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()

            # Current element ka index add karo
            dq.append(right)

            # Window size k ho gayi
            if right - left + 1 == k:

                # Front wala maximum hai
                result.append(nums[dq[0]])

                # Agar front window se bahar ho gaya
                if dq[0] == left:
                    dq.popleft()

                # Window slide
                left += 1

            right += 1

        return result
        