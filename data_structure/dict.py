'''
字典
'''

def main():
    scores = {
        '猪儒':20,
        '林肯':12,
        '皮皮虾':30
    }
    # 从键获取
    print(scores['猪儒'])
    # 编辑
    for v in scores:
        print(v)
    # 更新元素
    scores['猪儒'] = 98
    scores.update(维尼=20,傻猪=0)
    print(scores)
    # 获取没有的键会报错，可以用get方法代替
    if '聪明猪' in scores:
        print(scores)
    print(scores.get('聪明猪'))
    # get可以在返回None的时候设置默认值
    print(scores.get('聪明猪',100))
    # 删除字典中的元素
    print(scores.popitem())
    print(scores.popitem())
    print(scores.pop('猪儒'))
    print(scores)
    # 清空字典
    scores.clear()
    print(scores)


if __name__ == '__main__':
    main()