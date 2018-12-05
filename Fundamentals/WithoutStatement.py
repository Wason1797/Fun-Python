# this one is an exercise program from HackerEarth

# Unfortunately someone has come and eaten the problem statement. Are you good enough to solve it without the statement?
# Input
# The first line contains T denoting the number of test cases. The next T lines describe test cases and contain two integers each: N and M.
# Output
# For each test case output one integer - answer for the question.
# Constraints
# T <= 1000
# 1 <= N, M <= 109
# Note: N, M <= 1000 for 30% of the test

# sample inputs:

# 6
# 28 1
# 39 1
# 90 1
# 15 2
# 123 2
# 114514 1919

# sample outputs:

# 68
# 90
# 81
# 40
# 17
# 16

# Solution:

cases = int(input())
result_arr = []
for i in range(cases):
    current_num, cases = map(int, input().split(' '))
    j = cases
    while j > 0:
        # this conditions are based on Guillermo_Casanova's solution
        if current_num == 1:
            break
        elif current_num == 4:
            if j >= 8:
                j = (j % 8)
                continue
            else:
                current_num = 16
        else:
            current_num = sum(int(var)**2 for var in str(current_num))
        j -= 1
    result_arr.append(current_num)

for elem in result_arr:
    print(elem)
