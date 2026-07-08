class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        [1,2,3,4]
         ^     ^
         -> if sum < target, move l
         -> if sum > target, move r
        """

        l = 0
        r = len(numbers) - 1

        while (l < r):
            sum = numbers[l] + numbers[r]
            print("numbers[l]:", numbers[l])
            print("numbers[r]: ", numbers[r])
            print(sum)
            if sum == target:
                return [l + 1,r + 1]
            if sum < target:
                l += 1
            elif sum > target:
                r -= 1            
        
        # return False
        