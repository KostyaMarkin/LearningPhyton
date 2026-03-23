def can_form_palindrome(word):
    word = word.lower().replace(" ", "")

    char_count = {}
    for char in word:
        char_count[char] = char_count.get(char, 0) + 1

    odd_count = 0
    for count in char_count.values():
        if count % 2 != 0:
            odd_count += 1

    return odd_count <= 1


def form_palindrome(word):

    word = word.lower().replace(" ", "")

    if not can_form_palindrome(word):
        return None

    char_count = {}
    for char in word:
        char_count[char] = char_count.get(char, 0) + 1

    half = []
    middle = ""

    for char, count in char_count.items():
        half.append(char * (count // 2))

        if count % 2 != 0:
            middle = char

    left_part = "".join(half)
    palindrome = left_part + middle + left_part[::-1]

    return palindrome


input_string = input("Введите строку: ")
result = form_palindrome(input_string)

if result:
    print(f"Получившийся палиндром: {result}")
else:
    print("Из данного слова нельзя составить палиндром")

