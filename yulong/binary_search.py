'''
very efficient!
but need to cheat, sorted
Time Complexity O(log_2 n)
Space Complexity O(1)

psudocode
TODO 或許需要雙指標來跳出死回圈
middle = (len(input) + 1) // 2
if not middle:
    return false
if middle > value_you_want:
    find the left
if middle < value_you_want:
    find the right
if middle == value_you_want: 
    return middle
'''


def binary_search(value_you_want: float, sordted_input_list: list) -> int:

    _length = len(sordted_input_list)
    mid = (_length + 1) // 2
    while True:
        if mid == 0 or mid > _length:
            return -1
        if sordted_input_list[mid] > value_you_want:
            mid = (mid + 0) // 2
        elif sordted_input_list[mid] < value_you_want:
            mid = (mid + _length) // 2
        else:
            return mid


# def bsearch(l, value):
#     lo, hi = 0, len(l) - 1
#     while lo <= hi:
#         mid = (lo + hi) / 2
#         if l[mid] < value:
#             lo = mid + 1
#         elif value < l[mid]:
#             hi = mid - 1
#         else:
#             return mid
#     return -1


if __name__ == "__main__":
    sorted_input_list_1 = [5, 11, 12, 30, 44, 50, 57]
    print(binary_search(value_you_want=44, sordted_input_list=sorted_input_list_1))
    print(binary_search(value_you_want=57, sordted_input_list=sorted_input_list_1))
    print(binary_search(value_you_want=11, sordted_input_list=sorted_input_list_1))
    print(binary_search(value_you_want=4, sordted_input_list=sorted_input_list_1))
    print(binary_search(value_you_want=14, sordted_input_list=sorted_input_list_1))
    print(binary_search(value_you_want=31, sordted_input_list=sorted_input_list_1))
