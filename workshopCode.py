"""
https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.

Input: using standard input, take in a space-separated list of numbers
Output: print out the list in the format '[X, Y]' where X, Y are the two numbers
    that add to the target
"""

def SolveTwoSum(nums, target)
    #[2,7,11,15]
    for i, num1 in enumerate(nums):
        for j in range(i+1, len(nums)):
            if (num1 + nums[j] == target):
                return "[%d,%d]" % (i, j)
    
    return "impossible"

inLine = input("Type the space-separated list of numbers ").split(" ")
target = int(input("Type the target"))

for i in range(len(inLine)):
    inLine[i] = int(inLine[i])
    
print(SolveTwoSum(inLine, target))
