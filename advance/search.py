'''
查找算法
'''
import sort


print(dir(sort))
def seq_search(items, key):
    '''
    顺序查找
    '''
    for index, item in enumerate(items):
        if key == item:
            return index
    return -1

# 折半查找的前提是：查找的列表是已经排序过的。
# 其实就是二分法
def bin_search(items, key):
    '''
    折半查找
    '''
    start, end = 0, len(items) - 1
    while start <= end:
        mid = (start + end ) // 2
        if key > items[mid]:
            start = mid + 1
        elif key < items[end]:
            end = mid - 1
        else:
            return mid
    return -1

    

if __name__ == "__main__":
    items = [
        1,3,5,31,5,64,23,6,7,123,434,56,7,31
    ]
    sorted_list = sort.merge_sort(items)
    print(seq_search(items, 6))
    print(bin_search(sorted_list, 6))