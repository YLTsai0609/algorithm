'''
most stupid way
and best start way!

Time Complexity : O(N)
Space Complexity : O(1)
'''


def linear_search(value_you_want: float, input_list: list) -> int:

    for idx, element in enumerate(input_list):
        if element == value_you_want:
            return idx
    return -1


if __name__ == "__main__":
    input_list_1 = [12, 30, 44, 11, 30, 5]
    print(linear_search(value_you_want=44, input_list=input_list_1))
    print(linear_search(value_you_want=31, input_list=input_list_1))
