# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
nums = []
target = 0
def twoSum(nums: list[int], target: int) -> list[int]:
    for number in nums:
        print("number:" + str(number))
        for number2 in nums:
            print("number2:" + str(number2))
            if target == number + number2:
                return nums.index(number), nums.index(number2)

print(twoSum([1,2,3,4,6],9))
