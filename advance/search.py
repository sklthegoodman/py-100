'''
查找算法
'''

def seq_search(items, key):
    '''
    顺序查找
    '''
    for index, item in enumerate(items):
        if key == item:
            return index
    return -1

def bin_search1(items, key):
    '''
    折半查找
    '''
    pass

    

if __name__ == "__main__":
    items = [
        1,3,5,31,5,64,23,6,7,123,434,56,7,31
    ]
    print(seq_search(items, 6))