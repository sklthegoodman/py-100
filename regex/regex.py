'''
正则表达式
'''
import re

'''
验证输入用户名和QQ号是否有效并给出对应的提示信息。
'''
def verify_qq():
    # username = input('请输入用户名：')
    username = 'wrynxin'
    # qq = input('请输入QQ号：')
    qq = '109095682'
    # match函数的第一个参数是正则表达式字符串或正则表达式对象
    # 第二个参数是要跟正则表达式做匹配的字符串对象
    m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$',username)
    if not m1:
        print('请输入有效的用户名.')
    m2 = re.match(r'^[1-9]\d{4,11}$',qq)
    if not m2:
        print('请输入有效的QQ号.')
    if m1 and m2:
        print('你输入的信息是有效的!')
r'''
提示： 上面在书写正则表达式时使用了“原始字符串”的写法（在字符串前面加上了r），所谓“原始字符串”就是字符串中的每个字符都是它原始的意义，说得更直接一点就是字符串中没有所谓的转义字符啦。因为正则表达式中有很多元字符和需要进行转义的地方，如果不使用原始字符串就需要将反斜杠写作\\，例如表示数字的\d得书写成\\d，这样不仅写起来不方便，阅读的时候也会很吃力。
'''

'''
从一段文字中取出电话号码
'''
def abstract_phone_num():
    # 创建正则表达式对象 使用了前瞻和回顾来保证手机号前后不应该出现数字
    pattern = re.compile(r'(?<=\D)1[345789]\d{9}(?=\D)')
    sentence = '''
    重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
    不是15600998765，也是110或119，王大锤的手机号才是15600998765。
    '''
    # 查找所有匹配并保存到一个列表中
    str_list = re.findall(pattern,sentence)
    print(str_list)
    print('--------华丽的分隔线--------')
    # 通过迭代器取出匹配对象并获得匹配的内容
    str_iter = pattern.finditer(sentence)
    for tmp in str_iter:
        print(tmp.group())
    print('--------华丽的分隔线--------')
    # 通过search函数指定搜索位置找出所有匹配
    m = pattern.search(sentence)
    while m:
        print(m.group())
        m = pattern.search(sentence, m.end())
    
    


if __name__ == "__main__":
    # verify_qq()
    abstract_phone_num()