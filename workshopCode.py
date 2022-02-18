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
#single line comment


def SolveTwoSum(nums, target):
    for i, num in enumerate(inline):
        for j in range(i+1, len(inline)):
            if(num + nums[j] == target):
                return "[%d, %d]" %(i, j)
    return "Impossible"
            

inline = input("Type in your array separated by spaces\n").split(" ")
target = int(input("Type target number\n"))
for i in range(len(inline)):
    inline[i] = int(inline[i])
    
print(SolveTwoSum(inline, target))
        
        