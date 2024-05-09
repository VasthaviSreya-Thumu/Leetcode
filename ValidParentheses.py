class Solution(object):
    def isValid(self, s):
        l = [" "]
        k = {"{": "}", "[": "]", "(": ")", " ": "x"}
        for i in s:
            if i in "([{":
                l.append(i)
            else:
                t = l[-1]
                if (i == k[t]):
                    l.pop()
                else:
                    return False
        return l == [" "]
