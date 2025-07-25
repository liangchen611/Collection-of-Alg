import sys

s = sys.stdin.readline().strip()
p = sys.stdin.readline().strip()

def is_letter_or_digit(c):
    return c.isalnum()

def char_equal(p_char, t_char):
    # 大小写字母相等；其他字符必须完全相等
    if p_char.isalpha() and t_char.isalpha():
        return p_char.lower() == t_char.lower()
    return p_char == t_char

def is_match(pattern, target):
    pi = ti = 0
    star_idx = -1
    match = 0

    while ti < len(target):
        if pi < len(pattern):
            if pattern[pi] not in '*?':
                # 普通字符：必须相等
                if char_equal(pattern[pi], target[ti]):
                    pi += 1
                    ti += 1
                    continue
            elif pattern[pi] == '?':
                # ? 必须匹配 >=1 个字母或数字
                if ti >= len(target) or not is_letter_or_digit(target[ti]):
                    return False
                start = ti
                while ti < len(target) and is_letter_or_digit(target[ti]):
                    ti += 1
                pi += 1
                continue
            elif pattern[pi] == '*':
                # 记录 * 出现位置
                star_idx = pi
                match = ti
                pi += 1
                continue

        # 不匹配 → 回溯？
        if star_idx != -1:
            # 回溯到上一个 *
            pi = star_idx + 1
            match += 1
            # * 只能匹配字母或数字
            while match < len(target) and not is_letter_or_digit(target[match]):
                match += 1
            ti = match
        else:
            return False

    # target 匹配完了，检查 pattern 结尾是否都是 *
    while pi < len(pattern) and pattern[pi] == '*':
        pi += 1

    return pi == len(pattern)

if is_match(s,p):
    print("true")
elif is_match(s,p)==False:
    print("false")
    
'''
📜 举个例子：
模式串（pattern）：a*bc
目标串（target）：axyzbc
过程如下：

门牌写着 a，你看到第一个房间是 a → ✅匹配

门牌写着 * → 星号怪来了！它看后面是 x y z b，全部都是可吃的 → 全部吃掉！（贪心）

门牌继续：b → 你发现现在 target 已经到 c，不对啊，b对不上c！

星号怪回头：“我刚刚吃太多了，让我少吃点”

第二次吃 x y z → b 正好匹配 b ✅

然后 c → c ✅

✅ 成功匹配！
'''