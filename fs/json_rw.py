'''
读写JSON文件

json模块主要有四个比较重要的函数，分别是：
    - dump  将Python对象按照JSON格式序列化到文件中
    - dumps  将Python对象处理成JSON格式的字符串
    - load  将文件中的JSON数据反序列化成对象
    - loads 将字符串的内容反序列化成Python对象
'''

import json

json_string = ''

'''
存数据
'''
def dump_json():
    my_dict = {
        'name': '猪儒',
        'age': 12,
        'qq': 123,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }

    try:
        # 转化为文字
        global json_string
        json_string = json.dumps(my_dict)
        print(json_string)
        # 保存到文件
        with open('dump.json','w+', encoding='utf-8') as f:
            json.dump(my_dict, f)

    except IOError as e:
        print(e)


'''
读数据
'''
def load_json():
    # 从字符串反序列
    json_dict = json.loads(json_string)
    print(json_dict)
    # 从文件反序列
    with open('dump.json','r+',encoding='utf-8') as f:
        json_dict = json.load(f)
        print(json_dict)


if __name__ == "__main__":
    dump_json()
    load_json()



'''
在Python中要实现序列化和反序列化除了使用json模块之外，还可以使用pickle和shelve模块
[异常处理的指导]](https://segmentfault.com/a/1190000007736783)
'''