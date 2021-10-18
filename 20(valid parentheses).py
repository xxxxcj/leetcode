class Stack:
    def __init__(self):
        self.__list = []

    def is_empty(self):
        return self.__list == []

    def push(self, x):
        self.__list.append(x)

    def pop(self):
        if self.is_empty():
            return
        else:
            return self.__list.pop()

    def top(self):
        if self.is_empty():
            return
        else:
            return self.__list[-1]

    def print_stack(self):
        print(self.__list)


class Solution:
    def isValid(self, s: str) -> bool:
        # 利用栈实现
        # stack = Stack()
        # left_parentheses = ['(', '[', '{']
        # dict = {
        #     '(': ')',
        #     '[': ']',
        #     '{': '}'
        # }
        # for parentheses in s:
        #     if parentheses in left_parentheses:
        #         stack.push(parentheses)
        #     else:
        #         if stack.is_empty() or dict[stack.top()] != parentheses:
        #             return False
        #         else:
        #             stack.pop()
        # if stack.is_empty():
        #     return True
        # else:
        #     return False

        # 直接队列
        list = []
        left_parentheses = ['(', '[', '{']
        dict = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        for parentheses in s:
            if parentheses in left_parentheses:
                list.append(parentheses)
            else:
                if len(list) == 0 or dict[list[-1]] != parentheses:
                    return False
                else:
                    list.pop()
        if len(list) == 0:
            return True
        else:
            return False


s = "()"
print(Solution().isValid(s))
