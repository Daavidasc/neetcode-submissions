class Solution:
    def maxSlidingWindow(self, nums: List[int], k): 

        hola = deque()

        res = []

        l = 0
        for r in range(len(nums)):
           

            if hola and l > hola[0]:
                hola.popleft()

            while hola and nums[r] > nums[hola[-1]]:
                hola.pop()
            
            hola.append(r)

            if r - k + 1>= 0:
                res.append(nums[hola[0]])
                l=l+1

        return res