# Given an Array of integers
nums = [2, 7, 11, 15] 
target = 9
# Return indices of the two numbers such that they add up to a specific target.
# Because nums[0] + nums[1] = 2 + 7 = 9, return [0,1].

n = [i for i in nums]
m = [i for i in range(len(nums))]
J = [i for i in range(len(nums)-1)]
K = [i+1 for i in range(len(nums))]

print(n)
print(m)
print(J)
print(K)
print("-----------------")


q = [i for i in nums]
w = [nums[i] for i in range(len(nums))]
e = [nums[i] for i in range(len(nums)-1)]
r = [nums[i] for i in range(+1, len(nums))]

print(q)
print(w)
print(e)
print(r)