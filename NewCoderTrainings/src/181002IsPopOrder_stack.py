# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if set(pushV) != set(popV):
            return False
        popV = popV[::-1]
        curr_index = pushV.index(popV.pop())
        curr_stack =pushV[:curr_index]
        while len(popV):
            curr_top = popV.pop()
            if pushV.index(curr_top) > curr_index:
                curr_stack += pushV[curr_index + 1:pushV.index(curr_top)]
                curr_index = pushV.index(curr_top)
            elif curr_top == curr_stack[-1]:
                curr_stack.pop()
            else:
                return False
        return True