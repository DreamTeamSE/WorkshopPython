"""
https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.

Input: using standard input, take in a space-separated list of numbers
-> line 1
-> line 2 -> target number
Output: print out the list in the format '[X, Y]' where X, Y are the two numbers
    that add to the target

    Input: 2 7 11 15
    target: 9
    output: [0,1] bc 2 + 7 =9

    take a stirng of input and make it a list of numbers
"""
#make function

def SolveToSum(nums, target):
   # pass ,pass does nothing, functions need one line though, need it

     for i, num1 in enumerate(inLine):
        #2, dont want to start at find index so i + 1 range to the length of inline
        for j in range(i+1, length(inLine)):
            if(num1 + inLine[j] == target):
           # return "["i + str(i) + "," + str(j) "]" --> below is easier way of this
                return "[%d, %d]" % (i,j)

     return "impossible"

#split function splits string into list based on space if specified in " "

inLine = input("Type the space - seperatedlist").split(" ") # "2 7 11 15" -> ["2", "7", "11", "15"]
target = int(input())

for i in range(length(inLine)):
    inLine[i] = int(inLine[i])

print(SolveTwoSum(inLine, target))

#for loop to go through and check inline input, in C++ {} -> python it is : space


    #need to check every number to check if they add up with another number to equal target
