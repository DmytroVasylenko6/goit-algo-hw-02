from collections import deque


def check_palindrome(param):
    if len(param) == 0:
        return "Empty input"

    cleaned_phrase = param.lower().replace(" ", "")

    chars_dq = deque(cleaned_phrase)
    if chars_dq == deque(reversed(chars_dq)):
        return f"{param} is a palindrome"

    return f"{param} is not a palindrome"


def is_palindrome(param):
    if len(param) == 0:
        return "Empty input"

    cleaned_phrase = param.lower().replace(" ", "")

    chars_dq = deque(cleaned_phrase)
    while len(chars_dq) > 1:
        if chars_dq.popleft() != chars_dq.pop():
            return f"{param} is not a palindrome"

    return f"{param} is a palindrome"


try:
    txt = input("Type your test phrase: ")
    res = check_palindrome(txt)
    print("res: ", res)
    res2 = is_palindrome(txt)
    print("res2: ", res2)

except KeyboardInterrupt as err:
    print(err)
except ValueError as err:
    print(err)
