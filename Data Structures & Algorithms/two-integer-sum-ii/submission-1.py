class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ld = 0
        li = len(numbers)-1
        while ld<li:
            if numbers[ld]+numbers[li]==target:
                return [ld+1,li+1]
            if numbers[ld]+numbers[li]>target:
                li = li -1
            if numbers[ld]+numbers[li]<target:
                ld = ld +1