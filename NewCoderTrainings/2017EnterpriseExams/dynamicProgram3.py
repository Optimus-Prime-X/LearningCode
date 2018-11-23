# 一个袋子里面有n个球，每个球上面都有一个号码(拥有相同号码的球是无区别的)。如果一个袋子是幸运的当且仅当所有球的号码的和大于所有球的号码的积。
# 例如：如果袋子里面的球的号码是{1, 1, 2, 3}，这个袋子就是幸运的，因为1 + 1 + 2 + 3 > 1 * 1 * 2 * 3
# 你可以适当从袋子里移除一些球(可以移除0个,但是别移除完)，要使移除后的袋子是幸运的。现在让你编程计算一下你可以获得的多少种不同的幸运的袋子。
def solution():
    n = int(input())
    nums = sorted(list(map(int, input().strip().split())))
    counts = 0
    counts=nums.count(1)
    if counts == n: return n-1
    nums = nums[counts:]
    def dfs(id, sm, pr):
        lst = None
        result = counts - pr + sm
        for i in range(id, len(nums)):
            if nums[i] != lst:
                if (pr * nums[i]) - (sm + nums[i]) <counts:
                    result += dfs(i + 1, sm + nums[i], pr * nums[i])
                    lst = nums[i]
                else:
                    break
        return result
    return dfs(0, 0, 1)
print(solution())

