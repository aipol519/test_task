def chars_to_brackets(string):
    result_string = string.lower()
    chars_dict = dict()

    for char in result_string:
       if char in chars_dict:
           chars_dict[char] = chars_dict[char] + 1
       else:
           chars_dict[char] = 0

    for key in chars_dict:
        if chars_dict[key] > 0:
            result_string = result_string.replace(key, ')')
        else:
            result_string = result_string.replace(key, '(')

    return result_string

if __name__ == "__main__":
    print("Enter string:")
    string = input()

    print("Result string: ", chars_to_brackets(string))