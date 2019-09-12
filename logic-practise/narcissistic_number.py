'''
计算水仙花数 也就是三位的自幂数
    水仙花数是指一个 3 位数，它的每个位上的数字的 3次幂之和等于它本身（例如：1^3 + 5^3+ 3^3 = 153）
'''
import math
# from string import Template

def narcissistic(count):
    end = int(math.pow(10,int(count)))
    start = end // 10
    n_set = ['None','独身数','没有','水仙花数','四叶玫瑰数','五角星数','六合数','北斗七星数','八仙数','九九重阳数','十全十美数']
    print('我们现在计算的是%s：' % (n_set[count] or 'Noe') )
    
    cache = {}
    

    all_num = []
    for v in range(start,end):
        result = 0
        strv = str(v)
        if strv not in cache:
            for num in str(v):
                result += int(math.pow(int(num),count))
            cache[strv] = result
        else:
            result = cache[strv]            
        if result == v:
            all_num.append(result)

    if len(all_num):
        for n in all_num:
            print(n)
    else:
        print('没有这样的数哦')


# narcissistic(3)

for i in range(1,8):
    narcissistic(i)