def text_indentation(text):
    """
    Prints a text with 2 new lines after
    each of these characters: ., ? and :.

    Args:
        text (str): The text to be printed.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    print_flag = False

    for char in text:
        if char == ' ' and print_flag:
            continue
        print(char, end="")
        if char in ".?:":
            print("\n\n")
            print_flag = True
        else:
            print_flag = False
