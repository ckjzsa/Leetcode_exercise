class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while '{}' in s or '()' in s or '[]' in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return s == ''

    # Stack based solution
    class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        if len(s) == 0:
            return True

        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)

            elif i == ')':
                if len(stack) == 0:
                    return False
                elif stack[-1] != '(':
                    return False
                else:
                    stack.pop()
            elif i == ']':
                if len(stack) == 0:
                    return False
                elif stack[-1] != '[':
                    return False
                else:
                    stack.pop()
            elif i == '}':
                if len(stack) == 0:
                    return False
                elif stack[-1] != '{':
                    return False
                else:
                    stack.pop()
        return len(stack) == 0

    
