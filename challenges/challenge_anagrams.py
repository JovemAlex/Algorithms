def quicksort(string):
    string_list = list(string)
    if len(string_list) < 2:
        return string_list
    else:
        pivot = string_list[-1]
        left_list = []
        right_list = []
        for i in range(len(string_list) - 1):
            if string_list[i] < pivot:
                left_list.append(string_list[i])
            else:
                right_list.append(string_list[i])
        return quicksort(left_list) + [pivot] + quicksort(right_list)


def is_anagram(first_string, second_string):

    first_str = "".join(quicksort(first_string.lower()))
    second_str = "".join(quicksort(second_string.lower()))

    if len(first_str) == 0 or len(second_str) == 0:
        return (first_str, second_str, False)

    if first_str == second_str:
        return (first_str, second_str, True)
    else:
        return (first_str, second_str, False)
