class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        day_stk = []
        t = temperatures
        l = len(temperatures)
        higher = [0]*l
        current_day = -1
        
        for i in range(0,l):
            if len(day_stk)==0:
                day_stk.append(i)
            
            # 温度低，入栈
            if t[day_stk[-1]] >= t[i]:
                day_stk.append(i)
            
            if t[i]>t[day_stk[-1]]:
                current_day = day_stk.pop()
                higher[current_day] = i-current_day
                while len(day_stk)>0:
                    current_day = day_stk[-1]
                    # 温度更高
                    if t[current_day]<t[i]:
                        current_day = day_stk.pop()
                        higher[current_day] = i-current_day
                    
                    # 遇到一个，打断
                    if t[current_day]>=t[i]:
                        break
                day_stk.append(i)
        
        return higher

# 逐步将天数对应的下标入栈，当一个下标入栈时，如果栈空，直接入，否则就和栈顶元素比较，保持栈顶的天数总是当前栈中温度最低的天数

# 如果栈顶天数的温度比当前入栈的天数的温度高，那么新来的这个天数放到栈顶

# 反之，如果栈顶天数的温度要更低，那么出栈，然后可以用i - stack[-1]来算出下一个温度更高的天出现隔了几天，出栈完后，继续进行比较

# 重复此过程，直到栈空，或者找到一个天数的温度比这一天要高为止，再将此元素压入栈中