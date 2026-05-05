'''
Pos = right
neg = left
[2,4,-4,-1]

stack 2 4 -4 => 4 and -4 is gone
stack -4 2 => none is gone
stack 2 -4 => 2 is gone
'''
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for num in asteroids:
            if not stack or stack[-1] < 0 or num > 0:
                stack.append(num)
            else:
                while stack and stack[-1] > 0 and num < 0:
                    if stack[-1] > abs(num):
                        break
                    elif stack[-1] < abs(num):
                        stack.pop()
                       
                    else:
                        stack.pop()
                        break
                else:
                    stack.append(num)
            
      
        return stack
        