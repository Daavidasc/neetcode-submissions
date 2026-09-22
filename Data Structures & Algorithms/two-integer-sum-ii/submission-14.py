class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        li = 0
        ld = len(numbers)-1

        while ld > li:
            
            if numbers[ld] + numbers[li] > target:
                ld = ld-1
            elif numbers[ld] + numbers[li] < target:
                li = li + 1
            else:
                return [li+1,ld+1]
