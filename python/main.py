def leftpad(s:str, length:int, char:str=' '):
    """
    Pads the given string {s} with the specified character up to the desired length

    :param s: The original string
    :param length: The desired length of the result string
    :param char: the character to use for padding
    :return: The left padded string
    """

    if length <= len(s):
        return s
    padding = char * (length-len(s))
    return padding+s

def main():
    """Main function to demonstrate left_pad usage."""
    print(leftpad("42", 5, '0'))  # Output: "00042"
    print(leftpad("hello", 10, '*'))  # Output: "*****hello"
    print(leftpad("world", 5))  # Output: "world" (no padding needed)
    
if __name__ == '__main__':
    main()
