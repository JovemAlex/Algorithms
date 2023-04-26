def is_palindrome_iterative(word):
    if not isinstance(word, str) or len(word) == 0:
        return False

    low = 0
    high = len(word) - 1

    while low < high:
        if word[low] != word[high]:
            return False
        low += 1
        high -= 1

    return True
