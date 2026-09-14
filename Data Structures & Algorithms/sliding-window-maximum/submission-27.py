class Solution:
    def maxSlidingWindow(self, nums: List[int], k): 

        hola = deque()

        res = []

        for i in range(len(nums)):
           

            while hola and i - k >= hola[0]:
                hola.popleft()

            while hola and nums[i] > nums[hola[-1]]:
                hola.pop()
            
            hola.append(i)


            if i - k + 1>= 0:
                res.append(nums[hola[0]])


        return res